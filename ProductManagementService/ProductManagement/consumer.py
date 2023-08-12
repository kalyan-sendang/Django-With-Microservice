import pika
import json
import sys
import os
import django
print(sys.path)
# Append the path to the project directory to the system path
project_path = "C:/Users/kalya/OneDrive/Desktop/microservices-project-django/ProductManagementService"
sys.path.append(project_path)
# Set the DJANGO_SETTINGS_MODULE to the correct settings file
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "ProductManagementService.settings")
django.setup()

# import the model
from ProductManagement.models import Favourite

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue before consuming

channel.queue_declare("favourite_products", durable=True)


def callback(ch, method, properties, body):
    print('This is Favourites...')
    print(body)
    data = json.loads(body)
    print(data)
    user_id = data['user_id']
    product_id = data['product_id']

    Favourite.objects.create(user_id=user_id, product_id=product_id)


# Start consuming messages
channel.basic_consume(
    queue="favourite_products", on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()


# import pika


# def on_message_received(ch, method, properties, body):
#     print(f"received new message: {body}")


# connection_parameters = pika.ConnectionParameters('localhost')

# connection = pika.BlockingConnection(connection_parameters)

# channel = connection.channel()

# channel.queue_declare(queue='letterbox')

# channel.basic_consume(queue='letterbox', auto_ack=True,
#                       on_message_callback=on_message_received)

# print("Starting Consuming")

# channel.start_consuming()
