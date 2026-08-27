from material import Material


class Revista(Material):

    # Revista hereda de Material
    def __init__(self, titulo, autor, precio, edicion, es_nuevo=True):
        super().__init__(titulo, autor, precio, es_nuevo)
        if edicion <= 0:
            raise ValueError("El numero de edicion debe ser mayor que 0.")
        self.edicion = edicion

    def num_edicion(self):

        print(f"La revista es de la edicion numero {self.edicion}.")
        return self.edicion

    def descripcion(self):

        super().descripcion()
        print(f"Edición: {self.edicion}")