from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from typing import Optional

# Create FastAPI instance
app = FastAPI()

# Define the data model using Pydantic
class UserData(BaseModel):
    name: str
    email_id: str

# File path for JSON storage
JSON_FILE_PATH = "users.json"

# Function to initialize JSON file if it doesn't exist
def init_json_file():
    if not os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'w') as f:
            json.dump([], f)

# Function to read existing data from JSON file
def read_json_file():
    try:
        with open(JSON_FILE_PATH, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Function to write data to JSON file
def write_json_file(data):
    with open(JSON_FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)

# Initialize the JSON file on startup
init_json_file()

# API endpoint to add user data
@app.post("/add_user/")
async def add_user(user: UserData):
    try:
        # Read existing data
        existing_data = read_json_file()
        
        # Create new user dictionary
        new_user = {
            "name": user.name,
            "email_id": user.email_id
        }
        
        # Append new user to existing data
        existing_data.append(new_user)
        
        # Write updated data back to file
        write_json_file(existing_data)
        
        return {
            "message": "User added successfully",
            "data": new_user
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving user data: {str(e)}")

# API endpoint to get all users (optional)
@app.get("/users/")
async def get_users():
    try:
        users = read_json_file()
        return {
            "message": "Users retrieved successfully",
            "data": users
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving users: {str(e)}")

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)