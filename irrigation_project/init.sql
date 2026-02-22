CREATE TABLE IF NOT EXISTS sensor_measurements (
    id SERIAL PRIMARY KEY,
    sensor_id TEXT,
    humidity FLOAT,
    temperature FLOAT,
    anomaly BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
