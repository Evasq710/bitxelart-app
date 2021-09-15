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
    def __init__(self, titulo, ancho, alto, filas, columnas, matriz_celdas_texto, filtros = None):
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.matriz_celdas_texto = matriz_celdas_texto
        self.filtros = filtros
        self.matriz_celdas = []

        for y in range(self.filas):
            for x in range(self.columnas):
                self.matriz_celdas.append(self.Celda(x, y))
    
    def nuevas_celdas(self):
        encontrada = False
        celdas_no_encontradas = []
        for celda_nueva in self.matriz_celdas_texto:
            for celda in self.matriz_celdas:
                if celda_nueva.pos_x == celda.pos_x and celda_nueva.pos_y == celda.pos_y:
                    celda = celda_nueva
                    encontrada = True
                    break
            if not encontrada:
                celdas_no_encontradas.append(celda_nueva)
        return celdas_no_encontradas

    class Celda:
        def __init__(self, pos_x, pos_y, color = '#00FFFFFF', is_painted = False):
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.color = color
            self.is_painted = is_painted
        