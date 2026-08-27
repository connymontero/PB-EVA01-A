from material import Material



class Libro(Material):

    # libro heredade Material.
    def __init__(self, titulo, autor, precio, paginas, es_nuevo=True):
        super().__init__(titulo, autor, precio, es_nuevo)
        if paginas <= 0:
            raise ValueError("La cantidad de paginas debe ser mayor que 0.")
        self.paginas = paginas

    def cantidad_paginas(self):

        print(f"El libro tiene {self.paginas} paginas.")
        return self.paginas
        

    def descripcion(self):

        super().descripcion()
        print(f"Páginas: {self.paginas}")