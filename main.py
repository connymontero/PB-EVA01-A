from biblioteca import Biblioteca
from libro import Libro
from periodico import Periodico
from revista import Revista

def main():
    # crea la biblioteca y los materiales solicitados
    biblioteca = Biblioteca()
    libro_1 = Libro("Necronomicon", "Howard Phillips Lovecraft", 35000, 300)
    libro_2 = Libro("Tony Ninguno", "Andres Montero", 16000, 140)
    revista = Revista("Evon", "Editorial Planeta", 1000, 8)
    periodico = Periodico("Pincoya", "Redaccion", 1000, "26/08/2026")
    
    print("=== DESCRIPCION BIBLIOTECA ===")
    for material in (libro_1, libro_2, revista, periodico):
        material.descripcion()
        print()

    # modifica el precio de un material mediante el setter encapsulado
    libro_1.set_precio(25000)

    # agrega todos los materiales al catalogo
    for material in (libro_1, libro_2, revista, periodico):
        biblioteca.agregar_material(material)

    # muestra el catalogo polimorfico y el total de sus precios
    biblioteca.mostrar_catalogo()
    print(f"Total del catalogo: ${biblioteca.sumar_precios()}")

#verifica que se ejecute main
if __name__ == "__main__":

    main()
