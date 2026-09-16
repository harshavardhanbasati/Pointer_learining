from fastapi import FastAPI, HTTPException 
from sqlalchemy import create_engine
from pydantic import BaseModel, Field

app = FastAPI()

users = []
class User(BaseModel):
    user: str = Field(min_length=2,max_length = 30, nullable=False)
    age: int = Field(gt =0, lt=100)
    employed: bool
    user_id: int = Field(auto_crement=True, gt = 0)

@app.post("/add_user")

def add_user(user: User):
    users.append(user)
    return {"message": "Successfully recorded", "user": user}
@app.get("/getusers")
def show_users():
    if len(users) == 0:
        raise HTTPException(
            status_code = 404,
            detail = "no data is available"
        )
    return users

@app.put("/upone/{user_id}")
def update_user(user_id: int, user: User):
    if user_id >= len(users):
        raise HTTPException(
            status_code = 404,
            detail = "User not found"
        )
    users[user_id] = user
    return {
        "message": "User updated successfully",
        "User": user   
        }

@app.get("/getuser/{user_id}")

def getone(user_id: int):
    if user_id >= len(users):
        raise HTTPException(
            status_code = 404,
            detail = "user not found"
        )
    return users[user_id]

@app.delete("/delete_user/{user_id}")

def user_del(user_id: int):
    if user_id >= len(users):
        raise HTTPException(
            status_code = 404,
            detail = "user not sound"
        )
    users.pop(user_id)
    return {
        "messsage": "User deleted successfully"   
    }