
# 1. Definición de la tupla de prendas
prendas_de_vestir = ("Camisa", "Pantalón", "Chaqueta", "Calcetines", "Bufanda", "Gorro")

# 2. Inicialización del índice
i = 0

# 3. Uso del bucle 'while'
print("--- Armario de Prendas (Recorrido por índice) ---")

# El bucle se ejecuta mientras el índice (i) sea menor que la longitud total de la tupla
while i < len(prendas_de_vestir):
    # Accedemos a la prenda en la posición actual
    prenda_actual = prendas_de_vestir[i]

    # Imprimimos el índice (posición) y la prenda
    print(f"Posición {i}: {prenda_actual}")

    # ¡Super importantisimo! Vamos a incrementar el índice para avanzar a la siguiente prenda
    i += 1

print("--- Inventario Completo ---")