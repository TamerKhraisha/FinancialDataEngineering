import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
import os


def get_mic_codes():
    # URL of the CSV file
    url = "https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.csv"
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(url)

    # rename columns
    df.columns = ['mic', 'operating_mic', 'oprt_sgmt', 'market_name_institution_description', 'legal_entity_name', 'lei', 'market_category_code', 'acronym', 'iso_country_code', 'city', 'website', 'status', 'creation_date', 'last_update_date', 'last_validation_date', 'expiry_date', 'comments']

    # Convert date strings to date
    df['creation_date'] = pd.to_datetime(df['creation_date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
    df['last_update_date'] = pd.to_datetime(df['last_update_date'], format='%Y%m%d')
    df['last_validation_date'] = pd.to_datetime(df['last_validation_date'], format='%Y%m%d').fillna(pd.Timestamp('1900-01-01'))
    df['expiry_date'] = pd.to_datetime(df['expiry_date'], format='%Y%m%d').dt.strftime('%Y-%m-%d').fillna(pd.Timestamp('2100-01-01'))
    df['iso_country_code'] = df['iso_country_code'].fillna("")

    # Remove NaT null values from expiry_date column
    #df['last_validation_date'] = df['last_validation_date'].apply(lambda x: x.strftime('%Y-%m-%d')if not pd.isnull(x) else '')
    #df['expiry_date'] = df['expiry_date'].apply(lambda x: x.strftime('%Y-%m-%d')if not pd.isnull(x) else '')
    
    
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
        INSERT INTO mic ({})
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
    print(f"Successfully inserted {len(df)} rows into the 'mic' table!")