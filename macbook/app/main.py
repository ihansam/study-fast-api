from fastapi import FastAPI

from app import __version__
from app.routes import macbook_router

app = FastAPI(title="Macbook Spec API", version=__version__)
app.include_router(macbook_router)


if __name__ == '__main__':
    import json
    import os
    from pathlib import Path

    from dotenv import load_dotenv
    import uvicorn

    load_dotenv()
    _cfg_path = Path(os.environ.get('PROJECT_ROOT')).joinpath("api_config.json")

    with open(_cfg_path) as fp:
        cfg: dict = json.load(fp)

    uvicorn.run(app,
                host=cfg.get('host', "localhost"),
                port=int(cfg.get('port', '8000')))
