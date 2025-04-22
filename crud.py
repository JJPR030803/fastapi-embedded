from sqlalchemy.orm import Session
import models
from models import Parametros, ParametrosDB

def get_test(db: Session):
    return db.query(models.Test).all()

def create_test(db: Session, title: str):
    new_test = models.Test(name=title)
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    return new_test

def get_test_by_id(db: Session, id: int):
    return db.query(models.Test).filter(models.Test.id == id).first()

def delete_test(db: Session, id: int):
    task = db.query(models.Test).filter(models.Test.id == id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False

def create_param(db: Session, modelo: Parametros):
    db_parametro = ParametrosDB(
        nombre=modelo.nombre,
        valor_actual=modelo.valor_actual,
        valor_minimo=modelo.valor_minimo,
        valor_maximo=modelo.valor_maximo,
        valor_objetivo=modelo.valor_objetivo
    )
    db.add(db_parametro)
    db.commit()
    db.refresh(db_parametro)
    return db_parametro

# You might also want to add these CRUD operations for parameters
def get_parametros(db: Session):
    return db.query(ParametrosDB).all()

def get_parametro_by_id(db: Session, id: int):
    return db.query(ParametrosDB).filter(ParametrosDB.id == id).first()

def update_parametro(db: Session, id: int, parametro_data: Parametros):
    db_parametro = db.query(ParametrosDB).filter(ParametrosDB.id == id).first()
    if db_parametro:
        for key, value in parametro_data.dict().items():
            setattr(db_parametro, key, value)
        db.commit()
        db.refresh(db_parametro)
        return db_parametro
    return None

def delete_parametro(db: Session, id: int):
    parametro = db.query(ParametrosDB).filter(ParametrosDB.id == id).first()
    if parametro:
        db.delete(parametro)
        db.commit()
        return True
    return False