"""Notification Service"""

import psycopg2
import os

def notify_customer(order_id: int, notification_text: str) -> dict:
    # Connection parameters
    connection_params = {
        'host': os.environ.get('POSTGRES_HOST'),
        'port': os.environ.get('POSTGRES_PORT'),
        'database': os.environ.get('POSTGRES_DB'),
        'user': os.environ.get('POSTGRES_USER'),
        'password': os.environ.get('POSTGRES_PASSWORD')
    }

    # INSERT statement with placeholders for parameters
    sql = """
        INSERT INTO OrderNotifications (order_id, notification_text)
        VALUES (%s, %s);
    """

    try:
        # Establish a connection to the PostgreSQL database
        with psycopg2.connect(**connection_params) as connection:
            with connection.cursor() as cursor:
                # Execute the INSERT statement with parameters
                cursor.execute(sql, (order_id, notification_text))
                # Commit the transaction
                connection.commit()
                print("Notification inserted successfully!")
        return {'success': True, 'order_id': order_id}
    except psycopg2.Error as e:
        print("Error: Unable to insert notification:", e)
        return {'success': False}