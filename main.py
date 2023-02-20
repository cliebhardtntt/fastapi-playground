from fastapi import FastAPI
import numpy as np

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
    
def fib_numpy(n):
    F = np.matrix([[1, 1], [1, 0]])
    return (F ** (n - 1))[0, 0]
    
def slow_numpy(n):
    a = np.zeros(n)
    a[n // 2] = 1
    b = np.zeros(n)
    b[n // 2] = 1
    r = np.convolve(a, b)
    return r[0]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fib")    
async def fib():
    return {"message": str(fib_numpy(2000))}

@app.get("/largefib")    
async def largefib():
    return {"message": str(fib_numpy(20000000000000000000000000) % 10000)}

@app.get("/slow")    
async def slow():
    slow_numpy(100000)
    return {"message": "done"}
    