from fastapi import FastAPI

app = FastAPI()

@app.get("/counter")
def read_counter():
    return 0
