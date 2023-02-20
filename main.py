from fastapi import FastAPI

app = FastAPI()

def fib_naive(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib_naive(number - 1) + fib_naive(number - 2)
    
def fib_iter(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fib")    
async def fib():
    return {"message": str(fib_iter(2000))}

@app.get("/largefib")    
async def largefib():
    return {"message": str(fib_iter(2000000) % 10000)}
    