import psycopg2
import os

def process_payment(order_id: int):
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
                # Update payment status to 'Paid' for the given order ID
                cursor.execute(
                    "UPDATE Payments SET payment_status = 'Paid' WHERE order_id = %s;",
                    (order_id,)
                )
                # Commit the transaction
                connection.commit()
                print("Payment status updated to 'Paid' for order ID:", order_id)
                return {'success': True, 'order_id': order_id, 'notification': 'Payment for your order has been successfully processed.'}
        return order_id
    except psycopg2.Error as e:
        print("Error: Unable to update payment status:", e)
        return {'success': False, 'order_id': order_id, 'notification': 'There was an issue processing your payment. Please contact customer support for assistance.'}
