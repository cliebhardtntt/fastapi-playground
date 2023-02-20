from fastapi import FastAPI

app = FastAPI()

def fib_naive(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib_naive(number - 1) + fib_naive(number - 2)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fib")    
async def fib():
    return {"message": str(fib_naive(20))}
    