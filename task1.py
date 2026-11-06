from fastapi import FastAPI, HTTPException
import json
from pathlib import Path

app = FastAPI(title="User Management Demo")

DATA_FILE = Path(__file__).parent / "users.json"


def load_users():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except json.JSONDecodeError:
        return []


def save_users():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)


users = load_users()


def find_user(login):
    for user in users:
        if user.get("login") == login:
            return user
    return None

@app.get("/")
def home():
    return {"message": "Система для керування користувачами"}


@app.get("/user/get-all")
def get_all_users():

    return {"users": load_users()}
# uvicorn task1:app --reload

@app.post("/user/add")
def add_user(user: dict):
    login = user.get("login")

    if not login:
        raise HTTPException(status_code=400, detail="Поле login є обов'язковим")

    if find_user(login):
        raise HTTPException(status_code=400, detail="Користувач вже існує")

    users.append(user)
    save_users()

    return {"message": "Користувача додано", "user": user}