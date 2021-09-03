import tkinter

def abrirArchivo():    
    tkinter.Tk().withdraw()
    print('--> Se ha abierto la ventana para seleccionar el archivo')
    archivo = tkinter.filedialog.askopenfile(
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