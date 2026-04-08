import pika
import redis
import time
from flask import Flask, request

app = Flask(__name__)
redis_db = redis.Redis(host='redis', port=6379, db=0)

@app.route('/api/misc/heavy', methods=['GET'])
def get_heavy():
    name = request.args.get('name') or "test"
    
    # Check Redis Cache
    cached = redis_db.get(name)
    if cached:
        return f"(CACHE) {name}: {cached.decode()}"

    # Try to send to RabbitMQ
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='task_queue', durable=True)
        channel.basic_publish(exchange='', routing_key='task_queue', body=name)
        connection.close()
        return f"Demande pour {name} envoyée à RabbitMQ !", 202
    except Exception as e:
        return f"Erreur: RabbitMQ n'est pas encore prêt. Réessayez dans 5 secondes.", 500

if __name__ == "__main__":
    # On attend un peu que les autres services soient Up avant de lancer Flask
    time.sleep(5)
    app.run(host='0.0.0.0', port=5000)
