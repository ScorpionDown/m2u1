from fastapi import FastAPI

app = FastAPI()

"/"
@app.get("/")
def index():
    return "Hello FastAPI!"

# uvicorn simple_program:app --reload