from fastapi import FastAPI

from cicd_sample import add

app = FastAPI()


@app.get("/add")
def add_route(a: int, b: int) -> dict[str, int]:
    return {"result": add(a, b)}
