#Equipo Tuplas: Leonel Ruvalcaba, Nayeli Rodriguez, Manuel Quintero y Perla Torres

# Definimos una lista con frutas
frutas = ("manzana", "banana", "cereza", "uva")
print(f"La tupla de frutas es:\n{frutas}")  # Imprime la tupla completa

# Usamos while para recorrer
inicia = 0 
print("Recorriendo la tupla con while:") 

while inicia < len(frutas):
    print(f"En la posición {inicia}: {frutas[inicia]}") # Imprime cada fruta con su posición
    inicia += 1 # Incrementa el índice