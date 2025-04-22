from sqlalchemy import Column, Integer, String,Float
from sqlalchemy.sql.sqltypes import Float as SQLAlchemyFloat
from pydantic import BaseModel

from database import  Base


class Test(Base):
    __tablename__ = "Testing"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    value = Column(String)


class ParametrosDB(Base):
    __tablename__ = "Parametros"
    id = Column(Integer, primary_key=True, index=True,nullable=False)
    nombre = Column(String, unique=False, index=True,nullable=False)
    valor_actual = Column(Float,index=True,unique=False,nullable=False)
    valor_minimo = Column(Float,index=True,unique=False,nullable=False)
    valor_maximo = Column(Float,index=True,unique=False,nullable=False)
    valor_objetivo = Column(Float,index=True,unique=False,nullable=False)


class ParametrosBase(BaseModel):
    nombre: str
    valor_actual: float
    valor_minimo: float
    valor_maximo: float
    valor_objetivo: float

class ParametrosCreate(ParametrosBase):
    pass

class Parametros(ParametrosBase):
    id: int

    class Config:
        orm_mode = True