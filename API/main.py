from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Contexa!"}

@app.get("/health")
def read_health():
    return {"message": "OK"}

@app.post("/search")
def search(query: str):
    return {"message": f"Searching for {query}"}