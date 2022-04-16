#!/usr/bin/env python
import json, pika, sys, os

if __name__ == '__main__':

    if os.getenv('APP_RABBITMQ_USER') and os.getenv('APP_RABBITMQ_PASS'):
        credentials = pika.PlainCredentials(
            os.getenv('APP_RABBITMQ_USER'),
            os.getenv('APP_RABBITMQ_PASS')
        )
    else:
        credentials = null

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            os.getenv('APP_RABBITMQ_HOST') or 'localhost',
            os.getenv('APP_RABBITMQ_PORT') or 5672,
            os.getenv('APP_RABBITMQ_VHOST') or '/',
            credentials
        )
    )

    channel = connection.channel()

    queue = os.getenv('APP_RABBITMQ_QUEUE')
    channel.queue_declare(
        queue=queue,
        passive=False,
        durable=True,
        exclusive=False,
        auto_delete=False
    )

    exchange = os.getenv('APP_RABBITMQ_EXCHANGE') or 'router'
    channel.exchange_declare(
        exchange=exchange,
        exchange_type='direct',
        passive=False,
        durable=True,
        auto_delete=False
    )

    channel.queue_bind(
        queue=queue,
        exchange=exchange
    )

    message = {
        'to': input('Para:    '),
        'subject': input('Assunto: '),
        'body': input('Corpo:   ')
    }
    channel.basic_publish(
        exchange=exchange,
        routing_key=queue,
        body=json.dumps(message)
    )
    print("\nMensagem enviada: %s" % message)
