import pygame
from colores import Colores

#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#Creacion de la Grilla#-----------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#


class Grid:
    def __init__(self):
        # Número de filas y columnas en la cuadrícula
        self.num_filas = 20
        self.num_columnas = 10
        # Tamaño de cada celda en píxeles
        self.tamaño_celda = 30
        # Crear una cuadrícula vacía
        self.grid = [[0 for j in range(self.num_columnas)] for i in range(self.num_filas)] 
        """esta línea de código inicializa la cuadrícula (self.grid) como una matriz de tamaño self.num_filas x self.num_columnas, 
        donde todas las celdas se establecen inicialmente en 0."""
        # Obtener los colores para las celdas de la clase Colores
        self.colores = Colores.obtener_colores_celda()

        """se Inician los atributos de la cuadrícula, como el número de filas, 
        columnas, tamaño de celda, crea una cuadrícula vacía y obtiene los colores para las celdas."""

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



#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#Fin Grilla#----------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#