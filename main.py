import random

helados = []
id_existentes = []  

opcion = 100

def generar_id():
    while True:
        nuevo_id = random.randint(1000, 9999)  # Genera un ID de 4 dígitos
        if nuevo_id not in id_existentes:
            id_existentes.append(nuevo_id)  # Agregamos el ID a la lista
            return nuevo_id

print("Gestión de Helados")
print("******************")
print("1. Crear helado")
print("2. Ver lista de helados")
print("3. Editar helado")
print("4. Eliminar helado")
print("Presiona 5 para salir")

while opcion != 5:
    opcion = int(input("Digita una opción: "))
    if opcion == 1:
        print("Creación de un nuevo helado")
        
        helado = {}
        helado["id"] = generar_id()
        helado["nombre"] = input("Digita el nombre del helado: ")
        helado["descripcion"] = input("Digita la descripción del helado: ")
        helado["precio"] = float(input("Digita el precio del helado: "))
        
        helados.append(helado)  # Agregar a la lista
        print(f"Helado agregado exitosamente con ID {helado['id']}!\n")
        
    elif opcion == 2:
        print("Lista de Helados:")
        for heladoSeleccionado in helados:
            print(f"ID: {heladoSeleccionado['id']}, Nombre: {heladoSeleccionado['nombre']}, Descripción: {heladoSeleccionado['descripcion']}, Precio: ${heladoSeleccionado['precio']:.2f}")
        print()
        
    elif opcion == 3:
        id_cambio = int(input("Digita el ID del helado a modificar: "))
        for heladoBuscado in helados:
            if heladoBuscado["id"] == id_cambio:
                print("Helado encontrado! Modificando...")
                heladoBuscado["nombre"] = input(f"Nuevo nombre ({heladoBuscado['nombre']}): ") or heladoBuscado["nombre"]
                heladoBuscado["descripcion"] = input(f"Nueva descripción ({heladoBuscado['descripcion']}): ") or heladoBuscado["descripcion"]
                nuevo_precio = input(f"Nuevo precio (${heladoBuscado['precio']:.2f}): ")
                if nuevo_precio:
                    heladoBuscado["precio"] = float(nuevo_precio)
                print("Helado actualizado!\n")
                break
        else:
            print("No se encontró un helado con ese ID.\n")
        
    elif opcion == 4:
        id_eliminar = int(input("Digita el ID del helado a eliminar: "))
        for i, heladoBuscado in enumerate(helados):
            if heladoBuscado["id"] == id_eliminar:
                del helados[i]
                id_existentes.remove(id_eliminar)  # Eliminar el ID de la lista
                print("Helado eliminado exitosamente!\n")
                break
        else:
            print("No se encontró un helado con ese ID.\n")
        
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta nuevamente.\n")
