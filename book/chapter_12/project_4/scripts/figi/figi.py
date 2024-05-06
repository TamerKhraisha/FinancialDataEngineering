import json
import urllib.request
import urllib.parse
import json
import random
import io
import pandas as pd
import os
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
import pandas as pd

"""
See https://www.openfigi.com/api for more information.
"""

openfigi_apikey = ''  # Put API Key here if you have an institutional account

def map_jobs(jobs):
    '''
    Send an collection of mapping jobs to the API in order to obtain the
    associated FIGI(s).

    Parameters
    ----------
    jobs : list(dict)
        A list of dicts that conform to the OpenFIGI API request structure. See
        https://www.openfigi.com/api#request-format for more information. Note
        rate-limiting requirements when considering length of `jobs`.

    Returns
    -------
    list(dict)
        One dict per item in `jobs` list that conform to the OpenFIGI API
        response structure.  See https://www.openfigi.com/api#response-fomats
        for more information.
    '''
    handler = urllib.request.HTTPHandler()
    opener = urllib.request.build_opener(handler)
    openfigi_url = 'https://api.openfigi.com/v2/mapping'
    request = urllib.request.Request(openfigi_url, data=bytes(json.dumps(jobs), encoding='utf-8'))
    request.add_header('Content-Type','application/json')
    if openfigi_apikey:
        request.add_header('X-OPENFIGI-APIKEY', openfigi_apikey)
    request.get_method = lambda: 'POST'
    connection = opener.open(request)
    if connection.code != 200:
        raise Exception('Bad response code {}'.format(str(response.status_code)))
    return json.loads(connection.read().decode('utf-8'))

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
        INSERT INTO figi ({})
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
    print(f"Successfully inserted {len(df)} rows into the 'figi' table.")
