import requests
import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
import os

def fetch_lei_records(page_size=200, page_number=1):
    # Define the endpoint URL
    url = f"https://api.gleif.org/api/v1/lei-records?page[size]={page_size}&page[number]={page_number}"
    
    try:
        # Send a GET request to the endpoint
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the "data" field from the response
            lei_records = data.get("data")
            
            # Return the lei_records data
            return lei_records
        else:
            print(f"Failed to fetch LEI records. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to extract relevant data and create DataFrame
def parse_lei_records(json_data):
    records = []
    for item in json_data:
        record = {
            'lei': item.get('attributes', {}).get('lei', ''),
            'legal_name': item.get('attributes', {}).get('entity', {}).get('legalName', {}).get('name', ''),
            'jurisdiction': item.get('attributes', {}).get('entity', {}).get('jurisdiction', ''),
            'category': item.get('attributes', {}).get('entity', {}).get('category', ''),
            'status': item.get('attributes', {}).get('entity', {}).get('status', ''),
            'legal_form_id': item.get('attributes', {}).get('entity', {}).get('legalForm', {}).get('id', ''),
            'legal_address_city': item.get('attributes', {}).get('entity', {}).get('legalAddress', {}).get('city', ''),
            'legal_address_country': item.get('attributes', {}).get('entity', {}).get('legalAddress', {}).get('country', ''),
            'legal_address_postal_code': item.get('attributes', {}).get('entity', {}).get('legalAddress', {}).get('postalCode', ''),
            'headquarters_city': item.get('attributes', {}).get('entity', {}).get('headquartersAddress', {}).get('city', ''),
            'headquarters_country': item.get('attributes', {}).get('entity', {}).get('headquartersAddress', {}).get('country', ''),
            'headquarters_postal_code': item.get('attributes', {}).get('entity', {}).get('headquartersAddress', {}).get('postalCode', '')
        }
        records.append(record)
    df = pd.DataFrame(records)
    return df

def insert_data_into_db(df):

    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        host=os.environ.get('POSTGRES_HOST'),
        port=os.environ.get('POSTGRES_PORT')
    )

    # Create a cursor object
    cur = conn.cursor()
    
    # Define the INSERT query
    insert_query = sql.SQL("""
        INSERT INTO lei ({})
        VALUES %s;
    """).format(
        sql.SQL(', ').join(map(sql.Identifier, df.columns))
    )
    
    # Convert DataFrame to list of tuples
    data = [tuple(row) for row in df.to_numpy()]
    
    # Execute the INSERT query
    execute_values(cur, insert_query, data)
    
    # Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cur.close()
    conn.close()
    print(f"Successfully inserted {len(df)} rows into the 'lei' table!")