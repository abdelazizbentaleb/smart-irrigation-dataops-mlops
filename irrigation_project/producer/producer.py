import json
import time
from kafka import KafkaProducer
import random
import os
from datetime import datetime
time.sleep(15)  # attendre que Kafka démarre
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
TOPIC = "irrigation_raw_data"

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "sensor_id": f"sensor_{random.randint(1,3)}",
        "timestamp": datetime.now().isoformat(),
        "humidity": random.uniform(0, 110),  # Certaines valeurs aberrantes
        "temperature": random.uniform(15, 35)
    }
    producer.send(TOPIC, value=data)
    print(f"[SEND] {data}")
    time.sleep(2)
