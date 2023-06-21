import pygame
import sys
import sqlite3
from juego import Juego
from colores import Colores
import time
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import rotate


#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#Base De Datos#-------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#


# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('puntuacion\dtetris_scores.db')

# Crear la tabla de puntuaciones si no existe
conn.execute('''CREATE TABLE IF NOT EXISTS scores
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                score INTEGER)''')

"""En estas líneas de código, se importan los módulos necesarios, 
se establece una conexión a una base de datos SQLite y se crea una tabla llamada "scores" si no existe. 
Esta tabla tiene tres columnas: "id" (entero, clave primaria), "username" (texto) y "score" (entero)."""

# Función para insertar una puntuación en la base de datos
def insert_score(username, score):
    # Verificar si el nombre del jugador ya existe en la base de datos
    cursor = conn.execute("SELECT score FROM scores WHERE username = ?", (username,))
    existing_score = cursor.fetchone() #Este método recupera la fila siguiente de un conjunto de resultados de consulta y devuelve una sola secuencia

    if existing_score is None or score > existing_score[0]:
        # El nombre del jugador no existe o la nueva puntuación es mayor
        if existing_score is None:
            # Insertar una nueva fila en la tabla
            conn.execute("INSERT INTO scores (username, score) VALUES (?, ?)", (username, score))
        else:
            # Actualizar la puntuación existente
            conn.execute("UPDATE scores SET score = ? WHERE username = ?", (score, username))
        conn.commit() #Este método envía una COMMIT declaración al servidor MySQL


"""Esta función llamada insert_score se utiliza para insertar una puntuación en la base de datos. 
Primero verifica si el nombre del jugador ya existe en la base de datos consultando la tabla "scores". 
Si el nombre no existe o la nueva puntuación es mayor que la existente, 
se inserta una nueva fila en la tabla o se actualiza la puntuación existente."""


# Función para obtener el usuario con el puntaje máximo
def get_top_score_user():
    cursor = conn.execute("SELECT username, MAX(score) FROM scores")
    return cursor.fetchone()


"""La función get_top_score_user se utiliza para obtener el usuario con la puntuación máxima de la tabla "scores". 
Realiza una consulta SQL para seleccionar el nombre de usuario y la puntuación máxima,
 y devuelve la primera fila del resultado de la consulta."""


#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#inicio del Juego#----------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#


# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana del juego
ALTO = 620
ANCHO = 500

#Se carga el video
video = VideoFileClip("videos\dfondomenu.mp4")
videonombre = VideoFileClip("videos\dvideonombre.mp4")
videoPuntuacion = VideoFileClip("videos\dmenuPuntuacion.mp4")
videoJuego = VideoFileClip("videos\dfondoJuego.mp4")


#Rotación de 90 grados en sentido horario
video = rotate(video, 90)
videonombre = rotate(videonombre, 90)
videoPuntuacion = rotate(videoPuntuacion, 90)
videoJuego = rotate(videoJuego, 90)

#Reproducir en bucle
video = video.loop(duration=video.duration)
videonombre = videonombre.loop(duration=videonombre.duration)
videoPuntuacion = videoPuntuacion.loop(duration=videoPuntuacion.duration)
videoJuego = videoJuego.loop(duration=videoJuego.duration)

#Se crea una superficie de pygame
video_surface = pygame.display.set_mode((ANCHO, ALTO))




# Fuente para el título
font_titulo = pygame.font.Font("font\dfont.ttf", 25)

# Superficies de texto para mostrar en la pantalla
superficie_puntaje = font_titulo.render("Puntaje:", True, Colores.blanco)
superficie_siguiente = font_titulo.render("Siguiente:", True, Colores.blanco)
superficie_fin_juego = font_titulo.render("GAME OVER", True, Colores.rojo)
superficie_opcion_jugar = font_titulo.render("Iniciar juego", True, Colores.gris_oscuro)
superficie_opcion_puntuaciones = font_titulo.render("Puntuaciones", True, Colores.gris_oscuro)
superficie_opcion_salir = font_titulo.render("Salir", True, Colores.gris_oscuro)
opcion_salir = font_titulo.render("Esc para salir", True, Colores.blanco)
opcion_continuar = font_titulo.render("Esp para reiniciar", True, Colores.blanco)
mejor_punt = font_titulo.render("Mejor:", True, Colores.blanco)

# Rectángulos para los elementos en la pantalla
rect_puntaje = pygame.Rect(315, 55, 150, 60)
rect_siguiente = pygame.Rect(330, 215, 150, 180)

"""se define los rectángulos que se utilizarán para dibujar el puntaje y la pieza siguiente en la pantalla."""

