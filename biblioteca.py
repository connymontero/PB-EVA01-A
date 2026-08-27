from material import Material

class Biblioteca:
    # hereda de material
    def __init__(self):
        
        self.materiales = []

    def agregar_material(self, material):
        # append agrega un material al catalogo
        self.materiales.append(material)

    def mostrar_catalogo(self):
    
        print("--------- CATALOGO -----------")
        for material in self.materiales:
            # Polimorfismo = se ejecuta la descripcion de la subclase Material
            material.descripcion()
            print(f"Precio: ${material.get_precio()}")
            print("------------------------------")

    def mostrar_materiales(self):

        self.mostrar_catalogo()

    def sumar_precios(self):

        return sum(material.get_precio() for material in self.materiales)
    