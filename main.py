from tkinter import *
from tkinter import filedialog
from clases import Token, Imagen, Celda, Error
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
errores_encontrados = []
texto_doc = ""
texto_cargado = False
name_archivo_actual = ""

class Interfaz:
    def __init__(self, ventana):
        self.window = ventana
        self.window.title('Bixelart')        
        self.window.state('zoomed')
        
        imagen = PhotoImage(file = "images/fondo.png")
        fondo = Label(self.window, image = imagen, bg="white")
        fondo.photo = imagen
        fondo.place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.window, text="Bixelart App", font=("Consolas", 60, "bold"), bg="white")
        title.place(x=500, y=70)

        self.frame4 = LabelFrame(self.window,bg="white", text="Reportes")
        self.frame4_no_file = Frame(self.frame4, bg="white")
        self.frame4_no_file.place(x=0, y=0, relheight=1, relwidth=1)
        load_img4 = PhotoImage(file="images/sad.png")
        load_lb4 = Label(self.frame4_no_file, image=load_img4, bg="white")
        load_lb4.photo = load_img4
        load_lb4.place(x=10, y=40, width=300, height=300)
        title1= Label(self.frame4_no_file, text="No se ha cargado ningún archivo al programa.", font=("Consolas", 20), bg="white")
        title1.place(x=320, y=150)

        self.frame3 = LabelFrame(self.window,bg="white", text="Imágenes")
        self.frame3_no_file = Frame(self.frame3, bg="white")
        self.frame3_no_file.place(x=0, y=0, relheight=1, relwidth=1)
        load_img3 = PhotoImage(file="images/sad.png")
        load_lb3 = Label(self.frame3_no_file, image=load_img3, bg="white")
        load_lb3.photo = load_img3
        load_lb3.place(x=10, y=40, width=300, height=300)
        title1= Label(self.frame3_no_file, text="No se ha cargado ningún archivo al programa.", font=("Consolas", 20), bg="white")
        title1.place(x=320, y=150)

        self.frame2 = LabelFrame(self.window,bg="white", text="Analizar Archivo")
        self.frame2_no_file = Frame(self.frame2, bg="white")
        self.frame2_no_file.place(x=0, y=0, relheight=1, relwidth=1)
        load_img2 = PhotoImage(file="images/sad.png")
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
            frame.place(x=250, y=280, width=1050, height=420)

        frame_btn = Frame(self.window, bg="white")
        frame_btn.place(x=300, y=200)

        self.cargar_btn = Button(frame_btn, text="Cargar Archivo", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame1.tkraise(), self.abrirArchivo()])
        self.cargar_btn.grid(row=0, column=0, padx=20)

        self.analizar_btn = Button(frame_btn, text="Analizar Archivo y\ngenerar HTML", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame2.tkraise()])
        self.analizar_btn.grid(row=0, column=1, padx=20)

        self.imagenes_btn = Button(frame_btn, text="Imagenes", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame3.tkraise()])
        self.imagenes_btn.grid(row=0, column=2, padx=20)

        self.reportes_btn = Button(frame_btn, text="Ver Reportes HTML", font=("Consolas", 15), bg="light sea green", command = lambda:[self.frame4.tkraise()])
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
                title3= Label(self.frame_file, text="Archivo analizado exitosamente.", font=("Consolas", 20), bg="white")
                title3.place(x=320, y=190)
                print("\nTOKENS:")
                for x in tokens_leidos:
                    print(x.nombre, "FILA:", str(x.fila), "COLUMNA:", str(x.columna), "LEXEMA:", x.lexema)
                print("\nERRORES:")
                for y in errores_encontrados:
                    print(y.caracter, y.descripcion, "FILA:", str(y.fila), "COLUMNA:", str(y.columna))
                print("->Análisis finalizado con éxito")
            except Exception as ex:
                print(ex)
                title3= Label(self.frame_file, text="Ocurrió un error en el analizador léxico :(", font=("Consolas", 20), bg="white")
                title3.place(x=320, y=190)
                print("-> Ocurrió un error en el analizador léxico.")
            archivo.close()
            
        except Exception as e:
            print(e)
            print("->No se seleccionó un archivo")
    
    def is_ascii(self, caracter):
        if ord(caracter) == 32 or ord(caracter) == 33 or (ord(caracter) >= 35 and ord(caracter) <= 126) or ord(caracter) == 130 or (ord(caracter) >= 160 and ord(caracter) <= 165):
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
                                if sections == 6:
                                    # TODO Imagen sin filtros
                                    sections = 0
                                    lexema_actual += caracter
                                    estado_file = "a2"
                                else:
                                    # TODO Faltan secciones de imagen o hubo error en el Separador
                                    sections = 0
                                    lexema_actual += caracter
                                    estado_file = "a2"
                            elif caracter == "$":
                                for tkn in tokens:
                                    tkn.reinicio_token()
                                # TODO Fin del archivo
                                if sections == 6:
                                    # TODO Imagen sin filtros
                                    pass
                                else:
                                    # TODO Faltan secciones de imagen
                                    pass
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
                                estado_sec = "c85"
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                pass
                            else:
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
                                lexema_actual = ""
                                estado_sec = "c37"
                            elif caracter == "Y":
                                lexema_actual += caracter
                                new_token += 1
                                m_y = Token(9, "MirrorY", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(m_y)
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
                            elif ord(caracter) == 9 or ord(caracter) == 10 or ord(caracter) == 32:
                                lexema_actual += caracter
                                estado_sec = "c82.5"
                            elif caracter == "]":
                                lexema_actual += caracter
                                new_token += 1
                                cell = Token(15, "Celda", numero=new_token, lexema=lexema_actual, fila=fila, columna=columna-(len(lexema_actual)-1))
                                tokens_leidos.append(cell)
                                lexema_actual = ""
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
                        lexema_actual = ""
                        estado_file = "a0"
                elif estado_file == "a2":
                    if caracter == "@":
                        lexema_actual += caracter
                        estado_file = "a3"
                    else:
                        new_error += 1
                        e_arroba = Error(new_error, caracter, "Se esperaba el segundo '@' del token 'Separador'.", fila, columna-(len(lexema_actual)-1))
                        errores_encontrados.append(e_arroba)
                        lexema_actual = ""
                        estado_file = "a0"
                elif estado_file == "a3":
                    if caracter == "@":
                        lexema_actual += caracter
                        estado_file = "a4"
                    else:
                        new_error += 1
                        e_arroba = Error(new_error, caracter, "Se esperaba el tercer '@' del token 'Separador'.", fila, columna-(len(lexema_actual)-1))
                        errores_encontrados.append(e_arroba)
                        lexema_actual = ""
                        estado_file = "a0"
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
                        estado_file = "a0"
        else:
            pass

if __name__ == '__main__':
    ventana = Tk()
    app = Interfaz(ventana)
    ventana.mainloop()