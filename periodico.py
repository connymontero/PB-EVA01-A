from material import Material


class Periodico(Material):

	# Periodico  de Material
	def __init__(self, titulo, autor, precio, fecha_publicacion, es_nuevo=True):
		super().__init__(titulo, autor, precio, es_nuevo)
		self.fecha_publicacion = fecha_publicacion
        
	def descripcion(self):
	
		super().descripcion()
		print(f"Fecha de publicacion: {self.fecha_publicacion}")
