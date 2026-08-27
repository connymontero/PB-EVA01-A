class Material:
#   CLASE PADRE
    def __init__(self, titulo, autor, precio, es_nuevo=True):
        self.titulo = titulo
        self.autor = autor
        self.set_precio(precio)
        self.es_nuevo = es_nuevo

    def get_precio(self):

        return self.__precio

    def set_precio(self, nuevo_precio):
        # actualiza el precio solo cuando es mayor que cero
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        self.__precio = nuevo_precio

    def descripcion(self):

        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.__precio}")