import uvicorn
from fastapi import FastAPI
from api import users
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

description = """
    Zarda Api is small api to help people who always end up paying extra
    in road trips, sleepover, trips, restaurant, and going out with 
    other friends, it will split the invoice in the write way
    """

app = FastAPI()

app.include_router(users.router)


@app.get("/", response_class=RedirectResponse)
async def redirect_fastapi() -> str:
    return "/docs"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
