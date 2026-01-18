# 🌱 Smart Irrigation Platform – DataOps & MLOps

## 📌 Présentation
Ce projet s’inscrit dans le cadre du *projet intégrateur du module DataOps & MLOps*
du *Master Intelligence Artificielle Embarquée (MIAE)*.

Il vise à concevoir un *système d’irrigation intelligente* basé sur une
architecture *Edge–Fog–Cloud, intégrant les bonnes pratiques **DataOps* et *MLOps*
pour la collecte, le traitement, l’orchestration et l’exploitation des données IoT.

---

## 🎯 Objectifs pédagogiques
- Mettre en œuvre un pipeline *DataOps complet*
- Orchestrer les workflows avec *Apache Airflow*
- Gérer le cycle de vie des modèles avec *MLflow*
- Traiter des données IoT en *streaming*
- Assurer la traçabilité, la qualité et le monitoring des données
- Appliquer les principes *MLOps* (entraînement, versioning, déploiement)

---

## 🏗️ Architecture Générale

### 🔹 Edge
- Capteurs IoT (Arduino, capteurs d’humidité, température)
- Envoi des données via LoRa / MQTT

### 🔹 Fog
- Raspberry Pi
- Prétraitement, filtrage et détection d’anomalies simples

### 🔹 Cloud
- Kafka pour le streaming
- Apache Airflow pour l’orchestration
- PostgreSQL / MongoDB pour le stockage
- MLflow pour la gestion des modèles
- Dashboard de visualisation

---

## 📂 Structure du projet