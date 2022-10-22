import uvicorn
from fastapi import FastAPI
from rq import Retry

from app.tasks import queue

app = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health_check")
async def root():
    return {"message": "Health ok!"}


@app.get("/test_rq")
async def root():
    def say_hello():
        print("hello world")

    queue.enqueue(say_hello, retry=Retry(max=3))
    return {"message": "Health ok!"}


if __name__ == "__main__":
    uvicorn.run(app=app)
