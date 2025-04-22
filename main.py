from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, crud
from database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.put("/param")
def create_param(param: models.ParametrosCreate, db: Session = Depends(get_db)):
    return crud.create_param(db, param)

@app.get("/param", response_model=List[models.Parametros])
def read_parametros(db: Session = Depends(get_db)):
    return crud.get_parametros(db)

@app.get("/param/{param_id}", response_model=models.Parametros)
def read_parametro(param_id: int, db: Session = Depends(get_db)):
    parametro = crud.get_parametro_by_id(db, param_id)
    if not parametro:
        raise HTTPException(status_code=404, detail="Parameter not found")
    return parametro

@app.put("/param/{param_id}", response_model=models.Parametros)
def update_parametro(param_id: int, param: models.ParametrosCreate, db: Session = Depends(get_db)):
    parametro = crud.update_parametro(db, param_id, param)
    if not parametro:
        raise HTTPException(status_code=404, detail="Parameter not found")
    return parametro

@app.delete("/param/{param_id}")
def delete_parametro(param_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_parametro(db, param_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Parameter not found")
    return {"message": "Parameter deleted"}

@app.get("/")
def read_root():
    return {"message": "FastAPI + SQLite!"}

@app.get("/test")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_test(db)

@app.post("/test")
def create_test(title: str, db: Session = Depends(get_db)):
    return crud.create_test(db, title=title)

@app.get("/tests/{test_id}")
def read_task(test_id: int, db: Session = Depends(get_db)):
    task = crud.get_test_by_id(db, test_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/test/{test_id}")
def delete_task(test_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_test(db, test_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}