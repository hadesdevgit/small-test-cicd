from fastapi import FastAPI

from cicd_sample import add, minus

app = FastAPI()


@app.get("/add")
def add_route(a: int, b: int) -> dict[str, int]:
    return {"result": add(a, b)}

@app.get("/minus")
def minus_route(a: int, b: int) -> dict[str, int]:
    return {"result": minus(a, b)}
