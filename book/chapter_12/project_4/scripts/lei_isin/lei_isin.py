import requests
import zipfile
import io
import pandas as pd
import os
import psycopg2
import pandas as pd
from io import StringIO

# Function to extract, download, and read a zip file containing a CSV file
def download_and_extract_zip(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Read the content of the response as bytes
        zip_content = response.content
        
        # Create a file-like object from the bytes content
        zip_file = io.BytesIO(zip_content)
        
        # Extract the contents of the zip file
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            # Assume the zip file contains only one CSV file
            csv_filename = zip_ref.namelist()[0]
            
            # Extract the CSV file to the data directory 
            destination_directory = '../../data'
            extract_path = os.path.join(destination_directory, csv_filename)
            zip_ref.extract(csv_filename, destination_directory)
            
            print(f"CSV file '{csv_filename}' extracted successfully.")

            
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(extract_path)
            
            return df
    else:
        print("Failed to download the zip file.")
        return None

# Function to connect to PostgreSQL database and insert data using bulk insert
def bulk_insert_data(df):
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        dbname=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        host=os.environ.get('POSTGRES_HOST'),
        port=os.environ.get('POSTGRES_PORT')
    )

    cursor = connection.cursor()
    
    # Create a buffer to hold the CSV data
    buffer = StringIO()
    
    # Write DataFrame to buffer as a CSV string
    df.to_csv(buffer, index=False, header=False)
    
    # Move buffer cursor to the start
    buffer.seek(0)
    
    # Execute bulk insert using copy_from() method
    cursor.copy_from(buffer, 'lei_isin', sep=',', columns=('lei', 'isin'))
    
    # Commit changes to the database
    connection.commit()
    cursor.close()
    print(f"Successfully inserted {len(df)} rows into the 'lei_isin' table!")