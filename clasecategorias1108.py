class alumno1108:
    id_Categoria = 0
    Nombre = " "
    Descripcion = " "
    Fecha_creacion = 0
    Estado = ""
    Orden = 0
    Marca = " "

    def mostrardatos1108(self,n):
        print(f"ID Categoría: {n}")
        print(f"Nombre: {n}")
        print(f"Descripción: {n}")
        print(f"Fecha de Creación: {n}")
        print(f"Estado: {n}")
        print(f"Orden: {n}")
        print(f"Marca: {n}")
class Informacion:
        def Lista_Categorias1108(self):
            ListaCa1108 = {"Lienzo","Descripcion","Fecha de creacion","Estado", "Orden"}
            for x in ListaCa1108:
                print(x)
        def Tupla_Catergorias1108(self):
            TuplaCa = ("Lienzo","Descripcion","Fecha de creacion","Estado", "Orden")
            for x in TuplaCa:
                print(x)
        def Diccionario_Categorias1108(self):
            diccionario = {
            "Lienzo": "Buen estado",
            "Descripcion": "Lienzo de color blanco",
            "Fecha de creacion": "19 de mayo del 2024",
            "Estado: ": "Chihuahua",
            "Orden": "Dia 23 de julio",
            }
            for x, y in diccionario.items():
                print(x, y)
        def Altas_Categoria(self):
            print("Se dio de alta correctamente su compra")
        def Bajas_Categoria(self):
            print("Se dio de baja correctamente su compra")
# Ejemplo de uso
producto=alumno1108()
# 
producto.id_Categoria = 10215448
producto.Nombre = "Lienzo"
producto.Descripcion = "Cuadro grande de color blanco"
producto.Fecha_creacion = "20/19/21"
producto.Estado = "Bueno"
producto.Orden = 12454
producto.Marca = "Paintiny"
print(f"ID Categoría: {producto.id_Categoria}")
print(f"Nombre: {producto.Nombre}")
print(f"Descripción: {producto.Descripcion}")
print(f"Fecha de Creación: {producto.Fecha_creacion}")
print(f"Estado: {producto.Estado}")
print(f"Orden: {producto.Orden}")
print(f"Marca: {producto.Marca}")
#
datos=Informacion()
print("")
print("Lista:")
datos.Lista_Categorias1108()
print("")
print("Tupla:")
datos.Tupla_Catergorias1108()
print("")
print("Diccionario:")
datos.Diccionario_Categorias1108()
print("")
print("Funcion de altas:")
datos.Altas_Categoria()
print("")
print("Funcion de bajas:")
datos.Bajas_Categoria()
