

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------#Colores#---------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

class Colores:
	gris_oscuro = (26, 31, 40)
	verde = (47, 230, 23)
	rojo = (232, 18, 18)
	naranja = (226, 116, 17)
	amarillo = (237, 234, 4)
	morado = (166, 0, 247)
	cian = (21, 204, 209)
	azul = (13, 64, 216)
	blanco = (255, 255, 255)
	azul_oscuro = (44, 44, 127)
	azul_claro = (59, 85, 162)
	negro = (0, 0, 0)
	DARKSEAGREEN = (143, 188, 143)
	DARKSEAGREEN1 = (193, 255, 193)
	DARKSEAGREEN2 = (180, 238, 180)
	DARKSEAGREEN3 = (155, 205, 155)
	DARKSEAGREEN4 = (105, 139, 105)
	AQUAMARINE1 = (127, 255, 212)
	AQUAMARINE2 = (118, 238, 198)
	AQUAMARINE3 = (102, 205, 170)
	AQUAMARINE4 = (69, 139, 116)
	AZURE1 = (240, 255, 255)
	AZURE2 = (224, 238, 238)
	AZURE3 = (193, 205, 205)
	AZURE4 = (131, 139, 139)
	BANANA = (227, 207, 87)
	negro2 = (9,9,9)
	CRIMSON = (220, 20, 60)
	LAVENDER = (230, 230, 250)
	LIGHTPINK = (255, 182, 193)
	OLIVE = (128, 128, 0)
	ORANGE2 = (238, 154, 0)
	DEEPPINK1 = (255, 20, 147)
	MAROON = (128, 0, 0)
	
	
	@classmethod  #@classmethod es un decorador de python que permite definir un metodo en una clase en vez de una instancia de la clase
	def obtener_colores_celda(cls): #cls referencia a la clase y nos permite acceder a los atributos
		return [cls.gris_oscuro, cls.verde, cls.rojo, cls.naranja, cls.amarillo, cls.morado, cls.cian, cls.azul,cls.negro]
	
	#método de clase llamado obtener_colores_celda() que devuelve una lista con los colores de las celdas



#---------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------#Fin Colores#------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
