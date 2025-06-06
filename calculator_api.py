from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Calculator!"}

# Request model for numbers
class Numbers(BaseModel):
    num1: float
    num2: float

# Calculator operations
@app.post("/add")
def add(numbers: Numbers):
    return {"result": numbers.num1 + numbers.num2}

@app.post("/subtract")
def subtract(numbers: Numbers):
    return {"result": numbers.num1 - numbers.num2}

@app.post("/multiply")
def multiply(numbers: Numbers):
    return {"result": numbers.num1 * numbers.num2}

@app.post("/divide")
def divide(numbers: Numbers):
    if numbers.num2 == 0:
        raise HTTPException(status_code=400, detail="Zero division is not allowed")
    return {"result": round(numbers.num1 / numbers.num2, 4)}

# Run using: uvicorn calculator_api:app --reload