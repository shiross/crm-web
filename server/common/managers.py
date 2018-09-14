
class SuperManager:
    def __init__(self, entity, db):
        self.entity = entity
        self.errors = list()
        self.db = db

    def get_page(self, page_nr=0, max_entries=0, like_search=None, order_by=None, ascendant=True, query=None):
        """Lista los objetos de la base de datos de la entitad asignada en la clase hija.

        Parameters
        ----------
        page_nr : int
            Page number to display.
        max_entries : int
            max records per page.
        like_search : string, None
            Criteria de búsqueda.
        order_by : string, None
            Nombre de la columna a ordenar.
        ascendant : bool
            Criteria de sentido de orden.
        query:

        Returns
        -------
        dict
            Retorna un diccionario en donde la clave objects contiene el reultado del listado.
        """
        if not query:
            query = self.db.query(self.entity)

        if like_search and len(like_search) > 0:
            query = query.filter(self.colums_like(self.entity, like_search))

        total = query.count()
        max_pages = (total - 1) // max_entries + 1

        if page_nr < 1:
            page_nr = 1
        elif page_nr > max_pages:
            page_nr = max_pages

        if order_by and len(order_by) > 0:
            query = self.order_by(query, self.entity, order_by, ascendant)

        if total > 0:
            query = query.offset((page_nr - 1) * max_entries).limit(max_entries)

        return {"max_pages": max_pages, "objects": query}

    def colums_like(self, entity, like_search):
        """Retorna una colección de consultas "likes" de cada columna de la entidad asignada.

        Parameters
        ----------
        entity : class
            Clase entidad mapeada o modelo de sqlalchemy.
        like_search : string
            Criteria de búsqueda.

        Returns
        -------
        arguments : sqlalchemy.sql.elements.BooleanClauseList
            Tipo de dato propio de sqlalchemy, este resultado debe ser pasado como parametro
            al metodo filter.
        error
        """
        i = True
        for column in entity.__table__.columns:
            if i:
                arguments = column.like("%" + like_search + "%")
                i = False
            else:
                arguments = arguments | column.like("%" + like_search + "%")
        return arguments

    def order_by(self, query, entity, column_name, ascendant):
        """Concatena un order by a consulta dada.

        Parameters
        ----------
        query
            Consulta sqlalchemy.
        entity : class
            Clase entidad mapeada o modelo de sqlalchemy.
        column_name : string
            Nombre de la columna.
        ascendant : bool
            Sentido de orden establecido.

        Returns
        -------
        query
            Consulta sqlalchemy.
        """
        column = getattr(entity, column_name, None)
        if column is not None:
            if ascendant:
                return query.order_by(column)
            return query.order_by(column.desc())

    def obtain(self, key):
        return self.db.query(self.entity).get(key)

    def list_all(self):
        return self.db.query(self.entity)

    def many_to_many(self, object):
        if hasattr(object, 'secondary_classes'):
            for item in object.secondary_classes:
                obj_attr = getattr(object, item[0])
                keys = obj_attr[:]
                obj_attr.clear()
                for key in keys:
                    obj_attr.append(self.db.query(item[1]).
                                    get(key))
        return object

    def insert(self, object):
        object = self.many_to_many(object)
        self.db.add(object)
        self.db.commit()
        return object

    def update(self, object):
        object = self.many_to_many(object)
        self.db.merge(object)
        self.db.commit()
        return object

    def change_state(self, key, state):
        obj = self.db.query(self.entity).get(key)
        obj.enabled = state
        self.db.commit()
        return obj


class Error:
    def __init__(self, message, detail):
        self.message = message
        self.detail = detail
