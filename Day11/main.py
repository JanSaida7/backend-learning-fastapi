from fastapi import FastAPI

app = FastAPI()

# --- Route 1: The Homepage ---
@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}

# --- Route 2: The Dynamic Item Page ---
@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, int | str]:
    return {"item_id": item_id, "name": "The Great Widget"}