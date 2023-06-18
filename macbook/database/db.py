import json
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
_cfg_path = Path(os.environ.get('PROJECT_ROOT')).joinpath("db_config.json")

with open(_cfg_path) as fp:
    _cfg: dict = json.load(fp)

_db_url = f"mysql+pymysql://" \
         f"{_cfg['user']}:{_cfg['password']}" \
         f"@{_cfg['host']}:{_cfg['port']}" \
         f"/{_cfg['database']}?charset={_cfg['charset']}"

_engine = create_engine(_db_url)
_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


def get_db():
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()
