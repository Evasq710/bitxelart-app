from tkinter import *
from tkinter import filedialog
from token import Token

texto_doc = ""

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

if __name__ == '__main__':
    ventana = Tk()
    app = Interfaz(ventana)
    ventana.mainloop()