# parcial-1-labo
### 📄Documentación de la Laboratorio - UTN Tecnicatura Superior en Programación.

### Nombre: Bosco Mascaro Massimo Ariel

### **Laboratorio**

![TETRIS](https://github.com/magikboy/parcial-1-labo/blob/5feeefcec0e5d43faea89a4e8e41ba442be24bd4/maxresdefault.jpg)

### VIDEOJUEGO TETRIS 🎮

## 📄Consigna del juego:
Pygame :TETRIS
Especificaciones mínimas:

Los bloques solamente deberán ser de 4 formas:

✔Rectángulo

✔Cuadrado

✔Forma de T

✔Forma de L

-Cada bloque deberá aparecer de manera aleatoria, es decir no debe haber
un orden entre un tipo de elemento y el que le sigue.
-Cada partida debe ser por tiempo o hasta no poder realizarse más
movimientos.

-Mientras el bloque va bajando, no se puede volver a subir. Una vez que
bajó totalmente no se puede mover hacia ningún lado.

-Al final de cada partida se deberá guardar el SCORE junto con el nombre
de usuario. En tal sentido, se deberá elaborar un ranking ordenado de
mayor a menor puntuación, mostrando su respectivo nombre y puntuación.

Incluir.

✔Archivos.

✔POO.

✔Texto para ir mostrando el SCORE.

✔Eventos.

✔Colisiones.

✔Manejo de rectángulo.

✔Temporizador.

✔Imágenes.

✔Audios.

✔Ranking de puntuaciones

### Juego en funcionamiento 🎮

![juego](https://github.com/magikboy/parcial-1-labo/blob/87a4a8c16ee519fa5bf10b87d742671d097eeb67/2023-06-19-00-42-24.gif)


### 🚀ejercutable del proyecto y menus
``` py
import pygame
import sys
import sqlite3
from juego import Juego
from colores import Colores
import time

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('puntuacion\dtetris_scores.db')

# Crear la tabla de puntuaciones si no existe
conn.execute('''CREATE TABLE IF NOT EXISTS scores
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                score INTEGER)''')

# Función para insertar una puntuación en la base de datos
def insert_score(username, score):
    # Verificar si el nombre del jugador ya existe en la base de datos
    cursor = conn.execute("SELECT score FROM scores WHERE username = ?", (username,))
    existing_score = cursor.fetchone()

    if existing_score is None or score > existing_score[0]:
        # El nombre del jugador no existe o la nueva puntuación es mayor
        if existing_score is None:
            # Insertar una nueva fila en la tabla
            conn.execute("INSERT INTO scores (username, score) VALUES (?, ?)", (username, score))
        else:
            # Actualizar la puntuación existente
            conn.execute("UPDATE scores SET score = ? WHERE username = ?", (score, username))
        conn.commit()

# Función para obtener el usuario con el puntaje máximo
def get_top_score_user():
    cursor = conn.execute("SELECT username, MAX(score) FROM scores")
    return cursor.fetchone()

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana del juego
ALTO = 620
ANCHO = 500

# Fuente para el título
font_titulo = pygame.font.Font("font\dfont.ttf", 25)

# Superficies de texto para mostrar en la pantalla
superficie_puntaje = font_titulo.render("Puntaje", True, Colores.blanco)
superficie_siguiente = font_titulo.render("Siguiente", True, Colores.blanco)
superficie_fin_juego = font_titulo.render("GAME OVER", True, Colores.rojo)
superficie_opcion_jugar = font_titulo.render("Iniciar juego", True, Colores.blanco)
superficie_opcion_puntuaciones = font_titulo.render("Puntuaciones", True, Colores.blanco)
superficie_opcion_salir = font_titulo.render("Salir", True, Colores.blanco)
opcion_salir = font_titulo.render("Esc para salir", True, Colores.blanco)
opcion_continuar = font_titulo.render("Esp para reiniciar", True, Colores.blanco)
mejor_punt = font_titulo.render("Mejor:", True, Colores.blanco)

# Rectángulos para los elementos en la pantalla
rect_puntaje = pygame.Rect(330, 55, 150, 60)
rect_siguiente = pygame.Rect(330, 215, 150, 180)

# Crear la ventana del juego
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Segundo Parcial: Tetris")

# Cargar y redimensionar el fondo de pantalla
fondo = pygame.image.load("fondo\dfondo4.png").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Establecer el reloj para limitar la velocidad de actualización de la pantalla
reloj = pygame.time.Clock()

# Crear una instancia del juego
juego = Juego()

# Obtener el nombre del jugador
nombre_jugador = ""

# Función para mostrar la ventana de ingreso de nombre
def mostrar_ventana_nombre():
    global nombre_jugador
    fondo = pygame.image.load("fondo\dnombre1.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    nombre_ingresado = False

    while not nombre_ingresado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    nombre_ingresado = True
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_BACKSPACE:
                    nombre_jugador = nombre_jugador[:-1]
                else:
                    nombre_jugador += evento.unicode
            
        pantalla.blit(fondo, (0, 0))
        texto_ingreso = font_titulo.render("Ingresa tu nombre:", True, Colores.blanco)
        enter = font_titulo.render("Ent para continuar", True, Colores.blanco)
        texto_nombre = font_titulo.render(nombre_jugador, True, Colores.blanco)
        pantalla.blit(texto_ingreso, (70, 150))
        pantalla.blit(texto_nombre, (70, 240))
        pantalla.blit(enter, (120, 510))
        pygame.display.update()

# Obtener el usuario con el puntaje máximo
top_score_user = get_top_score_user()

# Evento personalizado para actualizar el juego
ACTUALIZAR_JUEGO = pygame.USEREVENT
pygame.time.set_timer(ACTUALIZAR_JUEGO, 200)

# Función para mostrar la tabla de puntuaciones
def mostrar_tabla_puntuaciones():
    fondo = pygame.image.load("fondo\dfondo3.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    opcion_salir2 = font_titulo.render("Esc para volver", True, Colores.blanco)
    top = font_titulo.render("Puntuaciones: ", True, Colores.blanco)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

        pantalla.blit(fondo, (0, 0))
        pantalla.blit(opcion_salir2, (140, 540, 50, 50))
        pantalla.blit(top, (130, 120, 50, 50))
        # Obtener los datos de la tabla de puntuaciones desde la base de datos
        cursor = conn.execute("SELECT username, score FROM scores ORDER BY score DESC LIMIT 5")
        puntuaciones = cursor.fetchall()

        # Mostrar los datos en la pantalla
        y = 210
        for i, puntuacion in enumerate(puntuaciones):
            texto_puntuacion = font_titulo.render(f"{i+1}. {puntuacion[0]}: {puntuacion[1]}", True, Colores.blanco)
            pantalla.blit(texto_puntuacion, (135, y))
            y += 40

        pygame.display.update()

# Función para mostrar el menú
def mostrar_menu():
    fondo = pygame.image.load("fondo\menu2.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Obtener la posición del cursor del mouse al hacer clic
                x, y = pygame.mouse.get_pos()
                if 160 < x < 300 and 160 < y < 230:  # Opción 1: Iniciar juego
                    juego.reiniciar()
                    return
                elif 110 < x < 350 and 280 < y < 330:  # Opción 2: Ver tabla de puntuaciones
                    mostrar_tabla_puntuaciones()
                elif 200 < x < 250 and 370 < y < 430:  # Opción 3: Salir
                    pygame.quit()
                    sys.exit()

        pantalla.blit(fondo, (0, 0))
        # Dibujar las opciones del menú en la pantalla
        pantalla.blit(superficie_opcion_jugar, (160, 190, 50, 50))
        pantalla.blit(superficie_opcion_puntuaciones, (150, 295, 50, 50))
        pantalla.blit(superficie_opcion_salir, (220, 405, 50, 50))
        pygame.display.update()

# Mostrar el menú antes del juego
mostrar_menu()
# Mostrar la ventana de ingreso de nombre
mostrar_ventana_nombre()

# Bucle principal del juego
tiempo_inicio = time.time()
while True:
    for evento in pygame.event.get():
        # Verificar si se ha cerrado la ventana
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Verificar si se ha presionado una tecla
        if evento.type == pygame.KEYDOWN:
            # Verificar si el juego ha terminado
            if juego.fin_juego == True:
                # Verificar si se ha presionado la tecla espaciadora
                if evento.key == pygame.K_SPACE:
                    # Insertar el puntaje en la base de datos
                    insert_score(nombre_jugador, juego.puntaje)
                    # Obtener el usuario con el puntaje máximo
                    top_score_user = get_top_score_user()
                    print("Usuario con el puntaje máximo:")
                    print(f"{top_score_user[0]}: {top_score_user[1]}")
                    # Reiniciar el juego
                    juego.fin_juego = False
                    juego.reiniciar()
                # Verificar si se ha presionado la tecla de escape
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # Verificar otras teclas presionadas si el juego no ha terminado
            elif evento.key == pygame.K_LEFT and juego.fin_juego == False:
                juego.mover_izquierda()
            elif evento.key == pygame.K_RIGHT and juego.fin_juego == False:
                juego.mover_derecha()
            elif evento.key == pygame.K_DOWN and juego.fin_juego == False:
                juego.mover_abajo()
                juego.actualizar_puntaje(0, 1)
            elif evento.key == pygame.K_UP and juego.fin_juego == False:
                juego.rotar()
        # Verificar si se ha activado el evento personalizado ACTUALIZAR_JUEGO
        if evento.type == ACTUALIZAR_JUEGO and juego.fin_juego == False:
            juego.mover_abajo()

    # Dibujar los elementos en la pantalla
    pantalla.blit(fondo, (0, 0))

    tiempo_transcurrido = time.time() - tiempo_inicio
    minutos = int(tiempo_transcurrido // 60)
    segundos = int(tiempo_transcurrido % 60)

    # Mostrar el tiempo transcurrido en la pantalla
    textp_tiempo = font_titulo.render(f"Tiempo:",True, Colores.blanco)
    superficie_tiempo2 = font_titulo.render(f"{minutos:02d}:{segundos:02d}", True, Colores.blanco)
    pantalla.blit(textp_tiempo, (330, 410))
    pantalla.blit(superficie_tiempo2, (330, 445))

    # Dibujar el puntaje
    superficie_valor_puntaje = font_titulo.render(str(juego.puntaje), True, Colores.blanco)
    pantalla.blit(superficie_puntaje, (350, 15, 50, 50))
    pygame.draw.rect(pantalla, Colores.gris_oscuro, rect_puntaje, 0, 10)
    pantalla.blit(
        superficie_valor_puntaje,
        superficie_valor_puntaje.get_rect(
            centerx=rect_puntaje.centerx, centery=rect_puntaje.centery
        ),
    )

    # Dibujar otros elementos del juego
    pantalla.blit(superficie_siguiente, (335, 170, 50, 50))
    pantalla.blit(mejor_punt, (330, 480, 50, 50))
    if juego.fin_juego:
        pantalla.blit(
            superficie_fin_juego,
            superficie_fin_juego.get_rect(centerx=ANCHO // 2, centery=ALTO // 2),
        )
        pantalla.blit(opcion_continuar, (130, 330, 50, 50))
        pantalla.blit(opcion_salir, (160, 360, 50, 50))
    else:
        juego.dibujar(pantalla)

    # Mostrar el usuario con el puntaje máximo si está disponible
    if top_score_user is not None:
        texto_usuario = font_titulo.render(
            f"{top_score_user[0]}:", True, Colores.blanco
        )
        texto_puntaje = font_titulo.render(
            f"{top_score_user[1]}", True, Colores.blanco
        )
        pantalla.blit(texto_usuario, (335, 520))
        pantalla.blit(texto_puntaje, (335, 550))

    # Actualizar la pantalla y establecer la velocidad de fotogramas
    pygame.display.update()
    reloj.tick(60)


}
```
### 🧠Explicacion
Importaciones:

〰Se importan los módulos necesarios, como pygame, sys, sqlite3, juego, colores y time. Estos módulos proporcionan funcionalidades para crear el juego, interactuar con la base de datos y manejar el tiempo.
Conexión a la base de datos:

〰Se establece una conexión a una base de datos SQLite utilizando el módulo sqlite3. Si la base de datos no existe, se crea una nueva.
Se define una tabla llamada "scores" que tiene columnas para el ID del puntaje, el nombre de usuario y el puntaje en sí.
Funciones para manipular la base de datos:

〰insert_score: Esta función se utiliza para insertar una puntuación en la base de datos. Verifica si el nombre de usuario ya existe y si la nueva puntuación es mayor. Si el nombre de usuario no existe, se inserta una nueva fila en la tabla; de lo contrario, se actualiza la puntuación existente.
get_top_score_user: Esta función devuelve el usuario con el puntaje máximo en la base de datos.
Inicialización de Pygame:

〰Se inicializa la biblioteca Pygame llamando a la función pygame.init().
Se definen las dimensiones de la ventana del juego.
Carga de recursos:

〰Se cargan y redimensionan las imágenes de fondo utilizadas en el juego.
Se crea una instancia del juego utilizando la clase Juego.
Ventana de ingreso de nombre:

〰Antes de mostrar el menú, se muestra una ventana para que el jugador ingrese su nombre. El nombre se almacena en la variable nombre_jugador.
Bucle principal del juego:

〰El juego se ejecuta dentro de un bucle infinito.
	Se manejan los eventos, como presionar teclas o cerrar la ventana.
	Dependiendo del evento, se realizan acciones como mover la pieza, rotarla, actualizar el juego, etc.
	Se dibujan los elementos del juego en la pantalla, como el fondo, el puntaje, el tiempo, la próxima pieza, etc.
	La pantalla se actualiza y se establece la velocidad de fotogramas utilizando el reloj de Pygame.
〰Funciones adicionales:

〰mostrar_menu: Esta función muestra el menú principal del juego, donde el jugador puede elegir entre iniciar el juego, ver la tabla de puntuaciones o salir.

〰mostrar_tabla_puntuaciones: Esta función muestra la tabla de puntuaciones obtenidas de la base de datos. Se muestran los mejores puntajes y los nombres de usuario correspondientes.

〰mostrar_ventana_nombre: Esta función muestra una ventana donde el jugador puede ingresar su nombre antes de comenzar el juego.


### 🤖Menu principal
![MENU PRINCIPAL](https://github.com/magikboy/parcial-1-labo/blob/808cd1a859e4195102cf4a7dd3dc5d2a04a5baa1/menu1.PNG)


### 🤖Menu de scores

![MENU SCORES](https://github.com/magikboy/parcial-1-labo/blob/faea3a0c5b3661aa432da058582056839d88fa45/menu2.PNG)

### 🤖Menu de ingreso de nombre

![MENU NOMBRE](https://github.com/magikboy/parcial-1-labo/blob/faea3a0c5b3661aa432da058582056839d88fa45/menu3.PNG)

### 🤖Juego en funcionamiento

![JUEGO](https://github.com/magikboy/parcial-1-labo/blob/faea3a0c5b3661aa432da058582056839d88fa45/menu4.PNG)

### 🧠GRILLA DEL JUEGO

``` py
import pygame
from colores import Colores

class Grid:
    def __init__(self):
        # Número de filas y columnas en la cuadrícula
        self.num_filas = 20
        self.num_columnas = 10
        # Tamaño de cada celda en píxeles
        self.tamaño_celda = 30
        # Crear una cuadrícula vacía
        self.grid = [[0 for j in range(self.num_columnas)] for i in range(self.num_filas)]
        # Obtener los colores para las celdas de la clase Colores
        self.colores = Colores.obtener_colores_celda()

    def imprimir_grid(self):
        # Imprimir la cuadrícula en la consola
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                print(self.grid[fila][columna], end=" ")
            print()

    def esta_dentro(self, fila, columna):
        # Verificar si una celda está dentro de los límites de la cuadrícula
        if fila >= 0 and fila < self.num_filas and columna >= 0 and columna < self.num_columnas:
            return True
        return False

    def esta_vacia(self, fila, columna):
        # Verificar si una celda está vacía (contiene un valor de 0)
        if self.grid[fila][columna] == 0:
            return True
        return False

    def fila_completa(self, fila):
        # Verificar si una fila está completamente llena (no contiene valores de 0)
        for columna in range(self.num_columnas):
            if self.grid[fila][columna] == 0:
                return False
        return True

    def limpiar_fila(self, fila):
        # Limpiar una fila, estableciendo todos los valores a 0
        for columna in range(self.num_columnas):
            self.grid[fila][columna] = 0

    def desplazar_fila_abajo(self, fila, num_filas):
        # Desplazar una fila hacia abajo, copiando los valores de la fila superior
        for columna in range(self.num_columnas):
            self.grid[fila+num_filas][columna] = self.grid[fila][columna]
            self.grid[fila][columna] = 0

    def limpiar_filas_completas(self):
        # Limpiar todas las filas completas y desplazar las filas superiores hacia abajo
        completadas = 0
        for fila in range(self.num_filas-1, 0, -1):
            if self.fila_completa(fila):
                self.limpiar_fila(fila)
                completadas += 1
            elif completadas > 0:
                self.desplazar_fila_abajo(fila, completadas)
        return completadas

    def reiniciar(self):
        # Reiniciar la cuadrícula, estableciendo todos los valores a 0
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                self.grid[fila][columna] = 0

    def dibujar(self, pantalla):
        # Dibujar la cuadrícula en la pantalla de juego utilizando colores
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                valor_celda = self.grid[fila][columna]
                rectangulo_celda = pygame.Rect(columna*self.tamaño_celda + 11, fila*self.tamaño_celda + 11,
                self.tamaño_celda - 1, self.tamaño_celda - 1)
                pygame.draw.rect(pantalla, self.colores[valor_celda], rectangulo_celda)

```


Inicialización de la cuadrícula: En el método __init__, se definen las características iniciales de la cuadrícula. Se establece el número de filas y columnas, el tamaño de cada celda en píxeles y se crea una cuadrícula vacía representada por una lista bidimensional (self.grid).

Métodos para verificar y modificar celdas:

⭕El método esta_dentro verifica si una celda está dentro de los límites de la cuadrícula.

⭕El método esta_vacia verifica si una celda está vacía (contiene el valor 0).

⭕El método fila_completa verifica si una fila está completamente llena (no contiene valores de 0).

⭕El método limpiar_fila establece todos los valores de una fila en 0.

⭕El método desplazar_fila_abajo desplaza una fila hacia abajo, copiando los valores de la fila superior.

⭕El método limpiar_filas_completas limpia todas las filas completas y desplaza las filas superiores hacia abajo.

Método para reiniciar la cuadrícula: El método reiniciar establece todos los valores de la cuadrícula en 0, reiniciando así la cuadrícula.


Método para dibujar la cuadrícula: El método dibujar utiliza la biblioteca Pygame para dibujar la cuadrícula en una pantalla de juego. Itera sobre cada celda de la cuadrícula, obtiene el valor de la celda y dibuja un rectángulo en la pantalla utilizando el color correspondiente a ese valor de celda.














### 🧠funcionamiento del juego

``` py
from grilla import *
from bloques import *
import random
import pygame

class Juego:
	def __init__(self):
		self.grid = Grid()  # Crear una nueva grilla
		self.bloques = [BloqueI(), BloqueJ(), BloqueL(), BloqueO(), BloqueS(), BloqueT(), BloqueZ()]  # Crear una lista de bloques disponibles
		self.bloque_actual = self.obtener_bloque_aleatorio()  # Obtener un bloque aleatorio como bloque actual
		self.siguiente_bloque = self.obtener_bloque_aleatorio()  # Obtener otro bloque aleatorio como siguiente bloque
		self.fin_juego = False  # Bandera para indicar si el juego ha terminado
		self.puntaje = 0  # Puntaje actual del jugador
		self.sonido_rotar = pygame.mixer.Sound("musica\drotate.ogg")  # Cargar el sonido de rotación
		self.sonido_limpiar = pygame.mixer.Sound("musica\clear.ogg")  # Cargar el sonido de limpiar filas

		pygame.mixer.music.load("musica\dtetris99.mp3")  # Cargar la música de fondo
		pygame.mixer.music.set_volume(0.1)  # Establecer el volumen de la música
		pygame.mixer.music.play(-1)  # Reproducir la música en bucle

	def actualizar_puntaje(self, lineas_completadas, puntos_movimiento_abajo):
		# Actualizar el puntaje según el número de líneas completadas y los puntos por movimiento hacia abajo
		if lineas_completadas == 1:
			self.puntaje += 100
		elif lineas_completadas == 2:
			self.puntaje += 300
		elif lineas_completadas == 3:
			self.puntaje += 500
		elif lineas_completadas == 4:
			self.puntaje += 800
		elif lineas_completadas == 5:
			self.puntaje += 1500
		self.puntaje += puntos_movimiento_abajo

	def obtener_bloque_aleatorio(self):
		if len(self.bloques) == 0:
			self.bloques = [BloqueI(), BloqueJ(), BloqueL(), BloqueO(), BloqueS(), BloqueT(), BloqueZ()]  # Reiniciar la lista de bloques si está vacía
		bloque = random.choice(self.bloques)  # Obtener un bloque aleatorio de la lista
		self.bloques.remove(bloque)  # Eliminar el bloque seleccionado de la lista
		return bloque

	def mover_izquierda(self):
		self.bloque_actual.mover(0, -1)  # Mover el bloque actual hacia la izquierda
		if self.bloque_dentro() == False or self.bloque_encaja() == False:
			self.bloque_actual.mover(0, 1)  # Deshacer el movimiento si el bloque no está dentro de la grilla o no encaja

	def mover_derecha(self):
		self.bloque_actual.mover(0, 1)  # Mover el bloque actual hacia la derecha
		if self.bloque_dentro() == False or self.bloque_encaja() == False:
			self.bloque_actual.mover(0, -1)  # Deshacer el movimiento si el bloque no está dentro de la grilla o no encaja

	def mover_abajo(self):
		self.bloque_actual.mover(1, 0)  # Mover el bloque actual hacia abajo
		if self.bloque_dentro() == False or self.bloque_encaja() == False:
			self.bloque_actual.mover(-1, 0)  # Deshacer el movimiento si el bloque no está dentro de la grilla o no encaja
			self.bloque_bloqueado()  # Fijar el bloque actual en su posición actual y obtener el siguiente bloque

	def bloque_bloqueado(self):
		celdas = self.bloque_actual.obtener_posiciones_celdas()  # Obtener las posiciones de celda del bloque actual
		for posicion in celdas:
			self.grid.grid[posicion.fila][posicion.columna] = self.bloque_actual.id  # Fijar el valor del bloque en la grilla
		self.bloque_actual = self.siguiente_bloque  # Establecer el siguiente bloque como bloque actual
		self.siguiente_bloque = self.obtener_bloque_aleatorio()  # Obtener un nuevo bloque aleatorio como siguiente bloque
		filas_completas = self.grid.limpiar_filas_completas()  # Limpiar las filas completas de la grilla
		if filas_completas > 0:
			self.sonido_limpiar.play()  # Reproducir el sonido de limpiar filas
			self.actualizar_puntaje(filas_completas, 0)  # Actualizar el puntaje según las filas completadas
		if self.bloque_encaja() == False:
			self.fin_juego = True  # Establecer la bandera de fin de juego si el siguiente bloque no encaja

	def reiniciar(self):
		self.grid.reiniciar()  # Reiniciar la grilla
		self.bloques = [BloqueI(), BloqueJ(), BloqueL(), BloqueO(), BloqueS(), BloqueT(), BloqueZ()]  # Reiniciar la lista de bloques
		self.bloque_actual = self.obtener_bloque_aleatorio()  # Obtener un nuevo bloque aleatorio como bloque actual
		self.siguiente_bloque = self.obtener_bloque_aleatorio()  # Obtener otro bloque aleatorio como siguiente bloque
		self.puntaje = 0  # Reiniciar el puntaje

	def bloque_encaja(self):
		celdas = self.bloque_actual.obtener_posiciones_celdas()  # Obtener las posiciones de celda del bloque actual
		for celda in celdas:
			if self.grid.esta_vacia(celda.fila, celda.columna) == False:  # Comprobar si alguna celda del bloque no está vacía en la grilla
				return False
		return True  # El bloque encaja en la grilla si todas las celdas están vacías

	def rotar(self):
		self.bloque_actual.rotar()  # Rotar el bloque actual
		if self.bloque_dentro() == False or self.bloque_encaja() == False:
			self.bloque_actual.deshacer_rotacion()  # Deshacer la rotación si el bloque no está dentro de la grilla o no encaja
		else:
			self.sonido_rotar.play()  # Reproducir el sonido de rotación

	def bloque_dentro(self):
		celdas = self.bloque_actual.obtener_posiciones_celdas()  # Obtener las posiciones de celda del bloque actual
		for celda in celdas:
			if self.grid.esta_dentro(celda.fila, celda.columna) == False:  # Comprobar si alguna celda del bloque está fuera de la grilla
				return False
		return True  # El bloque está completamente dentro de la grilla

	def dibujar(self, pantalla):
		self.grid.dibujar(pantalla)  # Dibujar la grilla en la pantalla
		self.bloque_actual.dibujar(pantalla, 11, 11)  # Dibujar el bloque actual en la pantalla

		# Dibujar el siguiente bloque en una posición específica dependiendo del tipo de bloque
		if self.siguiente_bloque.id == 3:
			self.siguiente_bloque.dibujar(pantalla, 255, 290)
		elif self.siguiente_bloque.id == 4:
			self.siguiente_bloque.dibujar(pantalla, 255, 280)
		else:
			self.siguiente_bloque.dibujar(pantalla, 270, 270)

```
La función **displayOff()** se utiliza para apagar todos los segmentos del display cuando se sale del switch o se necesita apagar el display.

Las funciones **cero() a nueve()**se utilizan para mostrar los dígitos del 0 al 9 en el display. Cada función enciende los segmentos necesarios para mostrar el dígito correspondiente. Por ejemplo, la función cero() enciende todos los segmentos excepto el segmento G.

La función **todos()** enciende todos los segmentos del display, lo que resulta en la visualización del número 8.

La función **actualizarDisplay()** se utiliza para mostrar el número del piso en el que se encuentra un elevador, por ejemplo. Se utiliza un switch para seleccionar el número del piso y luego se llama a esta función para actualizar el display con el número correspondiente. La función toma como argumento el número del piso y utiliza los comandos digitalWrite() para encender los segmentos necesarios para mostrar el número en el display.

### 🧠Posicionamiento de los bloques en las celdas

``` py
class Posicion:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
```


### 🧠Rotaciones de los distintos Bloques

``` py
from bloque import Bloque
from posicion import Posicion

class BloqueL(Bloque):
    def __init__(self):
        super().__init__(id=1)  # Llama al constructor de la clase padre Bloque con el identificador 1
        
        # Definir las posiciones de las celdas para cada rotación del bloque L
        self.celdas = {
            0: [Posicion(0, 2), Posicion(1, 0), Posicion(1, 1), Posicion(1, 2)],  # Primera rotación del bloque L
            1: [Posicion(0, 1), Posicion(1, 1), Posicion(2, 1), Posicion(2, 2)],  # Segunda rotación del bloque L
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(2, 0)],  # Tercera rotación del bloque L
            3: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 1), Posicion(2, 1)]   # Cuarta rotación del bloque L
        }
        
        self.mover(0, 3)  # Ajustar la posición inicial del bloque

# La clase BloqueL hereda de Bloque y representa un bloque en forma de "L".
# Se definen las posiciones de las celdas para cada rotación del bloque L en el diccionario self.celdas.

class BloqueJ(Bloque):
    def __init__(self):
        super().__init__(id=2)
        # Definir las posiciones de las celdas para cada rotación del bloque J
        self.celdas = {
            0: [Posicion(0, 0), Posicion(1, 0), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 1), Posicion(0, 2), Posicion(1, 1), Posicion(2, 1)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(2, 2)],
            3: [Posicion(0, 1), Posicion(1, 1), Posicion(2, 0), Posicion(2, 1)]
        }
        self.mover(0, 3)  # Ajustar la posición inicial del bloque

class BloqueI(Bloque):
    def __init__(self):
        super().__init__(id=3)
        # Definir las posiciones de las celdas para cada rotación del bloque I
        self.celdas = {
            0: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(1, 3)],
            1: [Posicion(0, 2), Posicion(1, 2), Posicion(2, 2), Posicion(3, 2)],
            2: [Posicion(2, 0), Posicion(2, 1), Posicion(2, 2), Posicion(2, 3)],
            3: [Posicion(0, 1), Posicion(1, 1), Posicion(2, 1), Posicion(3, 1)]
        }
        self.mover(-1, 3)  # Ajustar la posición inicial del bloque

class BloqueO(Bloque):
    def __init__(self):
        super().__init__(id=4)
        # Definir las posiciones de las celdas para el bloque O (no hay rotaciones)
        self.celdas = {
            0: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 0), Posicion(1, 1)]
        }
        self.mover(0, 4)  # Ajustar la posición inicial del bloque

class BloqueS(Bloque):
    def __init__(self):
        super().__init__(id=5)
        # Definir las posiciones de las celdas para cada rotación del bloque S
        self.celdas = {
            0: [Posicion(0, 1), Posicion(0, 2), Posicion(1, 0), Posicion(1, 1)],
            1: [Posicion(0, 1), Posicion(1, 1), Posicion(1, 2), Posicion(2, 2)],
            2: [Posicion(1, 1), Posicion(1, 2), Posicion(2, 0), Posicion(2, 1)],
            3: [Posicion(0, 0), Posicion(1, 0), Posicion(1, 1), Posicion(2, 1)]
        }
        self.mover(0, 3)  # Ajustar la posición inicial del bloque

class BloqueT(Bloque):
    def __init__(self):
        super().__init__(id=6)
        # Definir las posiciones de las celdas para cada rotación del bloque T
        self.celdas = {
            0: [Posicion(0, 1), Posicion(1, 0), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 1), Posicion(1, 1), Posicion(1, 2), Posicion(2, 1)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(2, 1)],
            3: [Posicion(0, 1), Posicion(1, 0), Posicion(1, 1), Posicion(2, 1)]
        }
        self.mover(0, 3)  # Ajustar la posición inicial del bloque

class BloqueZ(Bloque):
    def __init__(self):
        super().__init__(id=7)
        # Definir las posiciones de las celdas para cada rotación del bloque Z
        self.celdas = {
            0: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 2), Posicion(1, 1), Posicion(1, 2), Posicion(2, 1)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(2, 1), Posicion(2, 2)],
            3: [Posicion(0, 1), Posicion(1, 0), Posicion(1, 1), Posicion(2, 0)]
        }
        self.mover(0, 3)  # Ajustar la posición inicial del bloque

```


### 🧠Funcionamiento de los bloques

``` py
from colores import Colores
import pygame
from posicion import Posicion

class Bloque:
    def __init__(self, id):
        self.id = id
        self.celdas = {}
        self.tam_celda = 30
        self.despl_fila = 0
        self.despl_columna = 0
        self.estado_rotacion = 0
        self.colores = Colores.obtener_colores_celda()  # Inicializar los colores para las celdas

    def mover(self, filas, columnas):
        self.despl_fila += filas  # Actualizar el desplazamiento de filas
        self.despl_columna += columnas  # Actualizar el desplazamiento de columnas

    def obtener_posiciones_celdas(self):
        mosaicos = self.celdas[self.estado_rotacion]  # Obtener las posiciones de las celdas para el estado de rotación actual
        moved_tiles = []
        for posicion in mosaicos:
            # Aplicar el desplazamiento actual a cada posición de celda
            posicion = Posicion(posicion.fila + self.despl_fila, posicion.columna + self.despl_columna)
            moved_tiles.append(posicion)
        return moved_tiles  # Devolver las posiciones de celda actualizadas

    def rotar(self):
        self.estado_rotacion += 1  # Incrementar el estado de rotación
        if self.estado_rotacion == len(self.celdas):
            self.estado_rotacion = 0  # Restablecer el estado de rotación si supera el número de rotaciones disponibles

    def deshacer_rotacion(self):
        self.estado_rotacion -= 1  # Decrementar el estado de rotación
        if self.estado_rotacion == 0:
            self.estado_rotacion = len(self.celdas) - 1  # Volver al último estado de rotación si se vuelve negativo

    def dibujar(self, pantalla, offset_x, offset_y):
        mosaicos = self.obtener_posiciones_celdas()  # Obtener las posiciones de celda actuales
        for mosaico in mosaicos:
            # Calcular el rectángulo para cada celda y dibujarlo en la pantalla
            rectangulo_mosaico = pygame.Rect(
                offset_x + mosaico.columna * self.tam_celda,
                offset_y + mosaico.fila * self.tam_celda,
                self.tam_celda - 1,
                self.tam_celda - 1
            )
            pygame.draw.rect(pantalla, self.colores[self.id], rectangulo_mosaico)  # Dibujar la celda con su color asignado

```


La función **setup()** es una función que se ejecuta una sola vez al inicio del programa. En ella se inicializan los pines que se van a utilizar como entradas o salidas, y se establece la velocidad de comunicación para la interfaz serial (Serial.begin(9600)). Además, se llama a la función mostrarPiso() para que muestre el piso en el que se encuentra el montacargas en ese momento.

La variable **botonSubir** es una variable que se utiliza para almacenar el estado del botón de subir. Se lee su estado utilizando la función digitalRead(), que devuelve un valor HIGH o LOW dependiendo de si el botón está pulsado o no.

La variable **botonBajar** es una variable que se utiliza para almacenar el estado del botón de bajar. Se lee su estado utilizando la función digitalRead().

la variable **botonPausa** es una variable que se utiliza para almacenar el estado del botón de pausa. Se lee su estado utilizando la función digitalRead().

### 📄Parcial:

[Consignas](https://github.com/magikboy/parcial-1-labo/blob/e1263af61cea1b0cd53b5fe3f9e29e358a023020/Pygame_Modelos_TPs.pdf)

### 📄Fuentes

- [Youtube](https://www.youtube.com)
- [pygame](https://www.pygame.org/docs/ref/draw.html)
- [programarcadegames](http://programarcadegames.com/index.php?chapter=formatting&lang=en#:~:text=A%20format%20of%20.,1.5555%20would%20display%20as%201.56%20)
- [Utn](http://www.sistemas-utnfra.com.ar/#/home)
