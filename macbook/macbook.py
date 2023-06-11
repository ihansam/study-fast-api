from pydantic import BaseModel


class MacBook(BaseModel):
    name: str
    core_version: str
    display_size: float
    release_year: int


intel_air_13 = MacBook(name="MacBook Air (Intel, 2020)",
                       core_version="Intel Core ix-10xx",
                       display_size=13,
                       release_year=2023)

macbook_db: list[dict] = [intel_air_13.dict()]
