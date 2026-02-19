CREATE TABLE IF NOT EXISTS sensor_measurements (
id SERIAL PRIMARY KEY,
sensor_id VARCHAR(50) NOT NULL,
timestamp TIMESTAMP NOT NULL,
humidity FLOAT NOT NULL,
temperature FLOAT
);
