import requests
import json
import pandas as pd
import os
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values

def search_by_ticker_and_mic(ticker: str, mic: str):
    url = f'https://api-eit.refinitiv.com/permid/search?q=ticker:{ticker}%20AND%20mic:{mic}'
    access_token = os.environ['PERMID_API_KEY']
    headers = {'X-AG-Access-Token' : access_token}
    try:
        response = requests.get(url, headers=headers)
    except Exception  as e:
        print ('Error in connect ' , e)
        return
    if response.status_code == 200:
        return response.json()

def parse_permid_search_output(output_json: dict):
    try:
        organizations_data = []
        for entity in output_json.get('result', {}).get('organizations', {}).get('entities', {}):
            organizations_data.append([
                entity.get('@id'),
                entity.get('organizationName'),
                entity.get('primaryTicker'),
                entity.get('orgSubtype'),
                entity.get('hasHoldingClassification'),
                entity.get('hasURL')
            ])
        
        instruments_data = []
        for entity in output_json.get('result', {}).get('instruments', {}).get('entities', []):
            instruments_data.append([
                entity.get('@id'),
                entity.get('hasName'),
                entity.get('assetClass'),
                entity.get('isIssuedByName'),
                entity.get('primaryTicker')
            ])
        
        quotes_data = []
        for entity in output_json.get('result', {}).get('quotes', {}).get('entities', []):
            quotes_data.append([
                entity.get('@id'),
                entity.get('hasName'),
                entity.get('assetClass'),
                entity.get('hasRIC'),
                entity.get('hasMic'),
                entity.get('hasExchangeTicker')
            ])
        
        # Create DataFrames
        organizations_df = pd.DataFrame(organizations_data, columns=['organization_id', 'organization_name', 'organization_primary_ticker', 'organization_subtype', 'organization_has_holding_classification', 'organization_webpage'])
        instruments_df = pd.DataFrame(instruments_data, columns=['instrument_id', 'instrument_name', 'instrument_asset_class', 'instrument_is_issued_by_name', 'instrument_primary_ticker'])
        quotes_df = pd.DataFrame(quotes_data, columns=['quote_id', 'quote_name', 'quote_asset_class', 'quote_ric', 'quote_mic', 'quote_exchange_ticker'])
        
        full_df = pd.concat([organizations_df, instruments_df, quotes_df], axis=1)
    
        return full_df

    except Exception as e:
        print(f"failed to parse the output: {e}")


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
        INSERT INTO permid ({})
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
    print(f"Successfully inserted {len(df)} rows into the permid table!")