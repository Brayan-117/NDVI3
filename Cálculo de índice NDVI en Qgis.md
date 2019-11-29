# Cálculo de índice NDVI en Qgis

# Resumen

En este proyecto se pretende elaborar un programa capaz de indicar el ìndice de vegetaciones 
por me-dio de imágenes satelitales obtenidas de la plata-forma glovis de la cual sacaremos 
las imágenes necesarias para llevar acabo nuestro proyecto.

Realizaremos este programa con la finalidad de
analizar datos ecológicos y así poder detectar la
vegetación que se encuentra en cierta región. 
Para realizar este programa utilizaremos Python
en el cual realizaremos nuestro código fuente y
haremos utilización de algunas de sus librerías
como lo son gdal y prossesing incluidos módulos de osgeos y os entre algunas otras.  

Palabras clave: Vegetación, Python, glovis, gdal, 
osgeo.

# Abstract
This project aims to develop a program capable of
indicating the index of vegetations by means of sat-ellite
images obtained from the glovis platform from
which we will obtain the necessary images to carry
out our project. We will carry out this program in order to analyse ecological data and thus be able to detect the vegetation found in a certain region.

To make this program we will use python in which we
will make our source code and we will use some of its
libraries such as os, osgeo, gdal among some oth-ers..

Keywords: Article template. Author’s instructions.

# Introducción
Dentro de este proyecto se presenta el cálculo
automatizado del índice de índice de vegetación
(NDVI) mediante un programa realizado en el
lenguaje de programación Python en su versión
3.7. Según la página web GIDAHATARI, “Los
índices de vegetación se calculan a partir de las
radiancias de las plantas en ciertos rangos del
espectro visible e invisible. Curiosamente la
vegetación tiene una mayor radiancia en el rojo
y el infrarrojo que en el azul.” (gidahatari.com,
2017).
También el sitio web nos menciona que “existen
varios índices de vegetación en base de diferen-tes fórmulas de combinación de bandas, dentro
de estos índices el más conocido es el NDVI, ya
que fue uno de los primeros en formularse y
porque puede ser aplicado a una serie de satéli-tes nuevos y antiguos” (gidahatari.com,
2017).

El propósito del proyecto es agilizar el cálculo
del índice de vegetación mediante un software
que sea útil tanto para uso público como para
uso escolar y por ende para futuros levanta-mientos que sean necesarios. Por otro lado, el
objetivo del cálculo del índice de vegetación es
estimar la cantidad, calidad y desarrollo de la
vegetación con base a la medición de la inten-sidad de la radiación de ciertas bandas del es-pectro electromagnético que la vegetación emi-te o refleja

# Desarrollo

## Librerias

### GDAL
Los modulos que tiene gdal nos sirve para abrir la imagen y ver los modulos, además nos ayu-da a leer los datos de las bandas y después de ello convierte los datos a puntos flotantes, lo cual nos ayudará a facilitar el cálculo de Índice de Vegetación
GDAL significa Geospatial Data Abstraction Library.

Es una biblioteca de software para la lectura y escritura de formatos de datos geoespaciales publicada bajo la MIT License por la Fundación OSGeo. Con esta librería se pueden realizar multitud de operaciones de transformación y procesamiento sobre gran variedad de datos ráster y vectoriales. La librería GDAL es utilizada por gran número de paquetes geomáticos como por ejemplo QGIS, gvSIG o ESRI ArcGIS. Des-de los menús de cualquiera de estos clientes SIG podemos acceder a las funciones de GDAL utilizando los formularios diseñados para ello.

GDAL tiene como función leer y escribir datos provenientes de ráster geoespaciales además realiza otras funciones como exportar imáge-nes, transformar formatos, reproyectar datos, hacer mosaicos de datos entre otras cosas.
Una de las funciones que tiene gdal es instalar el controlador de errores que captura el error, la clase el mensaje GDAL.

Encontrará los datos de la demo en /usr/local/share/data. Queremos echar un vista-zo a Natural Earth data en este inicio rápido. Queremos trabajar con una copia de los datos. Así que el primer paso es copiar los datos en su directorio home.

