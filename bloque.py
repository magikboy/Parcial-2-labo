from colores import Colores
import pygame
from posicion import Posicion


#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#Creacion del Bloque#-------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#


class Bloque:
    def __init__(self, id):
        self.id = id
        self.celdas = {}  # Diccionario para almacenar las posiciones de las celdas del bloque
        self.tam_celda = 30  # Tamaño de cada celda en píxeles
        self.despl_fila = 0  # Desplazamiento actual de filas
        self.despl_columna = 0  # Desplazamiento actual de columnas
        self.estado_rotacion = 0  # Estado de rotación actual del bloque
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


#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#Fin Creacion del Bloque#---------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
