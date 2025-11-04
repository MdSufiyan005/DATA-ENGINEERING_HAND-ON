# Introduction to Data Engineering

## About

This repository contains 5 practical assignments from my Data Engineering class, focusing on real-world implementation.

---

## Setup

### 1. Create Virtual Environment
```bash
python -m venv myenv
myenv/Scripts/activate   # Windows
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:
```ini
# OpenWeatherMap API
WEATHER_API_KEY=your_api_key_here

# PostgreSQL
HOST=your_postgres_host
USER=your_postgres_user
PASSWORD=your_postgres_password
DATABASE=weather_retail_db

# MongoDB
MONGO_URI=mongodb://your_user:your_password@host:port
MONGO_DB=weather_retail_db
```

**Note:** Add `.env` to `.gitignore` before committing.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Learning Goals

- Understand data flow through modern systems
- Build ETL pipelines for structured and unstructured data
- Explore relational vs. non-relational databases
- Work with batch and stream processing
- Apply data modeling and pipeline design best practices

---

## Topics Covered

- Relational vs. Non-relational Databases
- SQL for Data Manipulation
- Batch vs. Stream Processing
- Python and Pandas Projects
- API-based Data Ingestion (PostgreSQL & MongoDB)

