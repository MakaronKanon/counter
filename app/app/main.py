from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/counter")
def read_counter():
    # Todo: get counter.
    return 0

@app.put("/counter")
def update_counter(counter: int = Body(..., embed=True)):
    # Todo: set counter.
    return counter

