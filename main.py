from fastapi import FastAPI
import numpy as np
import multiprocessing
import threading

app = FastAPI()
    
def fib_iter(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
    
def slow_numpy(n):
    a = np.zeros(n)
    a[n // 2] = 1
    b = np.zeros(n)
    b[n // 2] = 1
    r = np.convolve(a, b)
    return r[0]

@app.get("/")
def root():
    #print("root PID " + str(multiprocessing.Process.pid))
    print("root TID " + str(threading.get_ident()))
    print("root: Before res")
    res = "Hello World"
    print("root: After res")
    return {"message": res}

@app.get("/largefib")    
def largefib():
    print("largefib TID " + str(threading.get_ident()))
    print("largefib" + str(multiprocessing.Process.pid))
    print("largefib: Before res")
    res = str(fib_iter(20000000000000) % 10000)
    print("largefib: After res")
    return {"message": res}

@app.get("/slow")    
def slow():
    slow_numpy(100000)
    return {"message": "done"}
    