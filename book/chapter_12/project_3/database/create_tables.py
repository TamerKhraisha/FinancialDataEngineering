import psycopg2
import os

# Database connection parameters
connection_params = {
    'host': os.environ.get('POSTGRES_HOST'),
    'port': os.environ.get('POSTGRES_PORT'),
    'database': os.environ.get('POSTGRES_DB'),
    'user': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD')
}

# SQL statements to create enum types
create_enum_order_status = """
    CREATE TYPE OrderStatus AS ENUM ('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled');
"""

create_enum_payment_status = """
    CREATE TYPE PaymentStatus AS ENUM ('Pending', 'Paid', 'Failed', 'Refunded');
"""

create_enum_payment_method = """
    CREATE TYPE PaymentMethod AS ENUM ('Credit Card', 'PayPal', 'Cash on Delivery', 'Bank Transfer', 'Other');
"""

create_enum_customer_status = """
CREATE TYPE CustomerStatus AS ENUM ('Active', 'Inactive', 'Pending');
"""

create_enum_delivery_status = """
CREATE TYPE DeliveryStatus AS ENUM ('Not Scheduled' ,'Scheduled', 'In Transit', 'Delivered', 'Failed');
"""

# SQL statements to create tables
create_table_customers = """
    CREATE TABLE Customers (
        customer_id SERIAL PRIMARY KEY,
        customer_name VARCHAR NOT NULL,
        email VARCHAR NOT NULL UNIQUE,
        country VARCHAR,
        city VARCHAR,
        street VARCHAR,
        phone_number VARCHAR NOT NULL,
        registration_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status CustomerStatus NOT NULL
    );
"""

create_table_orders = """
    CREATE TABLE Orders (
        order_id SERIAL PRIMARY KEY,
        customer_id INT NOT NULL REFERENCES Customers(customer_id),
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        acknowledged_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        order_status OrderStatus NOT NULL
    );
"""

create_table_payments = """
    CREATE TABLE Payments (
        payment_id SERIAL PRIMARY KEY,
        order_id INT REFERENCES Orders(order_id),
        payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        amount DECIMAL(10,2) NOT NULL,
        payment_method PaymentMethod NOT NULL,
        payment_status PaymentStatus NOT NULL
    );
"""

create_table_inventory = """
    CREATE TABLE Inventory (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR NOT NULL,
        quantity INT NOT NULL CHECK (quantity >= 0)
    );
"""

create_table_stock_bookings = """
    CREATE TABLE StockBookings (
        booking_id SERIAL PRIMARY KEY,
        order_id INT NOT NULL REFERENCES Orders(order_id),
        product_id INT NOT NULL REFERENCES Inventory(product_id),
        quantity INT NOT NULL,
        booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

create_table_delivery_schedule = """
    CREATE TABLE DeliverySchedule (
        delivery_id SERIAL PRIMARY KEY,
        order_id INT REFERENCES Orders(order_id),
        expected_delivery_date DATE,
        delivery_address VARCHAR NOT NULL,
        delivery_service VARCHAR,
        tracking_number BIGINT,
        status DeliveryStatus NOT NULL DEFAULT 'Not Scheduled'
    );
"""

create_table_order_notifications = """
    CREATE TABLE OrderNotifications (
        notification_id SERIAL PRIMARY KEY,
        order_id INT NOT NULL REFERENCES Orders(order_id),
        notification_text TEXT NOT NULL,
        notification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

# SQL statements to drop tables
drop_table_order_notifications = "DROP TABLE IF EXISTS OrderNotifications CASCADE;"
drop_table_delivery_schedule = "DROP TABLE IF EXISTS DeliverySchedule CASCADE;"
drop_table_stock_bookings = "DROP TABLE IF EXISTS StockBookings CASCADE;"
drop_table_inventory = "DROP TABLE IF EXISTS Inventory CASCADE;"
drop_table_payments = "DROP TABLE IF EXISTS Payments CASCADE;"
drop_table_orders = "DROP TABLE IF EXISTS Orders CASCADE;"
drop_table_customers = "DROP TABLE IF EXISTS Customers CASCADE;"

# SQL statements to drop enum types
drop_enum_order_status = "DROP TYPE IF EXISTS OrderStatus;"
drop_enum_payment_status = "DROP TYPE IF EXISTS PaymentStatus;"
drop_enum_payment_method = "DROP TYPE IF EXISTS PaymentMethod;"
drop_enum_customer_status = "DROP TYPE IF EXISTS CustomerStatus;"
drop_enum_delivery_status = "DROP TYPE IF EXISTS DeliveryStatus"

# Function to execute SQL statements
def execute_sql(sql):
    try:
        # Connect to the PostgreSQL database
        with psycopg2.connect(**connection_params) as connection:
            # Create a cursor
            with connection.cursor() as cursor:
                # Execute SQL statement
                cursor.execute(sql)
                print("SQL executed successfully.")
    except psycopg2.Error as e:
        print("Error executing SQL:", e)



if __name__ == "__main__":
    # Drop the tables if they exist
    execute_sql(drop_table_order_notifications)
    execute_sql(drop_table_delivery_schedule)
    execute_sql(drop_table_stock_bookings)
    execute_sql(drop_table_inventory)
    execute_sql(drop_table_payments)
    execute_sql(drop_table_orders)
    execute_sql(drop_table_customers)

    # Drop the enums if they exist
    execute_sql(drop_enum_order_status)
    execute_sql(drop_enum_payment_status)
    execute_sql(drop_enum_payment_method)
    execute_sql(drop_enum_customer_status)
    execute_sql(drop_enum_delivery_status)

    # Execute enum creation SQL statements
    execute_sql(create_enum_order_status)
    execute_sql(create_enum_payment_status)
    execute_sql(create_enum_payment_method)
    execute_sql(create_enum_customer_status)
    execute_sql(create_enum_delivery_status)
    
    # Execute table creation SQL statements
    execute_sql(create_table_customers)
    execute_sql(create_table_orders)
    execute_sql(create_table_payments)
    execute_sql(create_table_inventory)
    execute_sql(create_table_stock_bookings)
    execute_sql(create_table_delivery_schedule)
    execute_sql(create_table_order_notifications)