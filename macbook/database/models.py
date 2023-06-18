from pydantic import BaseModel


class MacBookSpecCreate(BaseModel):
    pname: str
    processor: str
    display: float
    unpack: int


class MacBookSpecResponse(BaseModel):
    pname: str
    processor: str
    display: float
    unpack: int
