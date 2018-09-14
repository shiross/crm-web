import json

from sqlalchemy.inspection import inspect


class Serializable:
    """Clase que serializa objetos de sqlalchemy."""

    way = {}

    def __init__(self, **properties):
        """Crea un objeto de sqlalchemy apartir de un diccionario.

        Parameters
        ----------
        properties : dict

        Returns
        -------
        objeto
            Retornará un objeto instanciado de la clase que lo heredó.
        """
        types = self.get_type_relationships()
        for property in properties:
            value = properties[property]
            if isinstance(value, list):
                attr = getattr(self, property, None)
                attr_type = types.get(property, None)
                if attr is not None and attr_type is not None:
                    for item in value:
                        attr.append(types.get(property)(**item))
                else:
                    setattr(self, property, value)
            else:
                if isinstance(value, dict):
                    attr_type = types.get(property, None)
                    if attr_type is not None:
                        setattr(self, property, attr_type(**value))
                else:
                    setattr(self, property, value)

    def get_type_relationships(self):
        """Retorna un diccionario con los nombres y tipos de los objetos relacionados."""
        self.secondary_classes = list()
        aux = dict()
        for item in inspect(type(self)).relationships:
            if item.secondary is not None:
                self.secondary_classes.append((str(item).split('.')[1], item.mapper.class_))
            else:
                aux[str(item).split('.')[1]] = item.mapper.class_
        return aux

    def get_type_attribute(self, name):
        return inspect(type(self)).columns._data[name].type

    def get_dict(self, way=None):
        """Retorna un diccionario que represenata los atributos y relaciones del objeto.

        Parameters
        ----------
        way : dict
            Este diccionario definirá que relaciones y subrelaciones serán mapeadas o tomadas en cuenta.
        """
        if way is None:
            way = self.way
        result = dict()
        for colum in self.__table__.columns:
            attr = getattr(self, colum.name)
            if not isinstance(attr, (str, int, float, bool)):
                result[colum.name] = str(attr)
            else:
                result[colum.name] = attr

        for key in way:
            attr = getattr(self, key)
            if attr is not None:
                if not isinstance(attr, list):
                    result[key] = attr.get_dict(way[key])
                else:
                    result[key] = [item.get_dict(way[key]) for item in attr]
        return result


    def get_json(self, way=None):
        """Retorna un string que representa el diccionario del objeto."""
        return json.dumps(self.get_dict())
