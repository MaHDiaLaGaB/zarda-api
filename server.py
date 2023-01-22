import uvicorn
from fastapi import FastAPI
from api import users

description = """
    Zarda Api is small api to help people who always end up paying extra
    in road trips, sleepover, trips, restaurant, and going out with 
    other friends, it will split the invoice in the write way
    """

app = FastAPI(title="ZardaAPI",
              description=description,
              version="0.0.1",
              terms_of_service="not yet",
              contact={
                  "name": "MaHDi the Water",
                  "url": "not yet",
                  "email": "elmahdi.alagab@gmail.com",
              },
              license_info={
                  "name": "MIT License",
                  "url": "https://mit-license.org/",
              }, docs_url="/")

app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, root_path="/")
