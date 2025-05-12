import numpy as np
import copy

# Matriz de distancias (en minutos)
distancias = np.array([
    [0, 4, 1, 9, 3, 10],
    [4, 0, 6, 7, 2, 8],
    [1, 6, 0, 5, 4, 3],
    [9, 7, 5, 0, 6, 2],
    [3, 2, 4, 6, 0, 7],
    [10, 8, 3, 2, 7, 0]
])

def calcular_tiempo_total(ruta, distancias):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancias[ruta[i]][ruta[i + 1]]
    return total


def generar_vecinos(ruta):
    vecinos = []
    for i in range(1, len(ruta) - 2):  
        vecino = ruta.copy()
        vecino[i], vecino[i + 1] = vecino[i + 1], vecino[i]
        vecinos.append(vecino)
    return vecinos

ruta_actual = [0, 1, 2, 3, 4, 5, 0]
tiempo_actual = calcular_tiempo_total(ruta_actual, distancias)

mejorado = True
while mejorado:
    mejorado = False
    vecinos = generar_vecinos(ruta_actual)
    
    for vecino in vecinos:
        tiempo_vecino = calcular_tiempo_total(vecino, distancias)
        if tiempo_vecino < tiempo_actual:
            ruta_actual = vecino
            tiempo_actual = tiempo_vecino
            mejorado = True
            break  # Aplica mejora e inicia otra iteración

# Resultado final
print("Ruta óptima aproximada:", ruta_actual)
print("Tiempo total:", tiempo_actual, "minutos")
