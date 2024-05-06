import psycopg2
import psycopg2.sql as sql
import os

def acknowledge_order(customer_id: int, products: dict, payment_amount: float, delivery_address: str) -> dict:
    # Connection parameters
    connection_params = {
        'host': os.environ.get('POSTGRES_HOST'),
        'port': os.environ.get('POSTGRES_PORT'),
        'database': os.environ.get('POSTGRES_DB'),
        'user': os.environ.get('POSTGRES_USER'),
        'password': os.environ.get('POSTGRES_PASSWORD')
    }

    # Start a transaction
    try:
        # Establish a connection to the PostgreSQL database
        with psycopg2.connect(**connection_params) as connection:
            # Set autocommit to False to start a transaction
            connection.autocommit = False

            # Create a cursor
            with connection.cursor() as cursor:
                # Insert order into Orders table
                cursor.execute(
                    sql.SQL("INSERT INTO Orders (customer_id, order_status) VALUES (%s, %s) RETURNING order_id;"),
                    (customer_id, 'Pending')
                )
                order_id = cursor.fetchone()[0]  # Get the order_id of the inserted order

                # Insert payment with pending status into Payments table
                cursor.execute(
                    sql.SQL("INSERT INTO Payments (order_id, amount, payment_method, payment_status) VALUES (%s, %s, %s, %s);"),
                    (order_id, payment_amount, 'Credit Card', 'Pending')
                )

                # Insert stock booking records into StockBookings table
                for product_id, quantity in products.items():
                    cursor.execute(
                        sql.SQL("INSERT INTO StockBookings (order_id, product_id, quantity) VALUES (%s, %s, %s);"),
                        (order_id, product_id, quantity)
                    )

                # Insert delivery records into the DeliverySchedule table
                cursor.execute(
                    sql.SQL("INSERT INTO DeliverySchedule (order_id, delivery_address) VALUES (%s, %s);"),
                    (order_id, delivery_address)
                )

                # Commit the transaction
                connection.commit()
                print("Data inserted into DeliverySchedule successfully!")


                # Commit the transaction
                connection.commit()
                print("Transaction committed successfully!")
                return {'success': True, 'order_id': order_id, 'notification': 'Your order has been received and is currently being processed.'}
    except psycopg2.Error as e:
        print("Error: Unable to perform transaction:", e)
        return {'success': False, 'order_id': None, 'notification': 'Your order could not be processed due to an unexpected error. Please contact customer support for assistance.'}


