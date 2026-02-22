import json
import time
from kafka import KafkaConsumer
import psycopg2

# ---------- Connexion PostgreSQL ----------
def connect_db():
    while True:
        try:
            conn = psycopg2.connect(
                host="postgres",
                database="irrigation",
                user="postgres",
                password="postgres",
                port=5432
            )
            print("Connecté à PostgreSQL")
            return conn
        except Exception as e:
            print("Postgres pas prêt, retry...")
            time.sleep(5)

conn = connect_db()
cursor = conn.cursor()

# ---------- Connexion Kafka ----------
consumer = KafkaConsumer(
    "irrigation_raw_data",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
    group_id="irrigation-group"
)

print("Consumer démarré...")

# ---------- Traitement ----------
for msg in consumer:
    try:
        data = msg.value
        print("Message reçu:", data)

        sensor_id = data.get("sensor_id")
        humidity = data.get("humidity")
        temperature = data.get("temperature")

        anomaly = False

        if humidity is None or humidity < 0 or humidity > 100:
            anomaly = True

        if data.get("status") == "offline":
            anomaly = True

	if temperature > 100:
            anomaly = True

        cursor.execute(
            """
            INSERT INTO sensor_measurements
            (sensor_id, humidity, temperature, anomaly)
            VALUES (%s, %s, %s, %s)
            """,
            (sensor_id, humidity, temperature, anomaly)
        )
        conn.commit()
        print("Inséré en base")

    except Exception as e:
        print("Erreur:", e)
        conn.rollback()
