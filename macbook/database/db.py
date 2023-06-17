import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

with open("../db_config.json") as cf:
    cfg: dict = json.load(cf)


_DB_URL = f"mysql+pymysql://" \
         f"{cfg['user']}:{cfg['password']}" \
         f"@{cfg['host']}:{cfg['port']}" \
         f"/{cfg['database']}?charset={cfg['charset']}"

_engine = create_engine(_DB_URL)
_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


def get_db():
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()
