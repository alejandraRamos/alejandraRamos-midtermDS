#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials("productor", "password")
connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.56.3',  5672,'/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'General'
message = ' '.join(sys.argv[2:]) or 'Hola, el programa funciona :D'
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
