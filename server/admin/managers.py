from server.common.managers import SuperManager
from .models import *
from openpyxl import load_workbook, Workbook


class NotaManager(SuperManager):

    def __init__(self, db):
        super().__init__(Nota_Venta, db)

    def importar_excel(self, cname):
        try:
            wb = load_workbook(filename="server/common/resources/uploads/" + cname, read_only=True)
            print(wb.get_sheet_names())
            #self.db.commit()
            return {'message': 'Importado Todos Correctamente.', 'success': True}
        except:
            #self.db.rollback()
            return {'message': 'Algun dato esta repetido.', 'success': False}