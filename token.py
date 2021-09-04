class Token:
    def __init__ (self, numero, id_token, nombre, lexema = None, fila = None, columna = None):
        self.numero = numero
        self.id = id_token
        self.nombre = nombre
        self.lexema = lexema
        self.fila = fila
        self.columna = columna