class Token:
    def __init__ (self, id_token, nombre, numero = None, lexema = None, fila = None, columna = None):
        self.id_token = id_token
        self.nombre = nombre
        self.numero = numero
        self.lexema = lexema
        self.fila = fila
        self.columna = columna