# Crear la ventana del juego
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Segundo Parcial: Tetris")

"""se crea la ventana del juego con el tamaño especificado por las constantes ANCHO y ALTO.
También se establece el título de la ventana como "Segundo Parcial: Tetris". """

"""En estas líneas se carga la imagen de fondo del juego y se redimensiona para que se ajuste al tamaño de la ventana del juego."""

# Establecer el reloj para limitar la velocidad de actualización de la pantalla
reloj = pygame.time.Clock()

"""Aquí se crea un objeto de reloj que se utilizará para limitar la velocidad de actualización de la pantalla."""

# Crear una instancia del juego
juego = Juego()

"""Se crea una instancia de la clase "Juego", que contiene la lógica y los elementos del juego."""

# Obtener el nombre del jugador
nombre_jugador = ""

"""Se inicializa la variable "nombre_jugador" como una cadena vacía para almacenar el nombre del jugador."""

#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#Menu Nombre#---------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

# Función para mostrar la ventana de ingreso de nombre
def mostrar_ventana_nombre():
    global nombre_jugador
    nombre_ingresado = False

    while not nombre_ingresado:
        frame = videonombre.get_frame(pygame.time.get_ticks() / 1000)
        frame = pygame.surfarray.make_surface(frame)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    nombre_ingresado = True
                elif evento.key == pygame.K_BACKSPACE:
                    # Eliminar el último carácter si se presiona Retroceso
                    nombre_jugador = nombre_jugador[:-1]
                elif len(nombre_jugador) < 6:
                    # Solo agregue el carácter si la longitud del nombre es menor a 6
                    nombre_jugador += evento.unicode
        """
        pygame.QUIT: Se ejecuta cuando se presiona el botón de cerrar la ventana del juego. 
        En este caso, se llama a las funciones pygame.quit() y sys.exit() para salir del juego y cerrar la ventana.

        pygame.KEYDOWN: Se ejecuta cuando se presiona una tecla. En este caso, se verifica si la tecla presionada es la tecla Enter 

        (pygame.K_RETURN). Si es así, se marca que se ingresó un nombre válido y se puede salir del bucle.

        pygame.KEYUP: Se ejecuta cuando se suelta una tecla después de haberla presionado. 

        En este caso, se verifica si la tecla suelta es la tecla de retroceso (pygame.K_BACKSPACE).

        Si es así, se elimina el último carácter ingresado del nombre del jugador. Si se suelta cualquier otra tecla, 
        se agrega su carácter unicode al nombre del jugador."""

            
        video_surface.blit(frame, (0, 0))
        pantalla.blit(video_surface, (0, 0))
        enter = font_titulo.render("Ent para continuar", True, Colores.CRIMSON)
        texto_nombre = font_titulo.render(nombre_jugador, True, Colores.CRIMSON)
        pantalla.blit(texto_nombre, (70, 240))
        pantalla.blit(enter, (120, 530))
        pygame.display.update()

"""Aquí se define una función llamada "mostrar_ventana_nombre()"
que se encargará de mostrar la ventana de ingreso de nombre del jugador."""


# Obtener el usuario con el puntaje máximo
top_score_user = get_top_score_user()

"""Se llama a la función "get_top_score_user()" para obtener el usuario con el puntaje máximo 
de la base de datos y se guarda en la variable "top_score_user"."""

# Evento personalizado para actualizar el juego
ACTUALIZAR_JUEGO = pygame.USEREVENT
pygame.time.set_timer(ACTUALIZAR_JUEGO, 200)

"""Aquí se crea un evento personalizado llamado "ACTUALIZAR_JUEGO" que se activará cada
200 milisegundos para actualizar el estado del juego."""

#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#Menu Tabla#----------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

# Función para mostrar la tabla de puntuaciones
def mostrar_tabla_puntuaciones():
    while True:
        frame = videoPuntuacion.get_frame(pygame.time.get_ticks() / 1000)
        frame = pygame.surfarray.make_surface(frame)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

        video_surface.blit(frame, (0, 0))
        pantalla.blit(video_surface, (0, 0))
        # Obtener los datos de la tabla de puntuaciones desde la base de datos
        cursor = conn.execute("SELECT username, score FROM scores ORDER BY score DESC LIMIT 5")
        puntuaciones = cursor.fetchall()

        # Mostrar los datos en la pantalla
        y = 240
        for i, puntuacion in enumerate(puntuaciones):
            texto_puntuacion = font_titulo.render(f"{i+1}. {puntuacion[0]}: {puntuacion[1]}", True, Colores.blanco)
            pantalla.blit(texto_puntuacion, (150, y))
            y += 40

        pygame.display.update()

