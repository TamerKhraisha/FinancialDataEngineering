import psycopg2
import os
import string
import random
from datetime import datetime, timedelta

def generate_tracking_number():
    return ''.join(random.choices(string.digits, k = 10))

def generate_delivery_date():
    # Get the current date
    current_date = datetime.now()
    # Calculate the date after 3 days (let's assume delivery takes places after 3 days)
    date_after_10_days = current_date + timedelta(days=3)
    # Format the date as YYYY-MM-DD
    formatted_date = date_after_10_days.strftime('%Y-%m-%d')
    return formatted_date


def schedule_delivery(order_id: int):
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
                # Schedule delivery
                tracking_number = generate_tracking_number()
                delivery_date = generate_delivery_date()

                cursor.execute(
                    "UPDATE DeliverySchedule SET delivery_service = 'DHL Express', expected_delivery_date=%s, tracking_number=%s WHERE order_id = %s;",
                    (delivery_date, tracking_number, order_id)
                )

                # Commit the transaction
                connection.commit()

        print("Delivery added to DeliverySchedule table successfully!")
        return {'success': True, 'order_id': order_id, 'notification': 'Your order has been shipped and is on its way to the delivery address.'}
    except psycopg2.Error as e:
        print("Error: Unable to add delivery to DeliverySchedule table:", e)
        return {'success': False, 'order_id': order_id, 'notification': 'Your order could not be processed due to an unexpected error. Please contact customer support for assistance.'}
