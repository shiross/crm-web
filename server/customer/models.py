from sqlalchemy import Column, Integer, String, Float, Date, Text, DateTime, Time
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from ..database.models import Base
from ..database.serializable import Serializable


class Customer(Serializable, Base):
    __tablename__ = "crm-cliente"

    id = Column(Integer, primary_key=True)
    cedula = Column(String(10),nullable=False)
    nombre = Column(String(50), nullable=False)
    telefono = Column(String(15),nullable=False)
    estado = Column(Integer, nullable=False)

    def get_dict_api(self, way=None):
        dictionary = super().get_dict(way)
        empresa = {"id": dictionary["id"],
                   "name": dictionary["name"],
                   "nit": dictionary["nit"],
                   "activity": dictionary["activity"],
                   "payment": dictionary["payment"],
                   "text": dictionary["text"],
                   "coin": dictionary["coin"]
                   }
        return empresa


class Zone(Serializable,Base):
    __tablename__= "crm-zona"

    id = Column(Integer,primary_key=True)
    nombre = Column(String(100),nullable=False)
