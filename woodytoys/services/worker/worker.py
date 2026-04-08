import pika
import redis
import woody
import time

# 1. Connexion à Redis (pour stocker le résultat final)
redis_db = redis.Redis(host='redis', port=6379, db=0)

# 2. Connexion à RabbitMQ (on attend qu'il soit prêt)
print(" [*] Connexion à RabbitMQ...")
while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        break
    except:
        time.sleep(2)

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    name = body.decode()
    print(f" [x] Je commence le calcul lourd pour : {name}")
    
    # On simule le travail lent
    result = woody.make_some_heavy_computation(name)
    
    # On enregistre le résultat dans Redis
    redis_db.setex(name, 60, result)
    
    print(f" [x] Travail fini pour {name} !")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print(' [*] En attente de messages...')
channel.start_consuming()
