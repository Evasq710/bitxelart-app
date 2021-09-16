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
        self.matriz_celdas_mirrorx = []
        self.matriz_celdas_mirrory = []
        self.matriz_celdas_double = []

        for y in range(self.filas):
            for x in range(self.columnas):
                self.matriz_celdas.append(self.Celda(x, y))
                
        for y in range(self.filas):
            for x in range(self.columnas):
                self.matriz_celdas_mirrorx.append(self.Celda(self.columnas - 1 - x, y))
        
        for y in range(self.filas):
            for x in range(self.columnas):
                self.matriz_celdas_mirrory.append(self.Celda(x, self.filas - 1 - y))
        
        for y in range(self.filas):
            for x in range(self.columnas):
                self.matriz_celdas_double.append(self.Celda(self.columnas - 1 - x, self.filas - 1 - y))
    
    def nuevas_celdas(self):
        encontrada = False
        celdas_no_encontradas = []
        for celda_nueva in self.matriz_celdas_texto:
            if celda_nueva.is_painted:
                for celda in self.matriz_celdas:
                    if celda_nueva.pos_x == celda.pos_x and celda_nueva.pos_y == celda.pos_y:
                        celda.paint_cell()
                        celda.set_color(celda_nueva.color)
                        encontrada = True
                        break
                for celda in self.matriz_celdas_mirrorx:
                    if celda_nueva.pos_x == celda.pos_x and celda_nueva.pos_y == celda.pos_y:
                        celda.paint_cell()
                        celda.set_color(celda_nueva.color)
                        break
                for celda in self.matriz_celdas_mirrory:
                    if celda_nueva.pos_x == celda.pos_x and celda_nueva.pos_y == celda.pos_y:
                        celda.paint_cell()
                        celda.set_color(celda_nueva.color)
                        break
                for celda in self.matriz_celdas_double:
                    if celda_nueva.pos_x == celda.pos_x and celda_nueva.pos_y == celda.pos_y:
                        celda.paint_cell()
                        celda.set_color(celda_nueva.color)
                        break
                if not encontrada:
                    celdas_no_encontradas.append(celda_nueva)
        return celdas_no_encontradas

    class Celda:
        def __init__(self, pos_x, pos_y, color = '#FFFFFF00', is_painted = False):
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.color = color
            self.is_painted = is_painted
        
        def paint_cell(self):
            self.is_painted = True
        
        def set_color(self, color):
            self.color = color