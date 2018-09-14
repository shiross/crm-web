from sqlalchemy import Column, Integer, String, Float, Date, Text
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship

from ..database.models import Base
from ..database.serializable import Serializable


class Marca(Serializable, Base):
    __tablename__ = 'cns_marca'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Unidad(Serializable, Base):
    __tablename__ = 'cns_unidad_medida'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)


class Cliente(Serializable, Base):
    __tablename__ = 'cns_cliente'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Vendedor(Serializable, Base):
    __tablename__ = 'cns_vendedor'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Estado(Serializable, Base):
    __tablename__ = 'cns_estado'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Tipo(Serializable, Base):
    __tablename__ = 'cns_tipo'
    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)


class Estado_Tipo(Serializable, Base):
    way = {'estado': {}, 'tipo': {}}
    __tablename__ = 'cns_estado_tipo'
    id = Column(Integer, primary_key=True)
    fk_estado = Column(Integer, ForeignKey('cns_estado.id'))
    fk_tipo = Column(Integer, ForeignKey('cns_tipo.id'))

    estado = relationship('Estado')
    tipo = relationship('Tipo')


class Producto(Serializable, Base):
    way = {'marca': {}, 'unidad': {}}
    __tablename__ = 'cns_producto'
    id = Column(Integer, primary_key=True)
    fk_marca = Column(Integer, ForeignKey('cns_marca.id'), nullable=False)
    fk_unidad = Column(Integer, ForeignKey('cns_unidad_medida.id'), nullable=False)

    marca = relationship('Marca')
    unidad = relationship('Unidad')


class Nota_Venta(Serializable, Base):
    way = {
        'cliente': {},
        'vendedor': {},
        'estado_tipo': {
            'estado': {},
            'tipo': {}
        },
        'detalle': [],
    }
    __tablename__ = 'cns_nota_venta'
    id = Column(Integer, primary_key=True)
    fk_cliente = Column(Integer, ForeignKey('cns_cliente.id'), nullable=False)
    fk_vendedor = Column(Integer, ForeignKey('cns_vendedor.id'), nullable=False)
    fk_estado_tipo = Column(Integer, ForeignKey('cns_estado_tipo.id'), nullable=False)
    nro_orden = Column(String(10), nullable=False, unique=True)
    nro_proforma = Column(String(10), nullable=False, unique=True)
    fecha_compra = Column(Date, nullable=True)
    fecha_alta = Column(Date, nullable=True)
    fecha_pedido = Column(Date, nullable=True)

    cliente = relationship('Cliente')
    vendedor = relationship('Vendedor')
    estado_tipo = relationship('Estado_Tipo')
    detalle = relationship('Detalle')


class Detalle(Serializable, Base):
    way = {
        'producto': {},
        'nota': {}
    }
    __tablename__ = 'cns_detalle'
    id = Column(Integer, primary_key=True)
    fk_nota = Column(Integer, ForeignKey('cns_nota_venta.id'), nullable=False)
    fk_producto = Column(Integer, ForeignKey('cns_producto.id'), nullable=False)
    fecha_comprometida = Column(Date, nullable=True)
    fecha_llegada = Column(Date, nullable=True)
    cantidad = Column(Float, nullable=True)
    details = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

    nota = relationship('Nota_Venta')
    producto = relationship('Producto')
