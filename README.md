
# 📊 Introduction to Data Engineering

This repo documents the **fundamental concepts, tools, and workflows** that power modern data infrastructure. I

---

## 🧠 About the Repository

This repository contains **5 practical assignments** from my **Data Engineering class**, focusing on real-world problem-solving and implementation.

---

## ⚙️ Setup Instructions

Before running any scripts, configure your **environment variables** in a `.env` file. This ensures your **API keys** and **database credentials** remain secure and are not hard-coded into scripts. Also, make sure to install all the required dependencies.

### 1. Create a Virtual Environment

```bash
python -m venv myenv
myenv/Scripts/activate   # For Windows
```

### 2. Add Your Credentials

Create a `.env` file in the root directory and include your credentials:

```ini
# 🌦️ OpenWeatherMap API Key
WEATHER_API_KEY=your_api_key_here

# 🗄️ PostgreSQL Database
HOST=your_postgres_host
USER=your_postgres_user
PASSWORD=your_postgres_password
DATABASE=weather_retail_db

# 🍃 MongoDB Database
MONGO_URI=mongodb://your_user:your_password@host:port
MONGO_DB=weather_retail_db
```

⚠️ **Important:** Never commit your `.env` file to GitHub. Add it to `.gitignore`.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🎯 Learning Goals

* Understand how data flows through modern systems
* Build ETL pipelines for structured & unstructured data
* Explore relational vs. non-relational databases
* Work with batch and stream processing
* Apply best practices in data modeling and pipeline design

---

## 📚 Topics Covered

* Relational vs. Non-relational Databases
* SQL for Data Manipulation
* Batch vs. Stream Processing
* Hands-on Projects with Python and Pandas
* API-based Data Ingestion into PostgreSQL & MongoDB

