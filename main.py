from tkinter import *
from tkinter import filedialog
import interface

def abrirArchivo():    
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
        return texto
    except:
        return None

if __name__ == '__main__':
    ventana = Tk()
    app = interface.Interfaz(ventana)
    ventana.mainloop()