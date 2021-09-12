from tkinter import *
from tkinter import filedialog
from clases import Token, Imagen
import os

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

tokens_leidos = []
imagenes_cargadas = []
texto_doc = ""
texto_cargado = False
name_archivo_actual = ""

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

        self.frame4 = LabelFrame(self.window,bg="white", text="Reportes")
        self.frame3 = LabelFrame(self.window,bg="white", text="Imágenes")
        self.frame2 = LabelFrame(self.window,bg="white", text="Analizar Archivo")
        self.frame1 = LabelFrame(self.window,bg="white", text="Cagar Archivo")
        self.frame_no_file = Frame(self.frame1, bg="white")
        self.frame_no_file.place(x=0, y=0, relheight=1, relwidth=1)
        load_img = PhotoImage(file="images/load.png")
        load_lb = Label(self.frame_no_file, image=load_img, bg="white")
        load_lb.photo = load_img
        load_lb.place(x=10, y=10, width=300, height=300)
        title1= Label(self.frame_no_file, text="No se ha cargado ningún archivo al programa.", font=("Consolas", 20), bg="white")
        title1.place(x=320, y=120)
        
        for frame in (self.frame1, self.frame2, self.frame3, self.frame4):
            frame.place(x=300, y=280, width=1000, height=350)

        frame_btn = Frame(self.window, bg="cornsilk")
        frame_btn.place(x=300, y=200)

        self.cargar_btn = Button(frame_btn, text="Cargar Archivo", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame1.tkraise() ,self.abrirArchivo()])
        self.cargar_btn.grid(row=0, column=0, padx=20)

        self.analizar_btn = Button(frame_btn, text="Analizar Archivo y\ngenerar HTML", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame2.tkraise()])
        self.analizar_btn.grid(row=0, column=1, padx=20)

        self.imagenes_btn = Button(frame_btn, text="Imagenes", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame3.tkraise()])
        self.imagenes_btn.grid(row=0, column=2, padx=20)

        self.reportes_btn = Button(frame_btn, text="Ver Reportes HTML", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame4.tkraise()])
        self.reportes_btn.grid(row=0, column=3, padx=20)

        self.salir_btn = Button(frame_btn, text="Salir", font=("Consolas", 15), fg="cornsilk", bg="firebrick")
        self.salir_btn.grid(row=0, column=4, padx=20)

    def abrirArchivo(self):
        global texto_doc
        global texto_cargado
        global name_archivo_actual
        name_file = filedialog.askopenfilename(
            title = "Seleccionar archivo PXLA",
            initialdir = "./",
            filetypes = {
                ("Archivos PXLA", "*.pxla"),
                ("Todos los archivos", "*.*")
            }
        )
        try:
            archivo = open(name_file)
            texto = archivo.read()
            texto_doc = texto
            texto_cargado = True
            self.frame_file = Frame(self.frame1, bg="white")
            self.frame_file.place(x=0, y=0, relheight=1, relwidth=1)
            load_img = PhotoImage(file="images/loaded.png")
            load_lb = Label(self.frame_file, image=load_img, bg="white")
            load_lb.photo = load_img
            load_lb.place(x=10, y=10, width=300, height=300)
            title1= Label(self.frame_file, text="El archivo se encuentra cargado al programa.", font=("Consolas", 20), bg="white")
            title1.place(x=320, y=110)
            name_archivo_actual = os.path.basename(name_file)
            title2= Label(self.frame_file, text=name_archivo_actual, font=("Consolas", 20), bg="white")
            title2.place(x=320, y=150)
            print("->Archivo leído con éxito")
            archivo.close()
        except Exception as e:
            print(e)
            print("->No se seleccionó un archivo")

if __name__ == '__main__':
    ventana = Tk()
    app = Interfaz(ventana)
    ventana.mainloop()