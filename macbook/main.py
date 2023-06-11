from fastapi import FastAPI, HTTPException

from macbook import macbook_db, MacBook

app = FastAPI(title="Macbook DB API", version="0.0.1")


@app.get("/")
async def root():
    return "Hello! go to /docs for using API"


@app.get("/macbook")
async def get_all_macbook():
    return macbook_db


@app.get("/macbook/{name}")
async def find_macbook_by_name(name):
    for mb in macbook_db:
        if mb.get("name") == name:
            return mb

    raise HTTPException(status_code=404, detail=f"{name} not found")


@app.post("/macbook")
async def create_new_macbook(macbook: MacBook):
    macbook_db.append(macbook.dict())
    return {"message": "MacBook created successfully"}


@app.put("/macbook/{name}")
async def update_macbook(name: str, updated_mb: MacBook):
    for mb in macbook_db:
        if mb.get("name") == name:
            mb.update(updated_mb.dict())
            return {"message": f"{name} updated successfully"}

    raise HTTPException(status_code=404, detail=f"{name} not found")


@app.delete("macbook/{name}")
async def delete_macbook(name: str):
    for idx, mb in enumerate(macbook_db):
        if mb.get("name") == name:
            macbook_db.pop(idx)
            return {"message": f"{name} deleted successfully"}

    raise HTTPException(status_code=404, detail=f"{name} not found")


if __name__ == '__main__':
    import uvicorn
    import json

    with open("config.json") as cf:
        cfg: dict = json.load(cf)

    uvicorn.run(app,
                host=cfg.get('host', "localhost"),
                port=int(cfg.get('port', '8000')))
