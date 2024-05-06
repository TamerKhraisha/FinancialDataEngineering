import psycopg2
import os

# Function to update inventory based on stock bookings of an order
def update_inventory(order_id: int) -> dict:
    # Connection parameters
    connection_params = {
        'host': os.environ.get('POSTGRES_HOST'),
        'port': os.environ.get('POSTGRES_PORT'),
        'database': os.environ.get('POSTGRES_DB'),
        'user': os.environ.get('POSTGRES_USER'),
        'password': os.environ.get('POSTGRES_PASSWORD')
    }
    try:
        # Establish a connection to the PostgreSQL database
        with psycopg2.connect(**connection_params) as connection:
            # Create a cursor
            with connection.cursor() as cursor:
                # Get stock bookings for the given order ID
                cursor.execute(
                    "SELECT product_id, quantity FROM StockBookings WHERE order_id = %s;",
                    (order_id,)
                )
                stock_bookings = cursor.fetchall()  # Fetch all stock bookings

                # Update inventory based on stock bookings
                for product_id, quantity in stock_bookings:
                    cursor.execute(
                        "UPDATE Inventory SET quantity = quantity - %s WHERE product_id = %s;",
                        (quantity, product_id)
                    )

                # Commit the transaction
                connection.commit()
        print("Inventory updated based on stock bookings for order ID:", order_id)
        return {'success': True, 'order_id': order_id, 'notification': 'Stock for your order has been booked and is being prepared for shipment.'}

    except psycopg2.Error as e:
        print("Error: Unable to update inventory:", e)
        return {'success': False, 'order_id': order_id, 'notification': 'Your order could not be processed due to an unexpected error. Please contact customer support for assistance.'}
