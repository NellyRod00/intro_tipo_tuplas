#Equipo Tuplas: Leonel Ruvalcaba, Nayeli Rodriguez, Manuel Quintero y Perla Torres

# Definimos una tupla con nombres
nombres = ("Ana", "Luis", "María", "Carlos")
print(f"la tupla de nombres es:\n{nombres}")    # Imprieme la tupla completa

    # Recorriendo la tupla con un for
print("Lista de nombres:")
for nombre in nombres:
    print(nombre)

    # Ejemplo con tupla de números
numeros = (10, 20, 30, 40, 50)
print(f"los números en la tupla son:\n{numeros}")  # Imprime la tupla completa

print("Números multiplicados por 2:")   # Recorrie la tupla y multiplicando cada número por 2
for n in numeros:
    print(n * 2)