# task-weather-api
# FastAPI Task Manager & Weather API

A robust backend REST API built with FastAPI that manages a Todo task list backed by a MySQL database and fetches live weather data using an external Weather API.

---

## 🛠️ Tech Stack & Tools Used

* **Backend Framework:** FastAPI (Python)
* **Database:** MySQL
* **ORM (Object Relational Mapper):** SQLAlchemy
* **Database Driver:** PyMySQL
* **External API Integration:** Requests (for WeatherAPI)
* **Environment Management:** python-dotenv (for protecting API keys)

---

## 📦 Prerequisites & Installation

### 1. Installed Python Packages
The following libraries are required to run this project (included in `requirements.txt`):
* `fastapi`
* `uvicorn`
* `sqlalchemy`
* `pymysql`
* `requests`
* `python-dotenv`

### 2. Environment Setup
Create a `.env` file in the root directory and add your WeatherAPI key:
```env
WEATHER_API=your_actual_weather_api_key_here

🚀 How to Run the Project
Follow these steps to get the application running locally:

Step 1: Set Up the Database
Open your MySQL Command Line Client or MySQL Workbench and create the database framework:

SQL
CREATE DATABASE IF NOT EXISTS django_db;
Step 2: Initialize Virtual Environment & Install Dependencies
Open your terminal in the project folder and run:

Bash
# Activate your virtual environment (Windows)
venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt
Step 3: Run the FastAPI Server
Start the development server using Uvicorn:

Bash
uvicorn main:app --reload
Step 4: Access Interactive API Documentation
Once the server is running, open your browser and navigate to:

Swagger UI Docs: http://127.0.0.1:8000/docs
