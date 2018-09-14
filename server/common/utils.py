def decorators(*decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f
    return deco

from datetime import datetime
def str_date(str_date):
    datetime