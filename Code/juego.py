from grilla import *
from bloques import *
import random
import pygame


#---------------------------------------------------------------------------------------------------------------------#
#------------------------------------------#Creacion del sistema del Juego#-------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#


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
			self.siguiente_bloque.dibujar(pantalla, 245, 270)
		elif self.siguiente_bloque.id == 4:
			self.siguiente_bloque.dibujar(pantalla, 245, 260)
		else:
			self.siguiente_bloque.dibujar(pantalla, 255, 250)


#---------------------------------------------------------------------------------------------------------------------#
#------------------------------------------#Fin Creacion del sistema del Juego#---------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#