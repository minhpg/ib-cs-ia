
from pydantic import BaseModel

import app.config as config

class Settings(BaseModel):
    authjwt_secret_key: str = config.SECRET



