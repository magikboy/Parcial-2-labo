# parcial-1-labo
Juego tetris
### 📄Documentación de la Laboratorio - UTN Tecnicatura Superior en Programación.

### Nombre: Bosco Mascaro Massimo Ariel

### **Laboratorio**

![Arduino](https://github.com/magikboy/Parcial-1/blob/30c7b791849ce1d70de15ec52cb6a92ac3aec450/ArduinoTinkercad.jpg)

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

### 🚀Codigo del proyecto
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
### 🤖Funcionando
![Montacargas de hospital](https://github.com/magikboy/Parcial-1/blob/655e31a70d93ce6f4b70d06eaaaa3bd76ab51a28/2023-05-16-11-57-43.gif)

### 🧠Explicacion

``` C++
#define BOTON_SUBIR 2
#define BOTON_BAJAR 3
#define BOTON_PAUSAR 4
#define led_Verde 5
#define led_Rojo 6
#define A 7
#define B 8
#define C 9
#define D 10
#define E 11
#define F 12
#define G 13
const int TIEMPO_ESPERA_BOTON = 10; // Tiempo de espera entre lecturas de botones en milisegundos.
const int TIEMPO_POR_PISO = 3000; // Tiempo que tarda el montacargas en llegar a cada piso en milisegundos.
const int TIEMPO_ESPERA_MOVIMIENTO = 3000; // Tiempo de espera después de que se mueve el montacargas en milisegundos.

boolean botonSubir = false;
boolean botonBajar = false;
boolean botonPausa = false;
boolean enMovimiento = false;

int contador = 0; //INICIALIZO EL CONTADOR EN 0
String mensaje = ""; //PARA PODER ESCRIBIR EN EL MONITOR

const char* mensajesPisos[] = {
  "Llego al piso 0.",
  "Llego al piso 1.",
  "Llego al piso 2.",
  "Llego al piso 3.",
  "Llego al piso 4.",
  "Llego al piso 5.",
  "Llego al piso 6.",
  "Llego al piso 7.",
  "Llego al piso 8.",
  "Llego al piso 9."
};
```

Las constantes definen los pines que se usan para los botones, LEDs y segmentos de un display de siete segmentos. También define los tiempos que tarda el montacargas en llegar a cada piso y el tiempo que se espera después de que se mueve el montacargas.

Las variables booleanas son para almacenar el estado de los botones y el estado de movimiento del montacargas.

El contador se inicializa en 0 y se utiliza para indicar el piso actual en el que se encuentra el montacargas. El array de mensajes de pisos se usa para almacenar mensajes de texto que indican el piso al que se mueve el montacargas.


``` C++
// FUNCIONES

}
// FIN FUNCIONES
```
La función **displayOff()** se utiliza para apagar todos los segmentos del display cuando se sale del switch o se necesita apagar el display.

Las funciones **cero() a nueve()**se utilizan para mostrar los dígitos del 0 al 9 en el display. Cada función enciende los segmentos necesarios para mostrar el dígito correspondiente. Por ejemplo, la función cero() enciende todos los segmentos excepto el segmento G.

La función **todos()** enciende todos los segmentos del display, lo que resulta en la visualización del número 8.

La función **actualizarDisplay()** se utiliza para mostrar el número del piso en el que se encuentra un elevador, por ejemplo. Se utiliza un switch para seleccionar el número del piso y luego se llama a esta función para actualizar el display con el número correspondiente. La función toma como argumento el número del piso y utiliza los comandos digitalWrite() para encender los segmentos necesarios para mostrar el número en el display.

``` C++

}

```

La función **setup()** es una función que se ejecuta una sola vez al inicio del programa. En ella se inicializan los pines que se van a utilizar como entradas o salidas, y se establece la velocidad de comunicación para la interfaz serial (Serial.begin(9600)). Además, se llama a la función mostrarPiso() para que muestre el piso en el que se encuentra el montacargas en ese momento.

La variable **botonSubir** es una variable que se utiliza para almacenar el estado del botón de subir. Se lee su estado utilizando la función digitalRead(), que devuelve un valor HIGH o LOW dependiendo de si el botón está pulsado o no.

La variable **botonBajar** es una variable que se utiliza para almacenar el estado del botón de bajar. Se lee su estado utilizando la función digitalRead().

la variable **botonPausa** es una variable que se utiliza para almacenar el estado del botón de pausa. Se lee su estado utilizando la función digitalRead().

---
## <img src="tinkercad.png" alt="Tinkercad" height="32px"> Link al proyecto

- [Proyecto](https://www.tinkercad.com/things/cn31fUhwE2b)

### 📄Parcial:

[Consignas](https://github.com/magikboy/Parcial-1/blob/02b8c8bd45b8f18107d74b41cb75eaca4d41e1a5/Primer%20Parcial%20SPD%20Parte%20Practica.pdf)

### 📄Fuentes

- [Youtube](https://www.youtube.com)
- [electrontools](https://www.electrontools.com/Home/WP/display-7-segmentos/)
- [Utn](http://www.sistemas-utnfra.com.ar/#/home)
