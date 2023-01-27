from dotenv import load_dotenv
from base_configuration.base_config import BaseConfig
from base_configuration import generate_config
from typing import cast


class Config(BaseConfig):
    NAME = "ZardaImage"
    API_PORT = 8000
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///database.db"


load_dotenv()

config = cast(Config, generate_config(Config))  # pylint: disable=C0103
config.API_PORT = int(config.API_PORT)
