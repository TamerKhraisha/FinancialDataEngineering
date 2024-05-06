import requests
import zipfile
import io
import pandas as pd
import os
import psycopg2
from psycopg2 import sql
import pandas as pd
from io import StringIO

def fetch_countries_data(api_url):
    try:
        response = requests.get(api_url, headers={"Accept": "application/vnd.api+json"})
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        
        data = response.json().get("data", [])
        
        if data:
            countries = []
            for country in data:
                attributes = country.get("attributes", {})
                code = attributes.get("code")
                name = attributes.get("name")
                countries.append({"code": code, "name": name})
            
            return pd.DataFrame(countries)
        else:
            print("No data found.")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return pd.DataFrame()


def insert_data_into_db(df):
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        host=os.environ.get('POSTGRES_HOST'),
        port=os.environ.get('POSTGRES_PORT')
    )
    
    # Open a cursor to perform database operations
    cur = conn.cursor()
    
    # Iterate over the DataFrame rows and insert each row into the table
    for index, row in df.iterrows():
        insert_query = sql.SQL("""
        INSERT INTO country (code, name) VALUES (%s, %s)
        """)
        cur.execute(insert_query, (row['code'], row['name']))
    
    # Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cur.close()
    conn.close()
    print(f"Successfully inserted {len(df)} rows into the 'country' table.")