![Palabras Del Texto Alternativo](https://github.com/Brayan-117/NDVI3/blob/master/imagenes/f1.jpg)
Figura 1. Datos en directorio Home

Entonces encontrará un archivo ráster de Natu-ralEarth y un .tfw World-file at:

![Palabras Del Texto Alternativo](https://github.com/Brayan-117/NDVI3/blob/master/imagenes/f2.png) 
Figura 2. Archivo Raster

![Palabras Del Texto Alternativo](https://github.com/Brayan-117/NDVI3/blob/master/imagenes/f3.jpg)
Figura 3. Dato Interesante

Generalmente los usuarios de esta librería son cartógrafos en ingenieros que estén involucra-dos en el manejo de datos geoespaciales, claro que también puedem manejarlo estudiantes que los necesiten.

### Processing

En nuestro programa utilizamos processing para calcular el NDVI

Processing es una biblioteca gráfica de código abierto y un entorno de desarrollo integrado (IDE) creado para las comunidades de artes electrónicas, nuevos medios y diseño visual con el propósito de enseñar a los no programa-dores los fundamentos de la programación de computadoras en un contexto visual.

La interfaz de Processing es muy sencilla debi-do a que ésta funciona principalmente como un editor de texto, que nos servira para compilar el código de los programas que escribamos. es desarrollado por artistas y diseñadores como una herramienta alternativa al software propieta-rio.

El primer paso consiste en descargar las libre-rías de Processing.js, para lo cual basta con acceder a la página de descargas del frame-work: http://processingjs.org/download

Podemos obtener un zip con varios archivos, incluido el propio framework, otro zip con varios ejemplos o el archivo .js suelto en dos formas, normal y minimizado. En el momento de escribir este artículo están en la versión 1.1.0, con lo que el archivo para poner en marcha Proces-sing.js se llama "processing-1.1.0.js" y el mini-mizado se llama "processing-1.1.0.min.js". Cualquiera de esas dos opciones servirá para comenzar, aunque en etapa de desarrollo intere-sa utilizar el archivo completo y en etapa de producción el minimizado.


### Opción 1) Usar el lenguaje Processing

La primera posibilidad que nos proponen es trabajar con el lenguaje Processing, que opina-mos estaría bien para aquellas personas que tengan experiencia previa en ese lenguaje de programación.
Esta manera de trabajar con Processing.js la explicamos en el artículo usar Processing.js mediante el lenguaje Processing.

### Opción 2) Usar código nativo Javascript

La segunda posibilidad es escribir directamente código Javascript nativo, haciendo uso del objeto Processing, que implementa el frame-work. Esta segunda opción será propia para las personas que ya tenga experiencia en Ja-vascript y no vean la necesidad o no deseen aprender un nuevo lenguaje.

Esta otra manera de trabajar con Processing la explicaremos en el artículo usando Proces-sing.js mediante Javascript.

Sirve como medio para la enseñanza y produc-ción de proyectos multimedia e interactivos de diseño digital. Por lo tanto, los usuarios pueaquellos que proyectos digitales y presen-taciones multimedia.

## Metodología

La estructura de nuestro proyecto es un tanto técnica, por lo cual ilustraremos cada uno de los pasos (procesos que realizamos) con su respectiva descripción y funcionamiento, eso hará que se pueda replicar nuestro programa para beneficio escolar, laboral o social.

1.	Primeramente, necesitamos importar los módulos y las librerías necesarias:    
 
![Palabras Del Texto Alternativo](https://github.com/Brayan-117/NDVI3/blob/master/imagenes/f4.png)
Figura 4. Importación de módulos y librerías

2.	A continuación, con la extensión os.chdir, le diremos que abra el directorio donde tendremos almacenadas nuestras imágenes, y con el os.listdir y os.getcwd  vamos a imprimir las listas de las bandas.  

![Palabras Del Texto Alternativo](https://github.com/Brayan-117/NDVI3/blob/master/imagenes/f5.jpg)
Figura 5. Listado de datos

3.	Ahora cargaremos las bandas, comenzaremos por la ROJA y la NIR (infrarojo), que hacemos con esto, leer el directorio donde tenemos las capas (bandas) y añadirlas con el comando iface.addRasterLayer.
 
![Palabras Del Texto Alternativo](https://github.com/Brayan-117/NDVI3/blob/master/imagenes/f6.jpg)
Figura 6. Cargado de Capas

4.	Por consiguiente, importamos el complemento de procesos que es prosessing, con ello tomará las variables NIR y RED para la calculadora de RASTERS.

Posteriormente agregamos la formula del calculo del NVDI con su respectiva variable:(NIR-RED) / (NIR+RED).
 
![Palabras Del Texto Alternativo](https://github.com/Brayan-117/NDVI3/blob/master/imagenes/f7.jpg)
Figura 7. Uso de Prosessing

Esto nos arrojará el resultado de las capas, las que no están aparecerán como <none>. Luego para agregar el cálculo del NVDI al mapa de Qgis como un raster usamos la siguiente línea de código:
 
![Palabras Del Texto Alternativo](https://github.com/Brayan-117/NDVI3/blob/master/imagenes/f8.jpg
Figura 8. Código de creación del mapa

Con ello ya se finaliza el proceso y se agregará automáticamente en nuestro mapa

# Manejo de datos

1.	Datos en el programa.

Para este programa se utilizaron las bandas Senitel-2 de 10 metros, las cuales son el rojo, azul, verde e infrarrojo. Estas bandas se utiliza-ron para realizar el cálculo de NDVI.

![Palabras Del Texto Alternativo](https://github.com/Brayan-117/NDVI3/blob/master/imagenes/f9.jpg)
Figura 9. Bandas satélite Senitel-2

2.	Sistema Operativo.

En el sistema operativo en el que ha funcionado el programa es Windows, pero se tiene contem-plado que funcione para los demás sistemas operativos.

3.	Programas y/o herramientas.

Dentro de QGIS se utilizaron las herramientas de Python para la realización del programa.

# Conclusiones

### Brayan Aguilar: 
Es notorio el funcionamiento del programa expuesto, por el momento solo se han hecho pruebas en el sistema operativo de Windows, específicamente en la versión 10. Al ver los resultados del programa se puede dar por hecho que nuestros objetivos fueron cumplidos, se manifiesta la conformi-dad del poder brindar apoyo con el programa mencionado a ingenieros y cartógrafos que lo necesiten y no solo eso, puede ser útil para todas las personas que lo requieran.
### Sarahí Ramírez: 
Cabe señalar que fue un ver-dadero reto el desarrollo del proyecto, ya que en innumerables ocasiones tuvieron que ha-cerse correcciones al código para que pudie-se correr con normalidad y funcional. Se re-calca que está satisfecho con los resultados que ha arrojado el programa.
### Gilberto Hdez: 
Como se puede apreciar en el desarrollo del proyecto nuestro programa es funcional, así que podemos dar por hecho que es totalmente optimo e incluso podría decir que compatible con cualquier sistema operativo (Windows, ¡Os, Unix, etc.), además de que el código es fácil de entender y opti-mo, se podría decir que lo más complejo de la ejecución del programa fue conseguir las imágenes satelitales con las que estuvimos haciendo las pruebas de este, además de unas pequeñas correcciones que le tuvimos que hacer a nuestro código para lograr que este cumpliera con nuestros objetivos.

# Bibliografías

Gidahatari. (2017). Calculo de Indice de Vegetación NDVI de Imágenes Sentinel 2 con Python en QGIS (PyQGIS). Recuperado de: http://gidahatari.com/ih-es/calculo-de-indice-de-vegetacion-ndvi-de-imagenes-sentinel-2-con-python-en-qgis-pyqgis

Landmao. (2015). 9.4 Calculate NDVI using GDAL. Recuperado de: http://learningzone.rspsoc.org.uk/index.php/Learning-Materials/Python-Scripting/9.4-Calculate-NDVI-using-GDAL

Neon. (2018). Calculate NDVI & Extract Spectra Using Masks in Python - Flightline Data Recuperado de: https://www.neonscience.org/calc-ndvi-py


