from fastapi import FastAPI
from database import engine,SessionLocal
from models import Task,Base,User
import requests
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

# To create our database and structure
Base.metadata.create_all(bind = engine)

@app.get('/')
def home():
    return "Api is running"

@app.get('/get-tasks')
def home():
    try:
        db = SessionLocal()
        tasks = db.query(Task).all()
        return tasks
    except Exception as e:
        return {"error":str(e)}
    finally:
        db.close()

@app.get('/users')
def get_users():
    try:
        db = SessionLocal()
        print("connection established")
        users = db.query(User).all()
        return users
    except Exception as e:
        return {"error":str(e)}
    finally:
        db.close()
# {"title":"value"}

@app.post('/get-weather/{city}')
def get_weather(city:str):
    try:
        response= requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHER_API')}&q={city}")
        data = response.json()
        return data['current']['temp_c']
    except Exception as e:
        return {"error":str(e)}
    
@app.post('/add-task')
def add_task(data:dict):
    task_title = data['title']
    try:
        db = SessionLocal()
        task = Task(title=task_title)
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    except Exception as e:
        return {"Error":str(e)}
    finally:
        db.close()

@app.delete('/delete/{task_id}')
def delete_task(task_id:int):
    db = SessionLocal()
    record = db.query(Task).filter(Task.task_id == task_id).first()
    if not record:
        return f"No task found with the ID {task_id}"
    db.delete(record)
    db.commit()
    db.close()
    return "Task deleted succesfully"

# {"title":"New value","status":True}
@app.put('/update-task/{task_id}')
def update_task(task_id:int, data:dict):
    db = None
    try:
        new_task_title = data['title']
        new_task_status = data['staus']
        db = SessionLocal()
        record = db.query(Task).filter(Task.task_id == task_id).first()
        if not record:
            return f"Task not found with ID {task_id}"
        record.title = new_task_title
        record.staus = new_task_status
        db.commit()
        db.refresh(record)
        return record
    except Exception as e:
        return str(e)
    finally:
        if db is not None:
            db.close()

