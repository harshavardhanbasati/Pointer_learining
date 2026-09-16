from fastapi import FastAPI, HTTPException, Header, Depends
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "NulearCode"

ALOGIRITHM = "HS256"

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update(
        {
            "exp":expire
        }
    )
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALOGIRITHM)

    return token

@app.post("/login")

def login(username: str, password: str):
    if username != "admin" or password!="1234":
        raise HTTPException(
            status_code=404,
            detail="Invalid passsword or username!"
        )
    token = create_token({
        "sub":username
    })
    return{
        "access_token":token
    }
def verify_token(token: str = Header(None)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALOGIRITHM)
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
@app.get("/secure")

def secure_user(user = Depends(verify_token)):
    return{
        "message":"Secure Data Accessed",
        "user":user
    }

    