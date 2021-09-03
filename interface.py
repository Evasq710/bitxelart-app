from tkinter import *

class Interfaz:
    def __init__(self, ventana):
        self.window = ventana
        self.window.title('Bixelart')
        self.window.rowconfigure(0, weight = 1)
        self.window.columnconfigure(0, weight = 1)
        self.container_fondo = Frame(self.window, )
        self.container_fondo.grid(row = 0, column = 0, sticky = 'nsew')
        imagen = PhotoImage(file = "images\\fondo.png")
        fondo = Label(self.container_fondo, image=imagen)
        fondo.photo = imagen
        fondo.pack(fill=BOTH, expand=YES)