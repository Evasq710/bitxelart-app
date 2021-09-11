from tkinter import *
from tkinter import filedialog
from clases import Token

class Interfaz:
    def __init__(self, ventana):
        self.window = ventana
        self.window.title('Bixelart')        
        self.window.state('zoomed')
        
        imagen = PhotoImage(file = "images/fondo.png")
        fondo = Label(self.window, image = imagen, bg="cornsilk")
        fondo.photo = imagen
        fondo.place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.window, text="Bixelart App", font=("Consolas", 60, "bold"), bg="cornsilk")
        title.place(x=500, y=70)

        frame_btn = Frame(self.window, bg="cornsilk")
        frame_btn.place(x=300, y=200)

        self.cargar_btn = Button(frame_btn, text="Cargar Archivo", font=("Consolas", 15), bg="light sea green", command=self.abrirArchivo)
        self.cargar_btn.grid(row=0, column=0, padx=20)

        self.analizar_btn = Button(frame_btn, text="Analizar Archivo y\ngenerar HTML", font=("Consolas", 15), bg="light sea green")
        self.analizar_btn.grid(row=0, column=1, padx=20)

        self.imagenes_btn = Button(frame_btn, text="Imagenes", font=("Consolas", 15), bg="light sea green")
        self.imagenes_btn.grid(row=0, column=2, padx=20)

        self.reportes_btn = Button(frame_btn, text="Ver Reportes HTML", font=("Consolas", 15), bg="light sea green")
        self.reportes_btn.grid(row=0, column=3, padx=20)

        self.salir_btn = Button(frame_btn, text="Salir", font=("Consolas", 15), fg="cornsilk", bg="firebrick")
        self.salir_btn.grid(row=0, column=4, padx=20)

    def abrirArchivo(self):
        global texto_doc
        Tk().withdraw()
        print('--> Se ha abierto la ventana para seleccionar el archivo')
        archivo = filedialog.askopenfile(
            title = "Seleccionar archivo PXLA",
            initialdir = "./",
            filetypes = {
                ("Archivos PXLA", "*.pxla"),
                ("Todos los archivos", "*.*")
            }
        )
        try:
            texto = archivo.read()
            archivo.close()
            print("Archivo leído con éxito")
            texto_doc = texto
        except:
            print("No se seleccionó un archivo")

texto_doc = ""
tokens = []
titulo = Token(1, "titulo")
tokens.append(titulo)
ancho = Token(2, "ancho")
tokens.append(ancho)
alto = Token(3, "alto")
tokens.append(alto)
filas = Token(4, "filas")
tokens.append(filas)
columnas = Token(5, "columnas")
tokens.append(columnas)
celdas = Token(6, "celdas")
tokens.append(celdas)
filtros = Token(7, "filtros")
tokens.append(filtros)
mirrorx = Token(8, "mirrorx")
tokens.append(mirrorx)
mirrory = Token(9, "mirrory")
tokens.append(mirrory)
doublemirror = Token(10, "doublemirror")
tokens.append(doublemirror)
igual = Token(11, "igual")
tokens.append(igual)
cadena = Token(12, "cadena")
tokens.append(cadena)
numero = Token(13, "numero")
tokens.append(numero)
abre_llave = Token(14, "abre_llave")
tokens.append(abre_llave)
celda = Token(15, "celda")
tokens.append(celda)
coma = Token(16, "coma")
tokens.append(coma)
cierra_llave = Token(17, "cierra_llave")
tokens.append(cierra_llave)
punto_coma = Token(18, "punto_coma")
tokens.append(punto_coma)
separador = Token(19, "separador")
tokens.append(separador)

if __name__ == '__main__':
    ventana = Tk()
    app = Interfaz(ventana)
    ventana.mainloop()