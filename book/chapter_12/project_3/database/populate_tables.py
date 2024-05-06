import psycopg2
import os

connection_params = {
    'host': os.environ.get('POSTGRES_HOST'),
    'port': os.environ.get('POSTGRES_PORT'),
    'database': os.environ.get('POSTGRES_DB'),
    'user': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD')
}

def insert_into_inventory(data):
    try:
        # Establish a connection to the PostgreSQL database
        with psycopg2.connect(**connection_params) as connection:
            # Create a cursor
            with connection.cursor() as cursor:
                # Execute the INSERT statement for inventory data
                cursor.executemany(
                    "INSERT INTO Inventory (product_name, quantity) VALUES (%s, %s)",
                    data
                )

                # Commit the transaction for inventory data
                connection.commit()
                print("Data inserted into Inventory successfully!")

    except psycopg2.Error as e:
        print("Error: Unable to insert data into Inventory:", e)

def insert_into_customers(data):
    try:
        # Establish a connection to the PostgreSQL database
        with psycopg2.connect(**connection_params) as connection:
            # Create a cursor
            with connection.cursor() as cursor:
                # Execute the INSERT statement for customer data
                cursor.executemany(
                    "INSERT INTO Customers (customer_name, email, country, city, street, phone_number, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    data
                )

                # Commit the transaction for customer data
                connection.commit()
                print("Data inserted into Customers successfully!")

    except psycopg2.Error as e:
        print("Error: Unable to insert data into Customers:", e)

if __name__ == "__main__":
    # Define the data to be inserted into the Inventory table
    inventory_data = [
        ('Product A', 100),
        ('Product B', 50),
        ('Product C', 200),
        ('Product D', 75),
        ('Product E', 150)
    ]

    # Define the data to be inserted into the Customers table
    customer_data = [
        ('John Doe', 'john@example.com', 'USA', 'New York', '123 Main St', '123-456-7890', 'Active'),
        ('Jane Smith', 'jane@example.com', 'Canada', 'Toronto', '456 Maple Ave', '987-654-3210', 'Active'),
        ('Alice Johnson', 'alice@example.com', 'UK', 'London', '789 Oak St', '456-789-0123', 'Active'),
        ('Bob Brown', 'bob@example.com', 'Germany', 'Berlin', '321 Elm St', '789-012-3456', 'Active'),
        ('Charlie Chang', 'charlie@example.com', 'China', 'Beijing', '654 Pine St', '012-345-6789', 'Active')
    ]

    # Call the function to insert data into the Inventory table
    insert_into_inventory(inventory_data)

    # Call the function to insert data into the Customers table
    insert_into_customers(customer_data)