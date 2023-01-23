from fastapi import FastAPI
from db.session import Base, engine
from routes.test import router as test_router

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(test_router)

@app.get("/") # Route Path
def index():
    return {
        "Python" : "framework"
    }
