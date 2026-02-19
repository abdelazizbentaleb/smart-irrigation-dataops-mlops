FROM python:3.11

WORKDIR /app

# Copier uniquement le fichier producer.py
COPY producer.py .

# Installer uniquement kafka-python
RUN pip install kafka-python

# Lancer le producer
CMD ["python", "producer.py"]
