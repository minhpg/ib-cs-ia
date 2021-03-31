
from pydantic import BaseModel

import config

class Settings(BaseModel):
    authjwt_secret_key: str = config.SECRET



