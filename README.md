# Bitxelart app
### Nombre
Elías Abraham Vasquez Soto
### Carnet
201900131
### Sección
LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION Sección B-
### Descripción
Aplicación de escritorio desarrollada en Python, que genera imágenes digitales en estilo pixel art, procesando archivos de texto .pxla con las características de las imágenes (color, dimensiones, etc) mediante un analizador léxico.

**Formato del archivo**:

```
TITULO="Pokebola";
ANCHO=300;
ALTO=300;
FILAS=12;
COLUMNAS=12;
CELDAS = {
[0,0,FALSE,#000000],
[0,1,FALSE,#000000],
[3,3,FALSE,#000000],
[3,4,TRUE,#000000],
[3,5,TRUE,#000000],
[3,6,TRUE,#000000],
[3,7,TRUE,#000000],
[4,1,FALSE,#000000]
};
FILTROS = MIRRORX;
@@@@
TITULO="Estrella";
ANCHO=300;
ALTO=300;
FILAS=4;
COLUMNAS=4;
CELDAS = {
[0,0,FALSE,#000000],
[1,1,FALSE,#000000],
[3,3,FALSE,#000000],
[2,1,FALSE,#000000]
};
FILTROS = MIRRORX,MIRRORY,DOUBLEMIRROR;
```
