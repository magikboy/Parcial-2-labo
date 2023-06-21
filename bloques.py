from bloque import Bloque
from posicion import Posicion


#---------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------#Pocisiones de los Bloques#-------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#


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



#---------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------#Fin Pocisiones de los Bloques#------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#