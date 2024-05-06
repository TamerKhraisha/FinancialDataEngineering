import psycopg2
from psycopg2 import sql
import os

# Establish a connection to the PostgreSQL database
connection = psycopg2.connect(
    dbname=os.environ.get('POSTGRES_DB'),
    user=os.environ.get('POSTGRES_USER'),
    password=os.environ.get('POSTGRES_PASSWORD'),
    host=os.environ.get('POSTGRES_HOST'),
    port=os.environ.get('POSTGRES_PORT')
)

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# Define the CREATE TABLE statement
create_lei_isin_table = sql.SQL("""
    CREATE TABLE IF NOT EXISTS lei_isin (
        isin CHAR(12) NOT NULL,
        lei CHAR(20) NOT NULL,
        ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

create_lei_bic_table = sql.SQL("""
    CREATE TABLE IF NOT EXISTS lei_bic (
        bic VARCHAR NOT NULL,
        lei CHAR(20) NOT NULL,
        ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

create_country_table = sql.SQL("""
    CREATE TABLE IF NOT EXISTS country (
        name VARCHAR NOT NULL,
        code CHAR(2) NOT NULL,
        ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

create_mic_table = sql.SQL("""
    CREATE TABLE IF NOT EXISTS mic (
        mic CHAR(4) NOT NULL,
        operating_mic VARCHAR,
        oprt_sgmt VARCHAR,
        market_name_institution_description VARCHAR,
        legal_entity_name VARCHAR,
        lei CHAR(20),
        market_category_code VARCHAR,
        acronym VARCHAR,
        iso_country_code CHAR(2),
        city VARCHAR,
        website VARCHAR,
        status VARCHAR,
        creation_date DATE,
        last_update_date DATE,
        last_validation_date DATE,
        expiry_date DATE,
        comments TEXT,
        ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

create_figi_table = sql.SQL("""
    CREATE TABLE IF NOT EXISTS figi (
        figi CHAR(12),
        composite_figi CHAR(12),
        share_class_figi CHAR(12),
        isin CHAR(12),
        name VARCHAR,
        ticker VARCHAR,
        exch_code VARCHAR,
        mic_code CHAR(4),
        security_type VARCHAR,
        market_sector VARCHAR,
        security_type2 VARCHAR,
        security_description VARCHAR,
        ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

create_lei_table = sql.SQL("""
CREATE TABLE IF NOT EXISTS lei (
    lei CHAR(20),
    legal_name VARCHAR,
    jurisdiction VARCHAR,
    category VARCHAR,
    status VARCHAR,
    legal_form_id VARCHAR,
    legal_address_city VARCHAR,
    legal_address_country VARCHAR,
    legal_address_postal_code VARCHAR,
    headquarters_city VARCHAR,
    headquarters_country VARCHAR,
    headquarters_postal_code VARCHAR,
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

create_permid_table = sql.SQL("""
CREATE TABLE IF NOT EXISTS permid (
    organization_id VARCHAR,
    organization_name VARCHAR,
    organization_primary_ticker VARCHAR,
    organization_subtype VARCHAR,
    organization_has_holding_classification VARCHAR,
    organization_webpage VARCHAR,
    instrument_id VARCHAR,
    instrument_name VARCHAR,
    instrument_asset_class VARCHAR,
    instrument_is_issued_by_name VARCHAR,
    instrument_primary_ticker VARCHAR,
    quote_id VARCHAR,
    quote_name VARCHAR,
    quote_asset_class VARCHAR,
    quote_ric VARCHAR,
    quote_mic VARCHAR,
    quote_exchange_ticker VARCHAR,
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Execute the CREATE TABLE statement
try:
    cursor.execute(create_lei_isin_table)
    cursor.execute(create_country_table)
    cursor.execute(create_mic_table)
    cursor.execute(create_figi_table)
    cursor.execute(create_lei_table)
    cursor.execute(create_lei_bic_table)
    cursor.execute(create_permid_table)
    connection.commit()
    print("Tables created successfully")
except psycopg2.Error as e:
    print("Error creating table:", e)

# Close the cursor and connection
cursor.close()
connection.close()