"""Se define una función llamada "mostrar_tabla_puntuaciones()" que se encarga de mostrar la tabla de puntuaciones."""

#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#Menu Principal#------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

# Función para mostrar el menú
def mostrar_menu():
    while True:
        frame = video.get_frame(pygame.time.get_ticks() / 1000)
        frame = pygame.surfarray.make_surface(frame)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                # Evento: Salir del juego
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Evento: Clic del mouse
                # Obtener la posición del cursor del mouse al hacer clic
                x, y = pygame.mouse.get_pos()
                if 160 < x < 300 and 200 < y < 260: #cordenadas para el click
                    # Opción 1: Iniciar juego
                    juego.reiniciar()
                    return
                elif 110 < x < 350 and 300 < y < 350: #cordenadas para el click
                    # Opción 2: Ver tabla de puntuaciones
                    mostrar_tabla_puntuaciones()
                elif 200 < x < 250 and 370 < y < 430: #cordenadas para el click
                    # Opción 3: Salir
                    pygame.quit()
                    sys.exit()
        video_surface.blit(frame, (0, 0))
        pantalla.blit(video_surface, (0, 0))
        pygame.display.update()

"""Se define una función llamada "mostrar_menu()" que se encarga de mostrar el menú principal del juego."""

#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#Bucle Pincipal#------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

# Mostrar el menú antes del juego
mostrar_menu()
# Mostrar la ventana de ingreso de nombre
mostrar_ventana_nombre()

"""se llama a las funciones "mostrar_menu()" y "mostrar_ventana_nombre()" 
para mostrar el menú principal y la ventana de ingreso de nombre del jugador."""

# Bucle principal del juego
tiempo_inicio = time.time()
while True:
    frame = videoJuego.get_frame(pygame.time.get_ticks() / 1000)
    frame = pygame.surfarray.make_surface(frame)
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
                juego.actualizar_puntaje(0, 1)
            elif evento.key == pygame.K_RIGHT and juego.fin_juego == False:
                juego.mover_derecha()
                juego.actualizar_puntaje(0, 1)
            elif evento.key == pygame.K_DOWN and juego.fin_juego == False:
                juego.mover_abajo()
                juego.actualizar_puntaje(0, 1)
            elif evento.key == pygame.K_UP and juego.fin_juego == False:
                juego.rotar()
        # Verificar si se ha activado el evento personalizado ACTUALIZAR_JUEGO
        if evento.type == ACTUALIZAR_JUEGO and juego.fin_juego == False:
            juego.mover_abajo()

    """Estas líneas inician el bucle principal del juego, que se ejecutará infinitamente hasta que el juego se cierre."""

    # Dibujar los elementos en la pantalla
    video_surface.blit(frame, (0, 0))
    pantalla.blit(video_surface, (0, 0))
    # Calcular el tiempo transcurrido
    tiempo_transcurrido = time.time() - tiempo_inicio
    minutos = int(tiempo_transcurrido // 60)
    segundos = int(tiempo_transcurrido % 60)

    # Mostrar el tiempo transcurrido en la pantalla
    textp_tiempo = font_titulo.render(f"Tiempo:", True, Colores.blanco)
    superficie_tiempo2 = font_titulo.render(f"{minutos:02d}:{segundos:02d}", True, Colores.blanco)
    pantalla.blit(textp_tiempo, (330, 410))
    pantalla.blit(superficie_tiempo2, (330, 445))

    # Dibujar el puntaje
    superficie_valor_puntaje = font_titulo.render(str(juego.puntaje), True, Colores.blanco)
    pantalla.blit(superficie_puntaje, (325, 25, 50, 50))
    pantalla.blit(
        superficie_valor_puntaje,
        superficie_valor_puntaje.get_rect(centerx=rect_puntaje.centerx, centery=rect_puntaje.centery),
    )

    # Dibujar otros elementos del juego
    pantalla.blit(superficie_siguiente, (325, 180, 50, 50))
    pantalla.blit(mejor_punt, (330, 480, 50, 50))

    if juego.fin_juego:
        # El juego ha terminado
        pantalla.blit(
            superficie_fin_juego,
            superficie_fin_juego.get_rect(centerx=ANCHO // 2, centery=ALTO // 2),
        )
        pantalla.blit(opcion_continuar, (130, 330, 50, 50))
        pantalla.blit(opcion_salir, (160, 360, 50, 50))
    else:
        # El juego está en curso
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

    """se dibujan los elementos del juego en la pantalla, se actualiza la pantalla y
    se limita la velocidad de fotogramas a 60 FPS (fotogramas por segundo)."""

#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#Fin Bucle Pincipal#--------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

