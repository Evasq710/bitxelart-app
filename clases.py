class Token:
    def __init__ (self, id_token, nombre, leido = False, numero = None, lexema = None, fila = None, columna = None):
        self.id_token = id_token
        self.nombre = nombre
        self.leido = leido
        self.numero = numero
        self.lexema = lexema
        self.fila = fila
        self.columna = columna
    
    def is_already_read(self):
        return self.leido

    def token_leido(self):
        self.leido = True
    
    def reinicio_token(self):
        self.leido = False

class Error:
    def __init__ (self, numero, caracter, descripcion, fila, columna):
        self.numero = numero
        self.caracter = caracter
        self.descripcion = descripcion
        self.fila = fila
        self.columna = columna

class Imagen:
    def __init__(self, titulo, ancho, alto, filas, columnas, matriz_celdas, filtros = None):
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.matriz_celdas = matriz_celdas
        self.filtros = filtros

class Celda:
    def __init__(self, pos_x, pos_y, color, is_painted = False):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.is_painted = is_painted