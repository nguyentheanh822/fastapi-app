from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/get_version")
def get_version():
    return {"version": "1.0.0"}

@app.get("/check_prime/{number}")
def check_prime(number: int):
    if number < 2:
        return {"prime": False}
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return {"prime": False}
    return {"prime": True}
