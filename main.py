from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from clases import Token, Imagen, Error
import os
import traceback
import imgkit
import webbrowser

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
errores_encontrados = []
texto_doc = ""
texto_cargado = False
name_archivo_actual = ""

class Interfaz:
    def __init__(self, ventana):
        self.window = ventana
        self.window.title('Bitxelart')        
        self.window.state('zoomed')
        
        imagen = PhotoImage(file = "images/fondo.png")
        fondo = Label(self.window, image = imagen, bg="white")
        fondo.photo = imagen
        fondo.place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.window, text="Bitxelart App", font=("Consolas", 60, "bold"), bg="white")
        title.place(x=500, y=70)

        self.frame4 = LabelFrame(self.window,bg="white", text="Reportes")
        self.frame4_no_file = Frame(self.frame4, bg="white")
        self.frame4_no_file.place(x=0, y=0, relheight=1, relwidth=1)
        load_img4 = PhotoImage(file="images/question3.png")
        load_lb4 = Label(self.frame4_no_file, image=load_img4, bg="white")
        load_lb4.photo = load_img4
        load_lb4.place(x=10, y=40, width=300, height=300)
        title1= Label(self.frame4_no_file, text="No se ha cargado ningún archivo al programa.", font=("Consolas", 20), bg="white")
        title1.place(x=320, y=150)

        self.frame3 = LabelFrame(self.window,bg="white", text="Imágenes")
        self.frame3_no_file = Frame(self.frame3, bg="white")
        self.frame3_no_file.place(x=0, y=0, relheight=1, relwidth=1)
        load_img3 = PhotoImage(file="images/question2.png")
        load_lb3 = Label(self.frame3_no_file, image=load_img3, bg="white")
        load_lb3.photo = load_img3
        load_lb3.place(x=10, y=40, width=300, height=300)
        title1= Label(self.frame3_no_file, text="No se ha cargado ningún archivo al programa.", font=("Consolas", 20), bg="white")
        title1.place(x=320, y=150)

        self.frame2 = LabelFrame(self.window,bg="white", text="Analizar Archivo")
        self.frame2_no_file = Frame(self.frame2, bg="white")
        self.frame2_no_file.place(x=0, y=0, relheight=1, relwidth=1)
        load_img2 = PhotoImage(file="images/question1.png")
        load_lb2 = Label(self.frame2_no_file, image=load_img2, bg="white")
        load_lb2.photo = load_img2
        load_lb2.place(x=10, y=40, width=300, height=300)
        title1= Label(self.frame2_no_file, text="No se ha cargado ningún archivo al programa.", font=("Consolas", 20), bg="white")
        title1.place(x=320, y=150)

        self.frame1 = LabelFrame(self.window,bg="white", text="Cagar Archivo")
        self.frame1_no_file = Frame(self.frame1, bg="white")
        self.frame1_no_file.place(x=0, y=0, relheight=1, relwidth=1)
        load_img1 = PhotoImage(file="images/load.png")
        load_lb = Label(self.frame1_no_file, image=load_img1, bg="white")
        load_lb.photo = load_img1
        load_lb.place(x=10, y=40, width=300, height=300)
        title1= Label(self.frame1_no_file, text="No se ha cargado ningún archivo al programa.", font=("Consolas", 20), bg="white")
        title1.place(x=320, y=150)
        
        for frame in (self.frame1, self.frame2, self.frame3, self.frame4):
            frame.place(x=250, y=280, width=1050, height=480)

        frame_btn = Frame(self.window, bg="white")
        frame_btn.place(x=300, y=200)

        self.cargar_btn = Button(frame_btn, text="Cargar Archivo", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame1.tkraise(), self.abrirArchivo()])
        self.cargar_btn.grid(row=0, column=0, padx=20)

        self.analizar_btn = Button(frame_btn, text="Analizar Archivo y\ngenerar HTML", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame2.tkraise(), self.imagenes_html()])
        self.analizar_btn.grid(row=0, column=1, padx=20)

        self.imagenes_btn = Button(frame_btn, text="Imagenes", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame3.tkraise(), self.imagenes_programa()])
        self.imagenes_btn.grid(row=0, column=2, padx=20)

        self.reportes_btn = Button(frame_btn, text="Ver Reportes HTML", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame4.tkraise(), self.reportes_html()])
        self.reportes_btn.grid(row=0, column=3, padx=20)

        self.salir_btn = Button(frame_btn, text="Salir", font=("Consolas", 15), fg="cornsilk", bg="firebrick", command=ventana.destroy)
        self.salir_btn.grid(row=0, column=4, padx=20)

    def abrirArchivo(self):
        global texto_doc
        global texto_cargado
        global name_archivo_actual
        global tokens_leidos
        global imagenes_cargadas
        global errores_encontrados
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
            texto = ""
            texto = archivo.read()
            texto += "$"
            texto_doc = ""
            texto_doc = texto
            texto_cargado = True

            self.frame_file = Frame(self.frame1, bg="white")
            self.frame_file.place(x=0, y=0, relheight=1, relwidth=1)
            load_img1 = PhotoImage(file="images/loaded.png")
            load_lb = Label(self.frame_file, image=load_img1, bg="white")
            load_lb.photo = load_img1
            load_lb.place(x=10, y=40, width=300, height=300)
            title1= Label(self.frame_file, text="El archivo se encuentra cargado al programa.", font=("Consolas", 20), bg="white")
            title1.place(x=320, y=110)
            name_archivo_actual = os.path.basename(name_file)
            title2= Label(self.frame_file, text=name_archivo_actual, font=("Consolas", 20), bg="white")
            title2.place(x=320, y=150)
            print("->Archivo leído con éxito")

            try:
                title3= Label(self.frame_file, text="Analizando el archivo...", font=("Consolas", 20), bg="white")
                title3.place(x=320, y=190)
                tokens_leidos = []
                imagenes_cargadas = []
                errores_encontrados = []
                self.analizar_archivo()
                if len(imagenes_cargadas) > 0:
                    title3= Label(self.frame_file, text="Archivo analizado exitosamente.", font=("Consolas", 20), bg="white")
                    title3.place(x=320, y=190)
                else:
                    texto_cargado = False
                    title3= Label(self.frame_file, text="No se detectaron imágenes. Ver Errores.", font=("Consolas", 20), bg="white")
                    title3.place(x=320, y=190)
                print("->Análisis finalizado con éxito")
            except Exception:
                traceback.print_exc()
                title3= Label(self.frame_file, text="Ocurrió un error en el analizador léxico :(", font=("Consolas", 20), bg="white")
                title3.place(x=320, y=190)
                print("-> Ocurrió un error en el analizador léxico.")
            archivo.close()
            
        except Exception:
            traceback.print_exc()
            print("->No se seleccionó un archivo")
    
    def is_ascii(self, caracter):
        if ord(caracter) == 32 or ord(caracter) == 33 or (ord(caracter) >= 35 and ord(caracter) <= 154) or ord(caracter) == 130 or (ord(caracter) >= 160 and ord(caracter) <= 253):
            return True
        return False

    def is_number(self, caracter):
        if ord(caracter) >= 48 and ord(caracter) <= 57:
            return True
        return False
    
    def is_hexadecimal_letter(self, caracter):
        if (ord(caracter) >= 65 and ord(caracter) <= 70) or (ord(caracter) >= 97 and ord(caracter) <= 102):
            return True
        return False

    def analizar_archivo(self):
        global texto_doc
        global texto_cargado
        global tokens
        global tokens_leidos
        global imagenes_cargadas
        global errores_encontrados
        if texto_cargado:
            fila = 1
            columna = 0
            new_token = 0
            new_error = 0
            sections = 0
            estado_file = "a0"
            estado_img = "b0"
            estado_sec = "c0"
            lexema_actual = ""
            act_ancho = False
            act_alto = False
            act_filas = False
            act_columnas = False
            titulo_guardado = False
            titulo_aux = ''
            ancho_guardado = False
            ancho_aux = 0
            alto_guardado = False
            alto_aux = 0
            filas_guardado = False
            filas_aux = 0
            columnas_guardado = False
            columnas_aux = 0
            celdas_guardado = False
            posx_aux = ''
            posy_aux = ''
            boolean_aux = None
            color_aux =''
            celda_aux = None
            celdas_aux = []
            filtros_guardado = False
            imagen_aux = None
            filtros_aux = []
            imagen_sin_guardar = False
            for caracter in texto_doc:
                # Control Filas - columnas
                if ord(caracter) == 9: # tab
                    columna += 4
                elif ord(caracter) == 10: # salto de linea
                    columna = 0
                    fila += 1
                elif ord(caracter) == 32: # espacio
                    columna += 1
                else: # otro caracter
                    columna +=1
                # Estados
                if estado_file == "a0" or estado_file == "a5":
                    imagen_sin_guardar = True
                    if estado_img == "b0" and sections < 7:
                        if estado_sec == "c0":
                            if caracter == "T":
                                for tkn in tokens:
                                    if tkn.id_token == 1:
                                        if tkn.is_already_read():
                                            new_error += 1
                                            e_read = Error(new_error, caracter, "'T' en inicio de sección. El token 'TITULO' ha sido leído previamente.", fila, columna-(len(lexema_actual)-1))
                                            errores_encontrados.append(e_read)
                                        else:
                                            lexema_actual += caracter
                                            estado_sec = "c1"
                                        break
                            elif caracter == "A":
                                lexema_actual += caracter
                                estado_sec = "c11"
                            elif caracter == "F":
                                lexema_actual += caracter
                                estado_sec = "c21"
                            elif caracter == "C":
                                lexema_actual += caracter
                                estado_sec = "c51"
                            elif caracter == "@":
                                for tkn in tokens:
                                    tkn.reinicio_token()
                                if sections == 6 and titulo_guardado and ancho_guardado and alto_guardado and filas_guardado and columnas_guardado and celdas_guardado:
                                    imagen_aux = Imagen(titulo_aux, ancho_aux, alto_aux, filas_aux, columnas_aux, celdas_aux)
                                    celdas_no_encontradas = imagen_aux.nuevas_celdas()
                                    for celda in celdas_no_encontradas:
                                        new_error += 1
                                        e_celda = Error(new_error, 'Celda: (' + str(celda.pos_x) + ', ' + str(celda.pos_y) + ')', "No se encontró la celda. Posición máxima: (" + str(columnas_aux - 1) + ", " + str(filas_aux - 1) + ")", '-', '-')
                                        errores_encontrados.append(e_celda)
                                    imagenes_cargadas.append(imagen_aux)
                                    imagen_sin_guardar = False
                                else:
                                    descripcion = "Se encontró un separador de imagen, hacen falta las siguientes secciones de imagen: "
                                    if not titulo_guardado:
                                        descripcion += 'TITULO, '
                                    if not ancho_guardado:
                                        descripcion += 'ANCHO, '
                                    if not alto_guardado:
                                        descripcion += 'ALTO, '
                                    if not filas_guardado:
                                        descripcion += 'FILAS, '
                                    if not columnas_guardado:
                                        descripcion += 'COLUMNAS, '
                                    if not celdas_guardado:
                                        descripcion += 'CELDAS, '
                                    descripcion += "no fue posible guardar la imagen."
                                    new_error += 1
                                    e_secciones_faltantes = Error(new_error, caracter, descripcion, fila, columna-(len(lexema_actual)-1))
                                    errores_encontrados.append(e_secciones_faltantes)
                                    imagen_sin_guardar = False
                                titulo_guardado = False
                                titulo_aux = ''
                                ancho_guardado = False
                                ancho_aux = 0
                                alto_guardado = False
                                alto_aux = 0
                                filas_guardado = False
                                filas_aux = 0
                                columnas_guardado = False
                                columnas_aux = 0
                                celdas_guardado = False
                                posx_aux = ''
                                posy_aux = ''
                                boolean_aux = None
                                color_aux =''
                                celda_aux = None
                                celdas_aux = []
                                filtros_guardado = False
                                imagen_aux = None
                                filtros_aux = []
                                sections = 0
                                lexema_actual += caracter
                                estado_file = "a2"
                            elif caracter == "$":
                                for tkn in tokens:
                                    tkn.reinicio_token()
                                if sections == 6 and titulo_guardado and ancho_guardado and alto_guardado and filas_guardado and columnas_guardado and celdas_guardado:
                                    imagen_aux = Imagen(titulo_aux, ancho_aux, alto_aux, filas_aux, columnas_aux, celdas_aux)
                                    celdas_no_encontradas = imagen_aux.nuevas_celdas()
                                    for celda in celdas_no_encontradas:
                                        new_error += 1
                                        e_celda = Error(new_error, 'Celda: (' + str(celda.pos_x) + ', ' + str(celda.pos_y) + ')', "No se encontró la celda. Posición máxima: (" + str(columnas_aux - 1) + ", " + str(filas_aux - 1) + ")", '-', '-')
                                        errores_encontrados.append(e_celda)
                                    imagenes_cargadas.append(imagen_aux)
                                    imagen_sin_guardar = False
                                else:
                                    descripcion = "Se finalizó la lectura del archivo, hacen falta las siguientes secciones de imagen: "
                                    if not titulo_guardado:
                                        descripcion += 'TITULO, '
                                    if not ancho_guardado:
                                        descripcion += 'ANCHO, '
                                    if not alto_guardado:
                                        descripcion += 'ALTO, '
                                    if not filas_guardado:
                                        descripcion += 'FILAS, '
                                    if not columnas_guardado:
                                        descripcion += 'COLUMNAS, '
                                    if not celdas_guardado:
                                        descripcion += 'CELDAS, '
                                    descripcion += "no fue posible guardar la imagen."
                                    new_error += 1
                                    e_secciones_faltantes = Error(new_error, caracter, descripcion, fila, columna-(len(lexema_actual)-1))
                                    errores_encontrados.append(e_secciones_faltantes)
                                    imagen_sin_guardar = False
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_seccion = Error(new_error, caracter, "Se esperaba un caracter de inicio de sección, separador de imagen o fin de archivo.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_seccion)
                        elif estado_sec == "c1":
                            if caracter == "I":
                                lexema_actual += caracter
                                estado_sec = "c2"
                            else:
                                new_error += 1
                                e_I = Error(new_error, caracter, "Se esperaba una 'I' de la palabra reservada 'TITULO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_I)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c2":
                            if caracter == "T":
                                lexema_actual += caracter
                                estado_sec = "c3"
                            else:
                                new_error += 1
                                e_T = Error(new_error, caracter, "Se esperaba la segunda 'T' de la palabra reservada 'TITULO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_T)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c3":
                            if caracter == "U":
                                lexema_actual += caracter
                                estado_sec = "c4"
                            else:
                                new_error += 1
                                e_U = Error(new_error, caracter, "Se esperaba la 'U' de la palabra reservada 'TITULO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_U)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c4":
                            if caracter == "L":
                                lexema_actual += caracter
                                estado_sec = "c5"
                            else:
                                new_error += 1
                                e_L = Error(new_error, caracter, "Se esperaba la 'L' de la palabra reservada 'TITULO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_L)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c5":
                            if caracter == "O":
                                lexema_actual += caracter
                                new_token += 1
                                tit = Token(1, "Titulo", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(tit)
                                lexema_actual = ""
                                estado_sec = "c6"
                            else:
                                new_error += 1
                                e_O = Error(new_error, caracter, "Se esperaba la 'O' de la palabra reservada 'TITULO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_O)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c6":
                            if caracter == "=":
                                lexema_actual += caracter
                                new_token += 1
                                eq = Token(11, "Igual", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(eq)
                                lexema_actual = ""
                                estado_sec = "c7"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_Eq = Error(new_error, caracter, "Se esperaba el token '=' para la asignación del 'TITULO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_Eq)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c7":
                            if caracter == '"':
                                lexema_actual += caracter
                                estado_sec = "c8"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_com_d = Error(new_error, caracter, "Se esperaba el caracter '\"' que inicia la cadena del 'TITULO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_com_d)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c8":
                            if self.is_ascii(caracter):
                                lexema_actual += caracter
                                estado_sec = "c9"
                            else:
                                # TODO Error léxico, caracter no válido
                                pass
                        elif estado_sec == "c9":
                            if self.is_ascii(caracter):
                                lexema_actual += caracter
                            elif caracter == '"':
                                lexema_actual += caracter
                                new_token += 1
                                cad = Token(12, "Cadena", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(cad)
                                titulo_aux = lexema_actual
                                lexema_actual = ""
                                estado_sec = "c10"
                            else:
                                new_error += 1
                                e_com_d = Error(new_error, caracter, "Se esperaba el caracter '\"' que finaliza la cadena del 'TITULO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_com_d)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c10":
                            if caracter == ";":
                                lexema_actual += caracter
                                new_token += 1
                                p_c = Token(18, "Punto y coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(p_c)
                                lexema_actual = ""
                                for tkn in tokens:
                                    if tkn.id_token == 1:
                                        tkn.token_leido()
                                        break
                                titulo_guardado = True
                                estado_sec = "c85"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                titulo_aux = ''
                                new_error += 1
                                e_p_c = Error(new_error, caracter, "Se esperaba el token ';' que finaliza la sección del 'TITULO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_p_c)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c11":
                            if caracter == "N":
                                for tkn in tokens:
                                    if tkn.id_token == 2:
                                        if tkn.is_already_read():
                                            new_error += 1
                                            e_read = Error(new_error, caracter, "'N' dentro de inicio de sección. El token 'ANCHO' ha sido leído previamente.", fila, columna-(len(lexema_actual)-1))
                                            errores_encontrados.append(e_read)
                                            lexema_actual = ""
                                            estado_sec = "c0"
                                        else:
                                            act_ancho = True
                                            lexema_actual += caracter
                                            estado_sec = "c12"
                                        break
                            elif caracter == "L":
                                for tkn in tokens:
                                    if tkn.id_token == 3:
                                        if tkn.is_already_read():
                                            new_error += 1
                                            e_read = Error(new_error, caracter, "'L' dentro de inicio de sección. El token 'ALTO' ha sido leído previamente.", fila, columna-(len(lexema_actual)-1))
                                            errores_encontrados.append(e_read)
                                            lexema_actual = ""
                                            estado_sec = "c0"
                                        else:
                                            act_alto = True
                                            lexema_actual += caracter
                                            estado_sec = "c16"
                                        break
                            else:
                                new_error += 1
                                e_seccion = Error(new_error, caracter, "Se esperaba el caracter 'N' ó 'L' de la sección 'ANCHO' ó 'ALTO' respectivamente.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_seccion)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c12":
                            if caracter == "C":
                                lexema_actual += caracter
                                estado_sec = "c13"
                            else:
                                new_error += 1
                                e_C = Error(new_error, caracter, "Se esperaba la 'C' de la sección 'ANCHO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_C)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c13":
                            if caracter == "H":
                                lexema_actual += caracter
                                estado_sec = "c14"
                            else:
                                new_error += 1
                                e_H = Error(new_error, caracter, "Se esperaba la 'H' de la sección 'ANCHO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_H)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c14":
                            if caracter == "O":
                                lexema_actual += caracter
                                new_token += 1
                                an = Token(2, "Ancho", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(an)
                                lexema_actual = ""
                                estado_sec = "c15"
                            else:
                                new_error += 1
                                e_O = Error(new_error, caracter, "Se esperaba la 'O' de la sección 'ANCHO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_O)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c15":
                            if caracter == "=":
                                lexema_actual += caracter
                                new_token += 1
                                eq = Token(11, "Igual", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(eq)
                                lexema_actual = ""
                                estado_sec = "c19"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_Eq = Error(new_error, caracter, "Se esperaba el token '=' para la asignación del 'ANCHO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_Eq)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c16":
                            if caracter == "T":
                                lexema_actual += caracter
                                estado_sec = "c17"
                            else:
                                new_error += 1
                                e_T = Error(new_error, caracter, "Se esperaba la 'T' de la sección 'ALTO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_T)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c17":
                            if caracter == "O":
                                lexema_actual += caracter
                                new_token += 1
                                al = Token(3, "Alto", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(al)
                                lexema_actual = ""
                                estado_sec = "c18"
                            else:
                                new_error += 1
                                e_O = Error(new_error, caracter, "Se esperaba la 'O' de la sección 'ALTO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_O)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c18":
                            if caracter == "=":
                                lexema_actual += caracter
                                new_token += 1
                                eq = Token(11, "Igual", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(eq)
                                lexema_actual = ""
                                estado_sec = "c19"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_Eq = Error(new_error, caracter, "Se esperaba el token '=' para la asignación del 'ALTO'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_Eq)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c19":
                            if self.is_number(caracter):
                                lexema_actual += caracter
                                estado_sec = "c20"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                actual = ""
                                if act_ancho:
                                    actual = "ANCHO"
                                    act_ancho = False
                                elif act_alto:
                                    actual = "ALTO"
                                    act_alto = False
                                elif act_filas:
                                    actual = "FILAS"
                                    act_filas = False
                                elif act_columnas:
                                    actual = "COLUMNAS"
                                    act_columnas = False
                                new_error += 1
                                e_num = Error(new_error, caracter, "Se esperaba un número, correspondiente a la sección '"+actual+"'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_num)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c20":
                            if self.is_number(caracter):
                                lexema_actual += caracter
                            elif caracter == ";":
                                new_token += 1
                                num = Token(13, "Numero", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)))
                                tokens_leidos.append(num)
                                if act_ancho:
                                    try:
                                        ancho_aux = int(lexema_actual)
                                        ancho_guardado = True
                                    except Exception as e:
                                        print(e)
                                        print("-> Ocurrió un error en el parseo a entero del lexema " + lexema_actual + ", correspondiente al ANCHO.")
                                elif act_alto:
                                    try:
                                        alto_aux = int(lexema_actual)
                                        alto_guardado = True
                                    except Exception as e:
                                        print(e)
                                        print("-> Ocurrió un error en el parseo a entero del lexema " + lexema_actual + ", correspondiente al ALTO.")
                                elif act_filas:
                                    try:
                                        filas_aux = int(lexema_actual)
                                        filas_guardado = True
                                    except Exception as e:
                                        print(e)
                                        print("-> Ocurrió un error en el parseo a entero del lexema " + lexema_actual + ", correspondiente al FILAS.")
                                elif act_columnas:
                                    try:
                                        columnas_aux = int(lexema_actual)
                                        columnas_guardado = True
                                    except Exception as e:
                                        print(e)
                                        print("-> Ocurrió un error en el parseo a entero del lexema " + lexema_actual + ", correspondiente al COLUMNAS.")
                                lexema_actual = ""
                                lexema_actual += caracter
                                new_token += 1
                                p_c = Token(18, "Punto y coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(p_c)
                                lexema_actual = ""
                                id_act = 0
                                if act_ancho:
                                    id_act = 2
                                    act_ancho = False
                                elif act_alto:
                                    id_act = 3
                                    act_alto = False
                                elif act_filas:
                                    id_act = 4
                                    act_filas = False
                                elif act_columnas:
                                    id_act = 5
                                    act_columnas = False
                                for tkn in tokens:
                                    if tkn.id_token == id_act:
                                        tkn.token_leido()
                                        break
                                estado_sec = "c85"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                new_token += 1
                                num = Token(13, "Numero", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)))
                                tokens_leidos.append(num)
                                lexema_actual = ""
                                estado_sec = "c20.5"
                            else:
                                actual = ""
                                if act_ancho:
                                    actual = "ANCHO"
                                    act_ancho = False
                                elif act_alto:
                                    actual = "ALTO"
                                    act_alto = False
                                elif act_filas:
                                    actual = "FILAS"
                                    act_filas = False
                                elif act_columnas:
                                    actual = "COLUMNAS"
                                    act_columnas = False
                                new_error += 1
                                e_num_p_c = Error(new_error, caracter, "Se esperaba un número o un ';', correspondiente a la sección '"+actual+"'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_num_p_c)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c20.5":
                            if caracter == ";":
                                lexema_actual += caracter
                                new_token += 1
                                p_c = Token(18, "Punto y coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(p_c)
                                lexema_actual = ""
                                estado_sec = "c85"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                actual = ""
                                if act_ancho:
                                    actual = "ANCHO"
                                    act_ancho = False
                                elif act_alto:
                                    actual = "ALTO"
                                    act_alto = False
                                elif act_filas:
                                    actual = "FILAS"
                                    act_filas = False
                                elif act_columnas:
                                    actual = "COLUMNAS"
                                    act_columnas = False
                                new_error += 1
                                e_p_c = Error(new_error, caracter, "Se esperaba un un ';', para la finalización de la sección '"+actual+"'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_p_c)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c21":
                            if caracter == "I":
                                lexema_actual += caracter
                                estado_sec = "c22"
                            else:
                                new_error += 1
                                e_I = Error(new_error, caracter, "Se esperaba la 'I' de la sección 'FILAS' o 'FILTROS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_I)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c22":
                            if caracter == "L":
                                lexema_actual += caracter
                                estado_sec = "c23"
                            else:
                                new_error += 1
                                e_L = Error(new_error, caracter, "Se esperaba la 'L' de la sección 'FILAS' ó 'FILTROS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_L)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c23":
                            if caracter == "A":
                                for tkn in tokens:
                                    if tkn.id_token == 4:
                                        if tkn.is_already_read():
                                            new_error += 1
                                            e_read = Error(new_error, caracter, "'A' dentro de inicio de sección. El token 'FILAS' ha sido leído previamente.", fila, columna-(len(lexema_actual)-1))
                                            errores_encontrados.append(e_read)
                                            lexema_actual = ""
                                            estado_sec = "c0"
                                        else:
                                            act_filas = True
                                            lexema_actual += caracter
                                            estado_sec = "c24"
                                        break
                            elif caracter == "T":
                                for tkn in tokens:
                                    if tkn.id_token == 7:
                                        if tkn.is_already_read():
                                            new_error += 1
                                            e_read = Error(new_error, caracter, "'T' dentro de inicio de sección. El token 'FILTROS' ha sido leído previamente.", fila, columna-(len(lexema_actual)-1))
                                            errores_encontrados.append(e_read)
                                            lexema_actual = ""
                                            estado_sec = "c0"
                                        else:
                                            lexema_actual += caracter
                                            estado_sec = "c26"
                                        break
                            else:
                                new_error += 1
                                e_seccion = Error(new_error, caracter, "Se esperaba la 'A' ó la 'T' de las secciones 'FILAS' ó 'FILTROS' respectivamente.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_seccion)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c24":
                            if caracter == "S":
                                lexema_actual += caracter
                                new_token += 1
                                fi = Token(4, "Filas", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(fi)
                                lexema_actual = ""
                                estado_sec = "c25"
                            else:
                                new_error += 1
                                e_S = Error(new_error, caracter, "Se esperaba la 'S' de la sección 'FILAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_S)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c25":
                            if caracter == "=":
                                lexema_actual += caracter
                                new_token += 1
                                eq = Token(11, "Igual", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(eq)
                                lexema_actual = ""
                                estado_sec = "c19"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_Eq = Error(new_error, caracter, "Se esperaba el token '=' para la asignación de la sección 'FILAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_Eq)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c26":
                            if caracter == "R":
                                lexema_actual += caracter
                                estado_sec = "c27"
                            else:
                                new_error += 1
                                e_R = Error(new_error, caracter, "Se esperaba la 'R' de la sección 'FILTROS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_R)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c27":
                            if caracter == "O":
                                lexema_actual += caracter
                                estado_sec = "c28"
                            else:
                                new_error += 1
                                e_O = Error(new_error, caracter, "Se esperaba la 'O' de la sección 'FILTROS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_O)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c28":
                            if caracter == "S":
                                lexema_actual += caracter
                                new_token += 1
                                filt = Token(7, "Filtros", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(filt)
                                lexema_actual = ""
                                estado_sec = "c29"
                            else:
                                new_error += 1
                                e_S = Error(new_error, caracter, "Se esperaba la 'S' de la sección 'FILTROS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_S)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c29":
                            if caracter == "=":
                                lexema_actual += caracter
                                new_token += 1
                                eq = Token(11, "Igual", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(eq)
                                lexema_actual = ""
                                estado_sec = "c30"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_Eq = Error(new_error, caracter, "Se esperaba el token '=' para la asignación de la sección 'FILTROS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_Eq)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c30":
                            if caracter == "M":
                                lexema_actual += caracter
                                estado_sec = "c31"
                            elif caracter == "D":
                                lexema_actual += caracter
                                estado_sec = "c39"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_seccion = Error(new_error, caracter, "Se esperaba la 'M' ó la 'D' de los filtros de 'MIRROR' ó 'DOUBLEMIRROR' respectivamente.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_seccion)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c31":
                            if caracter == "I":
                                lexema_actual += caracter
                                estado_sec = "c32"
                            else:
                                new_error += 1
                                e_I = Error(new_error, caracter, "Se esperaba la 'I' del filtro 'MIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_I)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c32":
                            if caracter == "R":
                                lexema_actual += caracter
                                estado_sec = "c33"
                            else:
                                new_error += 1
                                e_R = Error(new_error, caracter, "Se esperaba la primera 'R' del filtro 'MIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_R)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c33":
                            if caracter == "R":
                                lexema_actual += caracter
                                estado_sec = "c34"
                            else:
                                new_error += 1
                                e_R = Error(new_error, caracter, "Se esperaba la segunda 'R' del filtro 'MIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_R)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c34":
                            if caracter == "O":
                                lexema_actual += caracter
                                estado_sec = "c35"
                            else:
                                new_error += 1
                                e_O = Error(new_error, caracter, "Se esperaba la 'O' del filtro 'MIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_O)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c35":
                            if caracter == "R":
                                lexema_actual += caracter
                                estado_sec = "c36"
                            else:
                                new_error += 1
                                e_R = Error(new_error, caracter, "Se esperaba la tercera 'R' del filtro 'MIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_R)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c36":
                            if caracter == "X":
                                lexema_actual += caracter
                                new_token += 1
                                m_x = Token(8, "MirrorX", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(m_x)
                                filtros_aux.append(lexema_actual)
                                lexema_actual = ""
                                estado_sec = "c37"
                            elif caracter == "Y":
                                lexema_actual += caracter
                                new_token += 1
                                m_y = Token(9, "MirrorY", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(m_y)
                                filtros_aux.append(lexema_actual)
                                lexema_actual = ""
                                estado_sec = "c38"
                            else:
                                new_error += 1
                                e_seccion = Error(new_error, caracter, "Se esperaba la 'X' ó la 'Y' de los filtros de 'MIRRORX' ó 'MIRRORY' respectivamente.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_seccion)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c37":
                            if caracter == ",":
                                lexema_actual += caracter
                                new_token += 1
                                com = Token(16, "Coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(com)
                                lexema_actual = ""
                                estado_sec = "c30"
                            elif caracter == ";":
                                lexema_actual += caracter
                                new_token += 1
                                p_c = Token(18, "Punto y coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(p_c)
                                lexema_actual = ""
                                filtros_guardado = True
                                for tkn in tokens:
                                    if tkn.id_token == 7:
                                        tkn.token_leido()
                                        break
                                estado_sec = "c85"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_seccion = Error(new_error, caracter, "Se esperaba la ',' ó ';' para un nuevo filtro ó finalizar la sección 'FILTROS' respectivamente.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_seccion)
                                filtros_aux = []
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c38":
                            if caracter == ",":
                                lexema_actual += caracter
                                new_token += 1
                                com = Token(16, "Coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(com)
                                lexema_actual = ""
                                estado_sec = "c30"
                            elif caracter == ";":
                                lexema_actual += caracter
                                new_token += 1
                                p_c = Token(18, "Punto y coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(p_c)
                                lexema_actual = ""
                                filtros_guardado = True
                                for tkn in tokens:
                                    if tkn.id_token == 7:
                                        tkn.token_leido()
                                        break
                                estado_sec = "c85"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_seccion = Error(new_error, caracter, "Se esperaba la ',' ó ';' para un nuevo filtro ó finalizar la sección 'FILTROS' respectivamente.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_seccion)
                                filtros_aux = []
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c39":
                            if caracter == "O":
                                lexema_actual += caracter
                                estado_sec = "c40"
                            else:
                                new_error += 1
                                e_O = Error(new_error, caracter, "Se esperaba la primera 'O' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_O)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c40":
                            if caracter == "U":
                                lexema_actual += caracter
                                estado_sec = "c41"
                            else:
                                new_error += 1
                                e_U = Error(new_error, caracter, "Se esperaba la 'U' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_U)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c41":
                            if caracter == "B":
                                lexema_actual += caracter
                                estado_sec = "c42"
                            else:
                                new_error += 1
                                e_B = Error(new_error, caracter, "Se esperaba la 'B' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_B)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c42":
                            if caracter == "L":
                                lexema_actual += caracter
                                estado_sec = "c43"
                            else:
                                new_error += 1
                                e_L = Error(new_error, caracter, "Se esperaba la 'L' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_L)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c43":
                            if caracter == "E":
                                lexema_actual += caracter
                                estado_sec = "c44"
                            else:
                                new_error += 1
                                e_E = Error(new_error, caracter, "Se esperaba la 'E' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_E)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c44":
                            if caracter == "M":
                                lexema_actual += caracter
                                estado_sec = "c45"
                            else:
                                new_error += 1
                                e_M = Error(new_error, caracter, "Se esperaba la 'M' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_M)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c45":
                            if caracter == "I":
                                lexema_actual += caracter
                                estado_sec = "c46"
                            else:
                                new_error += 1
                                e_I = Error(new_error, caracter, "Se esperaba la 'I' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_I)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c46":
                            if caracter == "R":
                                lexema_actual += caracter
                                estado_sec = "c47"
                            else:
                                new_error += 1
                                e_R = Error(new_error, caracter, "Se esperaba la primera 'R' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_R)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c47":
                            if caracter == "R":
                                lexema_actual += caracter
                                estado_sec = "c48"
                            else:
                                new_error += 1
                                e_R = Error(new_error, caracter, "Se esperaba la segunda 'R' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_R)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c48":
                            if caracter == "O":
                                lexema_actual += caracter
                                estado_sec = "c49"
                            else:
                                new_error += 1
                                e_O = Error(new_error, caracter, "Se esperaba la segunda 'O' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_O)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c49":
                            if caracter == "R":
                                lexema_actual += caracter
                                new_token += 1
                                d_m = Token(10, "DoubleMirror", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(d_m)
                                filtros_aux.append(lexema_actual)
                                lexema_actual = ""
                                estado_sec = "c50"
                            else:
                                new_error += 1
                                e_R = Error(new_error, caracter, "Se esperaba la tercera 'R' del filtro 'DOUBLEMIRROR'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_R)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c50":
                            if caracter == ",":
                                lexema_actual += caracter
                                new_token += 1
                                com = Token(16, "Coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(com)
                                lexema_actual = ""
                                estado_sec = "c30"
                            elif caracter == ";":
                                lexema_actual += caracter
                                new_token += 1
                                p_c = Token(18, "Punto y coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(p_c)
                                lexema_actual = ""
                                filtros_guardado = True
                                for tkn in tokens:
                                    if tkn.id_token == 7:
                                        tkn.token_leido()
                                        break
                                estado_sec = "c85"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_seccion = Error(new_error, caracter, "Se esperaba la ',' ó ';' para un nuevo filtro ó finalizar la sección 'FILTROS' respectivamente.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_seccion)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c51":
                            if caracter == "O":
                                for tkn in tokens:
                                    if tkn.id_token == 5:
                                        if tkn.is_already_read():
                                            new_error += 1
                                            e_read = Error(new_error, caracter, "'O' dentro de inicio de sección. El token 'COLUMNAS' ha sido leído previamente.", fila, columna-(len(lexema_actual)-1))
                                            errores_encontrados.append(e_read)
                                            lexema_actual = ""
                                            estado_sec = "c0"
                                        else:
                                            act_columnas = True
                                            lexema_actual += caracter
                                            estado_sec = "c52"
                                        break
                            elif caracter == "E":
                                for tkn in tokens:
                                    if tkn.id_token == 6:
                                        if tkn.is_already_read():
                                            new_error += 1
                                            e_read = Error(new_error, caracter, "'E' dentro de inicio de sección. El token 'CELDAS' ha sido leído previamente.", fila, columna-(len(lexema_actual)-1))
                                            errores_encontrados.append(e_read)
                                            lexema_actual = ""
                                            estado_sec = "c0"
                                        else:
                                            lexema_actual += caracter
                                            estado_sec = "c59"
                                        break
                            else:
                                new_error += 1
                                e_seccion = Error(new_error, caracter, "Se esperaba la 'O' ó la 'E' de las secciones 'COLUMNAS' ó 'CELDAS' respectivamente.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_seccion)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c52":
                            if caracter == "L":
                                lexema_actual += caracter
                                estado_sec = "c53"
                            else:
                                new_error += 1
                                e_L = Error(new_error, caracter, "Se esperaba la 'L' de la sección 'COLUMNAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_L)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c53":
                            if caracter == "U":
                                lexema_actual += caracter
                                estado_sec = "c54"
                            else:
                                new_error += 1
                                e_U = Error(new_error, caracter, "Se esperaba la 'U' de la sección 'COLUMNAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_U)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c54":
                            if caracter == "M":
                                lexema_actual += caracter
                                estado_sec = "c55"
                            else:
                                new_error += 1
                                e_M = Error(new_error, caracter, "Se esperaba la 'M' de la sección 'COLUMNAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_M)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c55":
                            if caracter == "N":
                                lexema_actual += caracter
                                estado_sec = "c56"
                            else:
                                new_error += 1
                                e_N = Error(new_error, caracter, "Se esperaba la 'N' de la sección 'COLUMNAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_N)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c56":
                            if caracter == "A":
                                lexema_actual += caracter
                                estado_sec = "c57"
                            else:
                                new_error += 1
                                e_A = Error(new_error, caracter, "Se esperaba la 'A' de la sección 'COLUMNAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_A)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c57":
                            if caracter == "S":
                                lexema_actual += caracter
                                new_token += 1
                                col = Token(5, "Columnas", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(col)
                                lexema_actual = ""
                                estado_sec = "c58"
                            else:
                                new_error += 1
                                e_S = Error(new_error, caracter, "Se esperaba la 'S' de la sección 'COLUMNAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_S)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c58":
                            if caracter == "=":
                                lexema_actual += caracter
                                new_token += 1
                                eq = Token(11, "Igual", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(eq)
                                lexema_actual = ""
                                estado_sec = "c19"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_Eq = Error(new_error, caracter, "Se esperaba el token '=' para la asignación de la sección 'COLUMNAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_Eq)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c59":
                            if caracter == "L":
                                lexema_actual += caracter
                                estado_sec = "c60"
                            else:
                                new_error += 1
                                e_L = Error(new_error, caracter, "Se esperaba la 'L' de la sección 'CELDAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_L)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c60":
                            if caracter == "D":
                                lexema_actual += caracter
                                estado_sec = "c61"
                            else:
                                new_error += 1
                                e_D = Error(new_error, caracter, "Se esperaba la 'D' de la sección 'CELDAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_D)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c61":
                            if caracter == "A":
                                lexema_actual += caracter
                                estado_sec = "c62"
                            else:
                                new_error += 1
                                e_A = Error(new_error, caracter, "Se esperaba la 'A' de la sección 'CELDAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_A)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c62":
                            if caracter == "S":
                                lexema_actual += caracter
                                new_token += 1
                                cel = Token(6, "Celdas", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(cel)
                                lexema_actual = ""
                                estado_sec = "c63"
                            else:
                                new_error += 1
                                e_S = Error(new_error, caracter, "Se esperaba la 'S' de la sección 'CELDAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_S)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c63":
                            if caracter == "=":
                                lexema_actual += caracter
                                new_token += 1
                                eq = Token(11, "Igual", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(eq)
                                lexema_actual = ""
                                estado_sec = "c64"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_Eq = Error(new_error, caracter, "Se esperaba el token '=' para la asignación de la sección 'CELDAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_Eq)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c64":
                            if caracter == "{":
                                lexema_actual += caracter
                                new_token += 1
                                a_ll = Token(14, "Abre llave", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(a_ll)
                                lexema_actual = ""
                                estado_sec = "c65"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_a_ll = Error(new_error, caracter, "Se esperaba el token '{' de la sección 'CELDAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_a_ll)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c65":
                            if caracter == "[":
                                lexema_actual += caracter
                                estado_sec = "c66"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_a_cor = Error(new_error, caracter, "Se esperaba el caracter '[' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_a_cor)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c66":
                            if self.is_number(caracter):
                                lexema_actual += caracter
                                posx_aux += caracter
                                estado_sec = "c67"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                            else:
                                new_error += 1
                                e_num = Error(new_error, caracter, "Se esperaba un número, propio de las X del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_num)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c67":
                            if self.is_number(caracter):
                                lexema_actual += caracter
                                posx_aux += caracter
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                                estado_sec = "c67.5"
                            elif caracter == ",":
                                lexema_actual += caracter
                                estado_sec = "c68"
                            else:
                                new_error += 1
                                e_num_com = Error(new_error, caracter, "Se esperaba un número propio de las X ó una coma, ambos caracteres del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_num_com)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c67.5":
                            if caracter == ",":
                                lexema_actual += caracter
                                estado_sec = "c68"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                            else:
                                new_error += 1
                                e_com = Error(new_error, caracter, "Se esperaba una coma para finalizar las X del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_com)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c68":
                            if self.is_number(caracter):
                                lexema_actual += caracter
                                posy_aux += caracter
                                estado_sec = "c69"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                            else:
                                new_error += 1
                                e_num = Error(new_error, caracter, "Se esperaba un número, propio de las Y del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_num)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c69":
                            if self.is_number(caracter):
                                lexema_actual += caracter
                                posy_aux += caracter
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                                estado_sec = "c69.5"
                            elif caracter == ",":
                                lexema_actual += caracter
                                estado_sec = "c70"
                            else:
                                new_error += 1
                                e_num_com = Error(new_error, caracter, "Se esperaba un número propio de las Y ó una coma, ambos caracteres del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_num_com)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c69.5":
                            if caracter == ",":
                                lexema_actual += caracter
                                estado_sec = "c70"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                            else:
                                new_error += 1
                                e_com = Error(new_error, caracter, "Se esperaba una coma para finalizar las Y del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_com)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c70":
                            if caracter == "T":
                                lexema_actual += caracter
                                estado_sec = "c71"
                            elif caracter == "F":
                                lexema_actual += caracter
                                estado_sec = "c75"
                            else:
                                new_error += 1
                                e_seccion = Error(new_error, caracter, "Se esperaba la 'T' ó la 'F' de 'TRUE' ó 'FALSE' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_seccion)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c71":
                            if caracter == "R":
                                lexema_actual += caracter
                                estado_sec = "c72"
                            else:
                                new_error += 1
                                e_R = Error(new_error, caracter, "Se esperaba la 'R' de 'TRUE' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_R)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c72":
                            if caracter == "U":
                                lexema_actual += caracter
                                estado_sec = "c73"
                            else:
                                new_error += 1
                                e_U = Error(new_error, caracter, "Se esperaba la 'U' de 'TRUE' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_U)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c73":
                            if caracter == "E":
                                lexema_actual += caracter
                                boolean_aux = True
                                estado_sec = "c74"
                            else:
                                new_error += 1
                                e_E = Error(new_error, caracter, "Se esperaba la 'E' de 'TRUE' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_E)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c74":
                            if caracter == ",":
                                lexema_actual += caracter
                                estado_sec = "c80"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                            else:
                                new_error += 1
                                e_com = Error(new_error, caracter, "Se esperaba la ',' que finaliza la palabra 'TRUE' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_com)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c75":
                            if caracter == "A":
                                lexema_actual += caracter
                                estado_sec = "c76"
                            else:
                                new_error += 1
                                e_A = Error(new_error, caracter, "Se esperaba la 'A' de 'FALSE' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_A)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c76":
                            if caracter == "L":
                                lexema_actual += caracter
                                estado_sec = "c77"
                            else:
                                new_error += 1
                                e_L = Error(new_error, caracter, "Se esperaba la 'L' de 'FALSE' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_L)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c77":
                            if caracter == "S":
                                lexema_actual += caracter
                                estado_sec = "c78"
                            else:
                                new_error += 1
                                e_S = Error(new_error, caracter, "Se esperaba la 'S' de 'FALSE' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_S)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c78":
                            if caracter == "E":
                                lexema_actual += caracter
                                boolean_aux = False
                                estado_sec = "c79"
                            else:
                                new_error += 1
                                e_E = Error(new_error, caracter, "Se esperaba la 'E' de 'FALSE' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_E)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c79":
                            if caracter == ",":
                                lexema_actual += caracter
                                estado_sec = "c80"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                            else:
                                new_error += 1
                                e_com = Error(new_error, caracter, "Se esperaba la ',' que finaliza la palabra 'FALSE' del token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_com)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c80":
                            if caracter == "#":
                                lexema_actual += caracter
                                color_aux += caracter
                                estado_sec = "c81"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                            else:
                                new_error += 1
                                e_hash = Error(new_error, caracter, "Se esperaba el símbolo '#' que indica el color de la 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_hash)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c81":
                            if self.is_hexadecimal_letter(caracter) or self.is_number(caracter):
                                lexema_actual += caracter
                                color_aux += caracter
                                estado_sec = "c82"
                            else:
                                new_error += 1
                                e_hexa = Error(new_error, caracter, "Se esperaba un número hexadecimal (0-9, A-F) para el token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_hexa)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c82":
                            if self.is_hexadecimal_letter(caracter) or self.is_number(caracter):
                                lexema_actual += caracter
                                color_aux += caracter
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                                estado_sec = "c82.5"
                            elif caracter == "]":
                                lexema_actual += caracter
                                new_token += 1
                                cell = Token(15, "Celda", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(cell)
                                lexema_actual = ""
                                try:
                                    posx_aux = int(posx_aux)
                                    posy_aux = int(posy_aux)
                                    celda_aux = Imagen.Celda(posx_aux, posy_aux, color = color_aux, is_painted = boolean_aux)
                                    celdas_aux.append(celda_aux)
                                    posx_aux = ''
                                    posy_aux = ''
                                    color_aux =  ''
                                    boolean_aux = None
                                except Exception as e:
                                    print(e)
                                    print("-> Ocurrió un error en el parseo de las posiciones x y de una celda.")
                                estado_sec = "c83"
                            else:
                                new_error += 1
                                e_hexa_c_cor = Error(new_error, caracter, "Se esperaba un número hexadecimal (0-9, A-F) o el caracter ']' para el token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_hexa_c_cor)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c82.5":
                            if caracter == "]":
                                lexema_actual += caracter
                                new_token += 1
                                cell = Token(15, "Celda", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(cell)
                                lexema_actual = ""
                                try:
                                    posx_aux = int(posx_aux)
                                    posy_aux = int(posy_aux)
                                    celda_aux = Imagen.Celda(posx_aux, posy_aux, color = color_aux, is_painted = boolean_aux)
                                    celdas_aux.append(celda_aux)
                                    posx_aux = ''
                                    posy_aux = ''
                                    color_aux =  ''
                                    boolean_aux = None
                                except Exception as e:
                                    print(e)
                                    print("-> Ocurrió un error en el parseo de las posiciones x y de una celda.")
                                estado_sec = "c83"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                            else:
                                new_error += 1
                                e_c_cor = Error(new_error, caracter, "Se esperaba el caracter ']' que finaliza el token 'CELDA'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_c_cor)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c83":
                            if caracter == ",":
                                lexema_actual += caracter
                                new_token += 1
                                com = Token(16, "Coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(com)
                                lexema_actual = ""
                                estado_sec = "c65"
                            elif caracter == "}":
                                lexema_actual += caracter
                                new_token += 1
                                c_ll = Token(17, "Cierra llave", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(c_ll)
                                lexema_actual = ""
                                estado_sec = "c84"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_com_c_ll = Error(new_error, caracter, "Se esperaba la ',' o el '}', para un nuevo token 'CELDA' ó para cerrar la sección 'CELDAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_com_c_ll)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c84":
                            if caracter == ";":
                                lexema_actual += caracter
                                new_token += 1
                                p_c = Token(18, "Punto y coma", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(p_c)
                                celdas_guardado = True
                                lexema_actual = ""
                                for tkn in tokens:
                                    if tkn.id_token == 6:
                                        tkn.token_leido()
                                        break
                                estado_sec = "c85"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
                                new_error += 1
                                e_p_c = Error(new_error, caracter, "Se esperaba la ';' para finalizar la sección 'CELDAS'.", fila, columna-(len(lexema_actual)-1))
                                errores_encontrados.append(e_p_c)
                                lexema_actual = ""
                                estado_sec = "c0"
                        elif estado_sec == "c85":
                            sections += 1
                            if sections == 7:
                                imagen_aux = Imagen(titulo_aux, ancho_aux, alto_aux, filas_aux, columnas_aux, celdas_aux, filtros = filtros_aux)
                                celdas_no_encontradas = imagen_aux.nuevas_celdas()
                                for celda in celdas_no_encontradas:
                                    new_error += 1
                                    e_celda = Error(new_error, 'Celda: (' + str(celda.pos_x) + ', ' + str(celda.pos_y) + ')', "No se encontró la celda. Posición máxima: (" + str(columnas_aux - 1) + ", " + str(filas_aux - 1) + ")", '-', '-')
                                    errores_encontrados.append(e_celda)
                                imagenes_cargadas.append(imagen_aux)
                                imagen_sin_guardar = False
                                titulo_guardado = False
                                titulo_aux = ''
                                ancho_guardado = False
                                ancho_aux = 0
                                alto_guardado = False
                                alto_aux = 0
                                filas_guardado = False
                                filas_aux = 0
                                columnas_guardado = False
                                columnas_aux = 0
                                celdas_guardado = False
                                posx_aux = ''
                                posy_aux = ''
                                boolean_aux = None
                                color_aux =''
                                celda_aux = None
                                celdas_aux = []
                                filtros_guardado = False
                                imagen_aux = None
                                filtros_aux = []
                                estado_sec = "c0"
                                sections = 0
                                for tkn in tokens:
                                    tkn.reinicio_token()
                                estado_file = "a1"
                            else:
                                estado_sec = "c0"
                elif estado_file == "a1":
                    if caracter == "@":
                        lexema_actual += caracter
                        estado_file = "a2"
                    elif caracter == "$":
                        # TODO Fin del archivo
                        pass
                    elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                        pass
                    else:
                        new_error += 1
                        e_arroba = Error(new_error, caracter, "Se esperaba el primer '@' del token 'Separador'.", fila, columna-(len(lexema_actual)-1))
                        errores_encontrados.append(e_arroba)
                elif estado_file == "a2":
                    if caracter == "@":
                        lexema_actual += caracter
                        estado_file = "a3"
                    else:
                        new_error += 1
                        e_arroba = Error(new_error, caracter, "Se esperaba el segundo '@' del token 'Separador'.", fila, columna-(len(lexema_actual)-1))
                        errores_encontrados.append(e_arroba)
                        estado_file = "a1"
                        lexema_actual = ""
                elif estado_file == "a3":
                    if caracter == "@":
                        lexema_actual += caracter
                        estado_file = "a4"
                    else:
                        new_error += 1
                        e_arroba = Error(new_error, caracter, "Se esperaba el tercer '@' del token 'Separador'.", fila, columna-(len(lexema_actual)-1))
                        errores_encontrados.append(e_arroba)
                        estado_file = "a1"
                        lexema_actual = ""
                elif estado_file == "a4":
                    if caracter == "@":
                        lexema_actual += caracter
                        new_token += 1
                        sep = Token(19, "Separador", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                        tokens_leidos.append(sep)
                        lexema_actual = ""
                        estado_file = "a5"
                    else:
                        new_error += 1
                        e_arroba = Error(new_error, caracter, "Se esperaba el cuarto '@' del token 'Separador'.", fila, columna-(len(lexema_actual)-1))
                        errores_encontrados.append(e_arroba)
                        lexema_actual = ""
                        estado_file = "a1"
            if imagen_sin_guardar:
                for tkn in tokens:
                    tkn.reinicio_token()
                if sections == 6 and titulo_guardado and ancho_guardado and alto_guardado and filas_guardado and columnas_guardado and celdas_guardado:
                    imagen_aux = Imagen(titulo_aux, ancho_aux, alto_aux, filas_aux, columnas_aux, celdas_aux)
                    celdas_no_encontradas = imagen_aux.nuevas_celdas()
                    for celda in celdas_no_encontradas:
                        new_error += 1
                        e_celda = Error(new_error, 'Celda: (' + str(celda.pos_x) + ', ' + str(celda.pos_y) + ')', "No se encontró la celda. Posición máxima: (" + str(columnas_aux - 1) + ", " + str(filas_aux - 1) + ")", '-', '-')
                        errores_encontrados.append(e_celda)
                    imagenes_cargadas.append(imagen_aux)
                else:
                    descripcion = "Se finalizó la lectura del archivo, hacen falta las siguientes secciones de imagen: "
                    if not titulo_guardado:
                        descripcion += 'TITULO, '
                    if not ancho_guardado:
                        descripcion += 'ANCHO, '
                    if not alto_guardado:
                        descripcion += 'ALTO, '
                    if not filas_guardado:
                        descripcion += 'FILAS, '
                    if not columnas_guardado:
                        descripcion += 'COLUMNAS, '
                    if not celdas_guardado:
                        descripcion += 'CELDAS, '
                    descripcion += "no fue posible guardar la imagen."
                    new_error += 1
                    e_secciones_faltantes = Error(new_error, caracter, descripcion, fila, columna-(len(lexema_actual)-1))
                    errores_encontrados.append(e_secciones_faltantes)
        else:
            pass

    def imagenes_html(self):
        global texto_cargado
        global imagenes_cargadas
        if texto_cargado:
            self.frame2_file = Frame(self.frame2, bg="white")
            self.frame2_file.place(x=0, y=0, relheight=1, relwidth=1)
            load_img2 = PhotoImage(file="images/html.png")
            load_lb = Label(self.frame2_file, image=load_img2, bg="white")
            load_lb.photo = load_img2
            load_lb.place(x=10, y=40, width=300, height=300)
            title1= Label(self.frame2_file, text="Generando las imágenes en formato HTML...", font=("Consolas", 20), bg="white")
            title1.place(x=320, y=150)
            imagenes = 0
            for imagen in imagenes_cargadas:
                img = self.generar_html(imagen)
                imagenes += img
            title1= Label(self.frame2_file, text="Imágenes en formato HTML generadas exitosamente.", font=("Consolas", 20), bg="white")
            title1.place(x=320, y=150)
            title1= Label(self.frame2_file, text=f"Imágenes generadas: {imagenes}", font=("Consolas", 20), bg="white")
            title1.place(x=320, y=190)
    
    def generar_html(self, imagen, jpg = False):
        imagenes_generadas = 0
        ancho_pixel = int(imagen.ancho / imagen.columnas)
        alto_pixel = int(imagen.alto / imagen.filas)
        css = '''body {
            background: #756d5a;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .imagen {'''
        css += f'''
            width: {imagen.ancho}px;
            height: {imagen.alto}px;'''
        css += '''\n}
        .pixel {'''
        css += f'''
            width: {ancho_pixel}px;
            height: {alto_pixel}px;'''
        css +='''\nfloat: left;
            box-shadow: 0px 0px 1px #ffffff;
        }
        #not_painted {
            background: #FFFFFF00;
        }'''
        html = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">'''
        if not jpg:
            html += f'\n<link rel="stylesheet" href="{imagen.titulo[1:len(imagen.titulo) - 1]}.css">'
            html += '''
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">'''
        html += f'''\n<title>{imagen.titulo[1:len(imagen.titulo) - 1]}</title>
        </head>
        <body>'''
        if not jpg:
            html += f'\n<p style="font-family: \'Press Start 2P\'; font-size: 40px; position: absolute; top: 0px;">{imagen.titulo[1:len(imagen.titulo) - 1]}</p>'
            html += '\n<div class="imagen" style="position: relative;">'
        else:
            html += '\n<div class="imagen">'
        for celda in imagen.matriz_celdas:
            if celda.is_painted:
                html += f'\n<div class="pixel" id="x{celda.pos_x}y{celda.pos_y}"></div>'
                css += f'\n#x{celda.pos_x}y{celda.pos_y}'
                css += ' {'
                css += f'''
                    background: {celda.color};'''
                css += '\n}'
            else:
                html += '\n<div class="pixel" id="not_painted"></div>'
        html += '''
            </div>
        </body>
        </html>'''
        try:
            ruta_html = ''
            if not jpg:
                ruta_html = f"Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]}.html"
            else:
                ruta_html = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]}.html"
            imagen_original = open(ruta_html, "w",encoding="utf8")
            imagen_original.write(html)
            imagen_original.close()
            ruta_css = ''
            if not jpg:
                ruta_css = f"Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]}.css"
            else:
                ruta_css = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]}.css"
            styles_original = open(ruta_css, "w",encoding="utf8")
            styles_original.write(css)
            styles_original.close()
            imagenes_generadas += 1
        except Exception:
            traceback.print_exc()
            print(f"-> Error en la creación del HTML - CSS de la imagen original: {imagen.titulo[1:len(imagen.titulo) - 1]}")
        if imagen.filtros is not None:
            for filtro in imagen.filtros:
                css_filtro = '''body {
                    background: #756d5a;
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                .imagen {'''
                css_filtro += f'''
                    width: {imagen.ancho}px;
                    height: {imagen.alto}px;'''
                css_filtro += '''\n}
                .pixel {'''
                css_filtro += f'''
                    width: {ancho_pixel}px;
                    height: {alto_pixel}px;'''
                css_filtro +='''\nfloat: left;
                    box-shadow: 0px 0px 1px #ffffff;
                }
                #not_painted {
                    background: #FFFFFF00;
                }'''
                html_filtro = '''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">'''
                if filtro == "MIRRORX":
                    if not jpg:
                        html_filtro += f'\n<link rel="stylesheet" href="{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX.css">'
                        html_filtro += '''
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">'''
                    html_filtro += f'''\n<title>{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX</title>
                    </head>
                    <body>'''
                    if not jpg:
                        html_filtro += f'\n<p style="font-family: \'Press Start 2P\'; font-size: 40px; position: absolute; top: 0px;">{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX</p>'
                        html_filtro += '\n<div class="imagen" style="position: relative;">'
                    else:
                        html_filtro += '\n<div class="imagen">'
                    for celda in imagen.matriz_celdas_mirrorx:
                        if celda.is_painted:
                            html_filtro += f'\n<div class="pixel" id="x{celda.pos_x}y{celda.pos_y}"></div>'
                            css_filtro += f'\n#x{celda.pos_x}y{celda.pos_y}'
                            css_filtro += ' {'
                            css_filtro += f'''
                                background: {celda.color};'''
                            css_filtro += '\n}'
                        else:
                            html_filtro += '\n<div class="pixel" id="not_painted"></div>'
                    html_filtro += '''
                        </div>
                    </body>
                    </html>'''
                    try:
                        ruta_html = ''
                        if not jpg:
                            ruta_html = f"Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX.html"
                        else:
                            ruta_html = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX.html"
                        imagen_mirrorx = open(ruta_html, "w",encoding="utf8")
                        imagen_mirrorx.write(html_filtro)
                        imagen_mirrorx.close()
                        ruta_css = ''
                        if not jpg:
                            ruta_css = f"Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX.css"
                        else:
                            ruta_css = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX.css"
                        styles_mirrorx = open(ruta_css, "w",encoding="utf8")
                        styles_mirrorx.write(css_filtro)
                        styles_mirrorx.close()
                        imagenes_generadas += 1
                    except Exception:
                        traceback.print_exc()
                        print(f"-> Error en la creación del HTML - CSS de la imagen MIRRORX: {imagen.titulo[1:len(imagen.titulo) - 1]}")
                elif filtro == "MIRRORY":
                    if not jpg:
                        html_filtro += f'\n<link rel="stylesheet" href="{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY.css">'
                        html_filtro += '''
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">'''
                    html_filtro += f'''\n<title>{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY</title>
                    </head>
                    <body>'''
                    if not jpg:
                        html_filtro += f'\n<p style="font-family: \'Press Start 2P\'; font-size: 40px; position: absolute; top: 0px;">{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY</p>'
                        html_filtro += '\n<div class="imagen" style="position: relative;">'
                    else:
                        html_filtro += '\n<div class="imagen">'
                    for celda in imagen.matriz_celdas_mirrory:
                        if celda.is_painted:
                            html_filtro += f'\n<div class="pixel" id="x{celda.pos_x}y{celda.pos_y}"></div>'
                            css_filtro += f'\n#x{celda.pos_x}y{celda.pos_y}'
                            css_filtro += ' {'
                            css_filtro += f'''
                                background: {celda.color};'''
                            css_filtro += '\n}'
                        else:
                            html_filtro += '\n<div class="pixel" id="not_painted"></div>'
                    html_filtro += '''
                        </div>
                    </body>
                    </html>'''
                    try:
                        ruta_html = ''
                        if not jpg:
                            ruta_html = f"Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY.html"
                        else:
                            ruta_html = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY.html"
                        imagen_mirrory = open(ruta_html, "w",encoding="utf8")
                        imagen_mirrory.write(html_filtro)
                        imagen_mirrory.close()
                        ruta_css = ''
                        if not jpg:
                            ruta_css = f"Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY.css"
                        else:
                            ruta_css = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY.css"
                        styles_mirrory = open(ruta_css, "w",encoding="utf8")
                        styles_mirrory.write(css_filtro)
                        styles_mirrory.close()
                        imagenes_generadas += 1
                    except Exception:
                        traceback.print_exc()
                        print(f"-> Error en la creación del HTML - CSS de la imagen MIRRORY: {imagen.titulo[1:len(imagen.titulo) - 1]}")
                elif filtro == "DOUBLEMIRROR":
                    if not jpg:
                        html_filtro += f'\n<link rel="stylesheet" href="{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR.css">'
                        html_filtro += '''
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">'''
                    html_filtro += f'''\n<title>{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR</title>
                    </head>
                    <body>'''
                    if not jpg:
                        html_filtro += f'\n<p style="font-family: \'Press Start 2P\'; font-size: 40px; position: absolute; top: 0px;">{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR</p>'
                        html_filtro += '\n<div class="imagen" style="position: relative;">'
                    else:
                        html_filtro += '\n<div class="imagen">'
                    for celda in imagen.matriz_celdas_double:
                        if celda.is_painted:
                            html_filtro += f'\n<div class="pixel" id="x{celda.pos_x}y{celda.pos_y}"></div>'
                            css_filtro += f'\n#x{celda.pos_x}y{celda.pos_y}'
                            css_filtro += ' {'
                            css_filtro += f'''
                                background: {celda.color};'''
                            css_filtro += '\n}'
                        else:
                            html_filtro += '\n<div class="pixel" id="not_painted"></div>'
                    html_filtro += '''
                        </div>
                    </body>
                    </html>'''
                    try:
                        ruta_html = ''
                        if not jpg:
                            ruta_html = f"Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR.html"
                        else:
                            ruta_html = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR.html"
                        imagen_double = open(ruta_html, "w",encoding="utf8")
                        imagen_double.write(html_filtro)
                        imagen_double.close()
                        ruta_css = ''
                        if not jpg:
                            ruta_css = f"Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR.css"
                        else:
                            ruta_css = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR.css"
                        styles_double = open(ruta_css, "w",encoding="utf8")
                        styles_double.write(css_filtro)
                        styles_double.close()
                        imagenes_generadas += 1
                    except Exception:
                        traceback.print_exc()
                        print(f"-> Error en la creación del HTML - CSS de la imagen DOUBLEMIRROR: {imagen.titulo[1:len(imagen.titulo) - 1]}")
                else:
                    print(f"-> {filtro} no es un filtro válido :(.")
        return imagenes_generadas

    def imagenes_programa(self):
        global texto_cargado
        global imagenes_cargadas
        if texto_cargado:
            self.frame3_file = Frame(self.frame3, bg="white")
            self.frame3_file.place(x=0, y=0, relheight=1, relwidth=1)
            lb = Label(self.frame3_file, text="Imagen a mostrar:", font=("Consolas", 14), bg="white")
            lb.place(x=250, y=30)
            titulo_imagen = StringVar(self.frame3_file)
            titulo_imagen.set('Seleccione una imagen')
            titulos_imagenes = []
            for imagen in imagenes_cargadas:
                titulos_imagenes.append(imagen.titulo)
            lista_imagenes = OptionMenu(self.frame3_file, titulo_imagen, *titulos_imagenes)
            lista_imagenes.place(x=450, y=30)
            mostrar_btn = Button(self.frame3_file, text="Mostrar imagen", font=("Consolas", 14), bg="green yellow", command=lambda:[self.mostrar_imagen(titulo_imagen.get())])
            mostrar_btn.place(x=650, y=25)
            self.frame_btn_filtros = Frame(self.frame3_file, bg="white")
            self.frame_btn_filtros.place(x=75, y=100)
            self.btn_original = Button(self.frame_btn_filtros, text="Original", font=("Consolas", 14), bg="aquamarine", state='disabled')
            self.btn_original.pack(pady=10)
            self.btn_mirrorx = Button(self.frame_btn_filtros, text="Mirror X", font=("Consolas", 14), bg="aquamarine", state='disabled')
            self.btn_mirrorx.pack(pady=10)
            self.btn_mirrory = Button(self.frame_btn_filtros, text="Mirror Y", font=("Consolas", 14), bg="aquamarine", state='disabled')
            self.btn_mirrory.pack(pady=10)
            self.btn_double = Button(self.frame_btn_filtros, text="Double Mirror", font=("Consolas", 14), bg="aquamarine", state='disabled')
            self.btn_double.pack(pady=10)
            self.frame_imagenes = Frame(self.frame3_file, bg="gray")
            self.frame_imagenes.place(x=225, y=75, width=700, height=380)
            self.lb_no_imagen = Label(self.frame_imagenes, text="No se ha seleccionado una imagen.", font=("Consolas", 14), bg="gray")
            self.lb_no_imagen.pack(expand=True, fill=BOTH)
    
    def mostrar_imagen(self, titulo_seleccionado):
        print("Titulo seleccionado: " + titulo_seleccionado)
        global imagenes_cargadas
        path_wkthmltoimage = 'C:\Program Files\wkhtmltopdf\\bin\wkhtmltoimage.exe'
        config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)
        for imagen in imagenes_cargadas:
            if imagen.titulo == titulo_seleccionado:
                ruta_html = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]}.html"
                ruta_css = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]}.css"
                ruta_jpg = f"Imagenes JPG/{imagen.titulo[1:len(imagen.titulo) - 1]}.jpg"
                try:
                    img = self.generar_html(imagen, jpg=True)
                    options = {'width': imagen.ancho + 20, 'height': imagen.alto + 20 }
                    imgkit.from_file(ruta_html, ruta_jpg, css=ruta_css, options=options, config=config)
                    if imagen.filtros is not None:
                        for filtro in imagen.filtros:
                            if filtro == "MIRRORX":
                                try:
                                    ruta_html_filtro = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX.html"
                                    ruta_css_filtro = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX.css"
                                    ruta_filtro = f"Imagenes JPG/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX.jpg"
                                    imgkit.from_file(ruta_html_filtro, ruta_filtro, css=ruta_css_filtro, options=options, config=config)
                                except:
                                    traceback.print_exc()
                                    print("-> Error en la conversión de HTML a JPG del fitro MIRRORX de la imagen " + imagen.titulo)
                            elif filtro == "MIRRORY":
                                try:
                                    ruta_html_filtro = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY.html"
                                    ruta_css_filtro = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY.css"
                                    ruta_filtro = f"Imagenes JPG/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY.jpg"
                                    imgkit.from_file(ruta_html_filtro, ruta_filtro, css=ruta_css_filtro, options=options, config=config)
                                except:
                                    traceback.print_exc()
                                    print("-> Error en la conversión de HTML a JPG del fitro MIRRORY de la imagen " + imagen.titulo)
                            elif filtro == "DOUBLEMIRROR":
                                try:
                                    ruta_html_filtro = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR.html"
                                    ruta_css_filtro = f"Imagenes JPG/Imagenes HTML/{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR.css"
                                    ruta_filtro = f"Imagenes JPG/{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR.jpg"
                                    imgkit.from_file(ruta_html_filtro, ruta_filtro, css=ruta_css_filtro, options=options, config=config)
                                except:
                                    traceback.print_exc()
                                    print("-> Error en la conversión de HTML a JPG del fitro DOUBLEMIRROR de la imagen " + imagen.titulo)
                    self.imagen_original_jpg(imagen)
                except:
                    traceback.print_exc()
                    print("-> Error en la conversión de HTML a JPG de la imagen original" + imagen.titulo)
                self.btn_original.config(state="normal", command= lambda:[self.imagen_original_jpg(imagen)])
                self.btn_mirrorx.config(state="normal", command= lambda:[self.imagen_mirrorx_jpg(imagen)])
                self.btn_mirrory.config(state="normal", command= lambda:[self.imagen_mirrory_jpg(imagen)])
                self.btn_double.config(state="normal", command= lambda:[self.imagen_double_jpg(imagen)])
                break
    
    def imagen_original_jpg(self, imagen):
        try:
            ancho_jpg = imagen.ancho + 20
            alto_jpg = imagen.alto + 20
            diferencia_ancho = 0
            diferencia_alto = 0
            if ancho_jpg > 700:
                diferencia_ancho = ancho_jpg - 700 
            if alto_jpg > 380:
                diferencia_alto = alto_jpg - 380
            ruta_jpg = f"Imagenes JPG/{imagen.titulo[1:len(imagen.titulo) - 1]}.jpg"
            imagen_original = Image.open(ruta_jpg)
            if diferencia_ancho != 0 or diferencia_alto != 0:
                if diferencia_ancho > diferencia_alto:
                    new_imagen = ImageTk.PhotoImage(imagen_original.resize((ancho_jpg - diferencia_ancho, alto_jpg - diferencia_ancho), Image.ANTIALIAS))
                    self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                    self.lb_no_imagen.photo = new_imagen
                else:
                    new_imagen = ImageTk.PhotoImage(imagen_original.resize((ancho_jpg - diferencia_alto, alto_jpg - diferencia_alto), Image.ANTIALIAS))
                    self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                    self.lb_no_imagen.photo = new_imagen
            else:
                new_imagen = ImageTk.PhotoImage(imagen_original)
                self.lb_no_imagen.config(bg="white", text="", image=imagen, compound=CENTER)
                self.lb_no_imagen.photo = new_imagen
            imagen_original.close()
        except:
            traceback.print_exc()
    
    def imagen_mirrorx_jpg(self, imagen):
        hay_filtro = False
        if imagen.filtros is not None:
            for filtro in imagen.filtros:
                if filtro == "MIRRORX":
                    hay_filtro = True
                    try:
                        ancho_jpg = imagen.ancho + 20
                        alto_jpg = imagen.alto + 20
                        diferencia_ancho = 0
                        diferencia_alto = 0
                        if ancho_jpg > 700:
                            diferencia_ancho = ancho_jpg - 700 
                        if alto_jpg > 380:
                            diferencia_alto = alto_jpg - 380
                        ruta_jpg = f"Imagenes JPG/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORX.jpg"
                        imagen_original = Image.open(ruta_jpg)
                        if diferencia_ancho != 0 or diferencia_alto != 0:
                            if diferencia_ancho > diferencia_alto:
                                new_imagen = ImageTk.PhotoImage(imagen_original.resize((ancho_jpg - diferencia_ancho, alto_jpg - diferencia_ancho), Image.ANTIALIAS))
                                self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                                self.lb_no_imagen.photo = new_imagen
                            else:
                                new_imagen = ImageTk.PhotoImage(imagen_original.resize((ancho_jpg - diferencia_alto, alto_jpg - diferencia_alto), Image.ANTIALIAS))
                                self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                                self.lb_no_imagen.photo = new_imagen
                        else:
                            new_imagen = ImageTk.PhotoImage(imagen_original)
                            self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                            self.lb_no_imagen.photo = new_imagen
                        imagen_original.close()
                        break
                    except:
                        traceback.print_exc()
        if not hay_filtro:
            self.lb_no_imagen.config(text=f"La imagen {imagen.titulo[1:len(imagen.titulo) - 1]} no posee el filtro Mirror X.", bg="gray", image="")
            self.lb_no_imagen.photo = ""
    
    def imagen_mirrory_jpg(self, imagen):
        hay_filtro = False
        if imagen.filtros is not None:
            for filtro in imagen.filtros:
                if filtro == "MIRRORY":
                    hay_filtro = True
                    try:
                        ancho_jpg = imagen.ancho + 20
                        alto_jpg = imagen.alto + 20
                        diferencia_ancho = 0
                        diferencia_alto = 0
                        if ancho_jpg > 700:
                            diferencia_ancho = ancho_jpg - 700 
                        if alto_jpg > 380:
                            diferencia_alto = alto_jpg - 380
                        ruta_jpg = f"Imagenes JPG/{imagen.titulo[1:len(imagen.titulo) - 1]} - MIRRORY.jpg"
                        imagen_original = Image.open(ruta_jpg)
                        if diferencia_ancho != 0 or diferencia_alto != 0:
                            if diferencia_ancho > diferencia_alto:
                                new_imagen = ImageTk.PhotoImage(imagen_original.resize((ancho_jpg - diferencia_ancho, alto_jpg - diferencia_ancho), Image.ANTIALIAS))
                                self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                                self.lb_no_imagen.photo = new_imagen
                            else:
                                new_imagen = ImageTk.PhotoImage(imagen_original.resize((ancho_jpg - diferencia_alto, alto_jpg - diferencia_alto), Image.ANTIALIAS))
                                self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                                self.lb_no_imagen.photo = new_imagen
                        else:
                            new_imagen = ImageTk.PhotoImage(imagen_original)
                            self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                            self.lb_no_imagen.photo = new_imagen
                        imagen_original.close()
                        break
                    except:
                        traceback.print_exc()
        if not hay_filtro:
            self.lb_no_imagen.config(text=f"La imagen {imagen.titulo[1:len(imagen.titulo) - 1]} no posee el filtro Mirror Y.", bg="gray", image="")
            self.lb_no_imagen.photo = ""
    
    def imagen_double_jpg(self, imagen):
        hay_filtro = False
        if imagen.filtros is not None:
            for filtro in imagen.filtros:
                if filtro == "DOUBLEMIRROR":
                    hay_filtro = True
                    try:
                        ancho_jpg = imagen.ancho + 20
                        alto_jpg = imagen.alto + 20
                        diferencia_ancho = 0
                        diferencia_alto = 0
                        if ancho_jpg > 700:
                            diferencia_ancho = ancho_jpg - 700 
                        if alto_jpg > 380:
                            diferencia_alto = alto_jpg - 380
                        ruta_jpg = f"Imagenes JPG/{imagen.titulo[1:len(imagen.titulo) - 1]} - DOUBLEMIRROR.jpg"
                        imagen_original = Image.open(ruta_jpg)
                        if diferencia_ancho != 0 or diferencia_alto != 0:
                            if diferencia_ancho > diferencia_alto:
                                new_imagen = ImageTk.PhotoImage(imagen_original.resize((ancho_jpg - diferencia_ancho, alto_jpg - diferencia_ancho), Image.ANTIALIAS))
                                self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                                self.lb_no_imagen.photo = new_imagen
                            else:
                                new_imagen = ImageTk.PhotoImage(imagen_original.resize((ancho_jpg - diferencia_alto, alto_jpg - diferencia_alto), Image.ANTIALIAS))
                                self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                                self.lb_no_imagen.photo = new_imagen
                        else:
                            new_imagen = ImageTk.PhotoImage(imagen_original)
                            self.lb_no_imagen.config(bg="white", text="", image=new_imagen, compound=CENTER)
                            self.lb_no_imagen.photo = new_imagen
                        imagen_original.close()
                        break
                    except:
                        traceback.print_exc()
        if not hay_filtro:
            self.lb_no_imagen.config(text=f"La imagen {imagen.titulo[1:len(imagen.titulo) - 1]} no posee el filtro DoubleMirror.", bg="gray", image="")
            self.lb_no_imagen.photo = ""

    def reportes_html(self):
        global texto_cargado
        if texto_cargado:
            self.frame4_file = Frame(self.frame4, bg="white")
            self.frame4_file.place(x=0, y=0, relheight=1, relwidth=1)
            load_img4 = PhotoImage(file="images/html.png")
            load_lb = Label(self.frame4_file, image=load_img4, bg="white")
            load_lb.photo = load_img4
            load_lb.place(x=10, y=40, width=300, height=300)
            title1= Label(self.frame4_file, text="Generando los reportes en formato HTML", font=("Consolas", 20), bg="white")
            title1.place(x=320, y=150)
            tokens_generados = self.reporte_tokens()
            if tokens_generados:
                title1= Label(self.frame4_file, text="Reporte de tokens generado exitosamente.", font=("Consolas", 20), bg="white")
                title1.place(x=320, y=150)                
            else:
                title1= Label(self.frame4_file, text="Fallo en la creación del reporte de Tokens.", font=("Consolas", 20), bg="white")
                title1.place(x=320, y=150)
            errores_generados = self.reporte_errores()
            if errores_generados:
                title2= Label(self.frame4_file, text="Reporte de errores generado exitosamente.", font=("Consolas", 20), bg="white")
                title2.place(x=320, y=190)
            else:
                title2= Label(self.frame4_file, text="Fallo en la creación del reporte de Errores.", font=("Consolas", 20), bg="white")
                title2.place(x=320, y=190)
            try:
                if tokens_generados:
                    webbrowser.open_new(os.path.abspath("Reportes HTML/tokens.html"))
                if errores_generados:
                    webbrowser.open_new(os.path.abspath("Reportes HTML/errores.html"))
            except:
                traceback.print_exc()
                print("->Ocurrió un error al abrir los reportes en el navegador.")
    
    def reporte_tokens(self):
        global tokens_leidos
        html = '''<!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
            <link rel="stylesheet" href="tokens.css" type="text/css" />
            <title>Reporte Tokens</title>
        </head>
        <body>
            <li style="float: left; padding-left: 25%; padding-right: 20px;"><span class="material-icons md-light md-100">generating_tokens</span></li>
            <h1>Reporte de Tokens</h1>
            <div class="datos-reporte">
                <div class="tabla-tokens">
                    <table class="table table-striped table-hover">
                        <thead style="background-color: black; color: white;">
                            <tr>
                            <th scope="col">#</th>
                            <th scope="col">Id Token</th>
                            <th scope="col">Token</th>
                            <th scope="col">Lexema</th>
                            <th scope="col">Fila</th>
                            <th scope="col">Columna</th>
                            </tr>
                        </thead>
                        <tbody>'''
        token_agregado = 0
        id_fila = ""
        for token in tokens_leidos:
            token_agregado += 1
            id_fila = "uno" if token_agregado % 2 == 1 else "dos"
            html += f'''\n<tr id="{id_fila}">
            <th scope="row">{token_agregado}</th>
            <td>{token.id_token}</td>
            <td>{token.nombre}</td>
            <td>{token.lexema}</td>
            <td>{token.fila}</td>
            <td>{token.columna}</td>
            </tr>'''
        html += '''\n</tbody>
                    </table>
                </div>
            </div>
            <footer>
                <p>Elías Abraham Vasquez Soto - 201900131</p>
                <p>Proyecto 1 - Laboratorio Lenguajes Formales y de Programación B-</p>        
                <img src="images/logo_usac.png" width="220" height="60"/>
            </footer>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        </body>
        </html>'''
        css = '''html {
            min-height: 100%;
            position: relative;
        }

        body {
            background-color:rgb(1, 11, 26);
            padding-top: 20px;
            margin-bottom: 150px;
        }

        /* ===== Iconos de Google ===== */
        /* Rules for sizing the icon. */
        .material-icons.md-24 { font-size: 24px; }
        .material-icons.md-30 { font-size: 30px; }
        .material-icons.md-100 { font-size: 100px; }
        /* Rules for using icons as black on a light background. */
        .material-icons.md-dark { color: rgba(0, 0, 0, 0.54); }
        .material-icons.md-dark.md-inactive { color: rgba(0, 0, 0, 0.26); }
        /* Rules for using icons as white on a dark background. */
        .material-icons.md-light { color: rgba(255, 255, 255, 1); }
        .material-icons.md-light.md-inactive { color: rgba(255, 255, 255, 0.3); }

        h1 {
            color: white;
            font-family: 'Lato', sans-serif;
            font-size: 75px;
        }

        .datos-reporte {
            background-color: rgb(255, 255, 255);
            padding-top: 20px;
            padding-bottom: 20px;
            padding-left: 50px;
            margin: 30px 100px 30px 100px;
        }

        .tabla-tokens {
            padding-top: 20px;
            padding-left: 20px;
            padding-right: 40px;
            text-align: center;
            font-family: 'Lato', sans-serif;
            font-size: 20px;
            letter-spacing: 1px;
        }

        table td{    
            color: white;
        }

        table th{    
            color: white;
        }

        #uno {
            background-color: rgb(61, 57, 48);
        }

        #dos {
            background-color: rgb(54, 1, 1);
        }

        footer {
            color: white;
            line-height: 10px;
            text-align: center;
            padding-top: 20px;
            padding-bottom: 5px;
            font-size: 15px;
            font-family: 'Lato', sans-serif;
            position: absolute;
            bottom: 0;
            width: 100%;
            background-image: url("images/footer.png");
        }'''
        try:
            reporte_tokens = open("Reportes HTML/tokens.html", "w",encoding="utf8")
            reporte_tokens.write(html)
            reporte_tokens.close()
            print("->HTML Tokens generado")
            css_tokens = open("Reportes HTML/tokens.css", "w",encoding="utf8")
            css_tokens.write(css)
            css_tokens.close()
            print("->CSS Tokens generado")
            return True
        except:
            traceback.print_exc()
            return False

    def reporte_errores(self):
        global errores_encontrados
        html = '''<!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
            <link rel="stylesheet" href="errores.css" type="text/css" />
            <title>Reporte Errores</title>
        </head>
        <body>
            <li style="float: left; padding-left: 25%; padding-right: 20px;"><span class="material-icons md-light md-100">error</span></li>
            <h1>Reporte de Errores</h1>
            <div class="datos-reporte">
                <div class="tabla-errores">
                    <table class="table table-striped table-hover">
                        <thead style="background-color: black; color: white;">
                            <tr>
                            <th scope="col">#</th>
                            <th scope="col">Caracter</th>
                            <th scope="col">Descripcion</th>
                            <th scope="col">Fila</th>
                            <th scope="col">Columna</th>
                            </tr>
                        </thead>
                        <tbody>'''
        error_agregado = 0
        id_fila = ""
        for error in errores_encontrados:
            error_agregado += 1
            id_fila = "uno" if error_agregado % 2 == 1 else "dos"
            html += f'''\n<tr id="{id_fila}">
            <th scope="row">{error_agregado}</th>
            <td>{error.caracter}</td>
            <td>{error.descripcion}</td>
            <td>{error.fila}</td>
            <td>{error.columna}</td>
            </tr>'''
        html += '''\n</tbody>
                    </table>
                </div>
            </div>
            <footer>
                <p>Elías Abraham Vasquez Soto - 201900131</p>
                <p>Proyecto 1 - Laboratorio Lenguajes Formales y de Programación B-</p>        
                <img src="images/logo_usac.png" width="220" height="60"/>
            </footer>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        </body>
        </html>'''
        css = '''html {
            min-height: 100%;
            position: relative;
        }

        body {
            background-color:rgb(54, 1, 1);
            padding-top: 20px;
            margin-bottom: 150px;
        }

        /* ===== Iconos de Google ===== */
        /* Rules for sizing the icon. */
        .material-icons.md-24 { font-size: 24px; }
        .material-icons.md-30 { font-size: 30px; }
        .material-icons.md-100 { font-size: 100px; }
        /* Rules for using icons as black on a light background. */
        .material-icons.md-dark { color: rgba(0, 0, 0, 0.54); }
        .material-icons.md-dark.md-inactive { color: rgba(0, 0, 0, 0.26); }
        /* Rules for using icons as white on a dark background. */
        .material-icons.md-light { color: rgba(255, 255, 255, 1); }
        .material-icons.md-light.md-inactive { color: rgba(255, 255, 255, 0.3); }


        h1 {
            color: white;
            font-family: 'Lato', sans-serif;
            font-size: 75px;
        }

        .datos-reporte {
            background-color: rgb(255, 255, 255);
            padding-top: 20px;
            padding-bottom: 20px;
            padding-left: 50px;
            margin: 30px 100px 30px 100px;
        }

        .tabla-errores {
            padding-top: 20px;
            padding-left: 20px;
            padding-right: 40px;
            text-align: center;
            font-family: 'Lato', sans-serif;
            font-size: 20px;
            letter-spacing: 1px;
        }

        table td{    
            color: white;
        }

        table th{    
            color: white;
        }

        #uno {
            background-color: rgb(61, 57, 48);
        }

        #dos {
            background-color: rgb(9, 2, 41);
        }

        footer {
            color: white;
            line-height: 10px;
            text-align: center;
            padding-top: 20px;
            padding-bottom: 5px;
            font-size: 15px;
            font-family: 'Lato', sans-serif;
            position: absolute;
            bottom: 0;
            width: 100%;
            background-image: url("images/footer.png");
        }'''
        try:
            reporte_errores = open("Reportes HTML/errores.html", "w",encoding="utf8")
            reporte_errores.write(html)
            reporte_errores.close()
            print("->HTML Errores generado")
            css_errores = open("Reportes HTML/errores.css", "w",encoding="utf8")
            css_errores.write(css)
            css_errores.close()
            print("->CSS Errores generado")
            return True
        except:
            traceback.print_exc()
            return False

if __name__ == '__main__':
    ventana = Tk()
    app = Interfaz(ventana)
    ventana.mainloop()