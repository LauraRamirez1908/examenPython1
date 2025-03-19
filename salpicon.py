frutas = []
contador = 0

print("Registro de frutas para el salpicón 🍉🍍🍎")
print("****************************************")

# Ingreso de 10 frutas usando while
while contador < 10:
    print(f"\nFruta {contador + 1}:")
    nombre = input("Nombre de la fruta: ")
    precio = float(input("Precio de la fruta: "))

    fruta = {"nombre": nombre, "precio": precio}  # Diccionario con los datos de la fruta
    frutas.append(fruta)  # Agregamos a la lista
    contador += 1  # Incrementamos el contador

# Ordenar las frutas por precio de mayor a menor usando burbuja y while
n = len(frutas)
i = 0
while i < n - 1:
    j = 0
    while j < n - i - 1:
        if frutas[j]["precio"] < frutas[j + 1]["precio"]:  # Si la fruta actual es más barata, intercambiamos
            frutas[j], frutas[j + 1] = frutas[j + 1], frutas[j]
        j += 1
    i += 1

# Mostrar la lista ordenada
print("\nFrutas ordenadas de mayor a menor precio:")
for fruta in frutas:
    print(f"{fruta['nombre']} - ${fruta['precio']:.2f}")
