import uvicorn
from fastapi import FastAPI
from api import users

description = """
    Zarda Api is small api to help people who always end up paying extra
    in road trips, sleepover, trips, restaurant, and going out with 
    other friends, it will split the invoice in the write way
    """

app = FastAPI(docs_url="/")

app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
