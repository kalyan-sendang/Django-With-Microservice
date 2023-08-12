import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()


def publish(user_id, product_id):

    exchange_name = 'user_favorite_products'
    message = {
        'user_id': user_id,
        'product_id': product_id
    }

    # channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')
    channel.basic_publish(exchange='',
                          routing_key='favourite_products', body=json.dumps(message))

    print(
        f"[x] Sent favorite product request for User {user_id}, Product {product_id}")

    connection.close()


# import pika

# connection_parameters = pika.ConnectionParameters('localhost')

# connection = pika.BlockingConnection(connection_parameters)

# channel = connection.channel()

# channel.queue_declare(queue='letterbox')

# message = "Hello this is my first message"

# channel.basic_publish(exchange='', routing_key='letterbox', body=message)

# print(f"sent message: {message}")

# connection.close()
