from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from database.entities import MacBookSpec
from database.models import MacBookSpecCreate

app = FastAPI(title="Macbook Spec API", version="0.0.2")


@app.get("/")
async def root():
    return "Hello! go to /docs to see how to use MacBook Spec API!"


@app.get("/macbook")
async def get_all_macbook(db: Session = Depends(get_db)):
    macbook_list = db.query(MacBookSpec).all()
    return macbook_list


@app.get("/macbook/{pname}")
async def find_macbook_by_name(pname, db: Session = Depends(get_db)):
    macbook = db.query(MacBookSpec).filter(MacBookSpec.pname == pname).first()
    if macbook is None:
        raise HTTPException(status_code=404, detail=f"{pname} not found")
    return macbook


@app.post("/macbook")
async def create_new_macbook(macbook: MacBookSpecCreate, db: Session = Depends(get_db)):
    _macbook = MacBookSpec(**macbook.dict())
    db.add(_macbook)
    db.commit()
    db.refresh(_macbook)
    return _macbook


@app.put("/macbook/{pname}")
async def update_macbook(pname, updated_mb: MacBookSpecCreate,
                         db: Session = Depends(get_db)):
    _macbook = db.query(MacBookSpec).filter(MacBookSpec.pname == pname).first()

    if _macbook is None:
        raise HTTPException(status_code=404, detail=f"{pname} not found")

    for key, val in updated_mb.dict(exclude_unset=True).items():
        setattr(_macbook, key, val)

    db.commit()
    db.refresh(_macbook)
    return _macbook


@app.delete("/macbook/{pname}")
async def delete_macbook(pname, db: Session = Depends(get_db)):
    _macbook = db.query(MacBookSpec).filter(MacBookSpec.pname == pname).first()

    if _macbook is None:
        raise HTTPException(status_code=404, detail=f"{pname} not found")

    db.delete(_macbook)
    db.commit()

    return {"message": f"{pname} deleted successfully"}


if __name__ == '__main__':
    import uvicorn
    import json

    with open("api_config.json") as cf:
        cfg: dict = json.load(cf)

    uvicorn.run(app,
                host=cfg.get('host', "localhost"),
                port=int(cfg.get('port', '8000')))
