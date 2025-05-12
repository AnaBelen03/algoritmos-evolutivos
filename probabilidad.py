import random
import math

# Lista de materias
materias = ["Mate", "Historia", "Física", "Lengua", "Química"]

# Puntajes de fatiga entre materias (por simplicidad, un diccionario simétrico)
fatiga = {
    ("Mate", "Historia"): 3,
    ("Mate", "Física"): 2,
    ("Mate", "Lengua"): 5,
    ("Mate", "Química"): 4,
    ("Historia", "Física"): 3,
    ("Historia", "Lengua"): 2,
    ("Historia", "Química"): 5,
    ("Física", "Lengua"): 4,
    ("Física", "Química"): 1,
    ("Lengua", "Química"): 3
}

# Función para obtener la fatiga entre dos materias
def obtener_fatiga(a, b):
    if a == b:
        return 0
    return fatiga.get((a, b)) or fatiga.get((b, a))

# Función para calcular el costo total de una secuencia
def costo_total(secuencia):
    return sum(obtener_fatiga(secuencia[i], secuencia[i+1]) for i in range(len(secuencia)-1))
# Simulated Annealing
secuencia_actual = materias.copy()
random.shuffle(secuencia_actual)
mejor_secuencia = secuencia_actual.copy()
mejor_costo = costo_total(mejor_secuencia)

T_inicial = 10
T_final = 1
iteraciones = 100

for i in range(iteraciones):
    T = T_inicial - (i * (T_inicial - T_final) / iteraciones)
    
    # Generar vecino intercambiando dos materias al azar
    vecino = secuencia_actual.copy()
    a, b = random.sample(range(len(vecino)), 2)
    vecino[a], vecino[b] = vecino[b], vecino[a]
    
    costo_vecino = costo_total(vecino)
    delta = costo_vecino - costo_total(secuencia_actual)

    # Criterio de aceptación
    if delta < 0 or random.random() < math.exp(-delta / T):
        secuencia_actual = vecino
        if costo_vecino < mejor_costo:
            mejor_costo = costo_vecino
            mejor_secuencia = vecino

# Resultado final
print("Mejor secuencia encontrada:", mejor_secuencia)
print("Costo total de fatiga:", mejor_costo)
