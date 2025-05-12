import numpy as np

# Paso 1: Crear arrays para GB y precios
gb = np.array([1, 2, 5, 10])
precios = np.array([5, 9, 20, 35])

# Calcular el costo por GB para cada paquete
costo_por_gb = precios / gb
print("Costo por GB:", costo_por_gb)

# Paso 2: Encontrar el paquete más económico en precio por GB
min_costo = np.min(costo_por_gb)
indice_min = np.argmin(costo_por_gb)
mejor_paquete = (gb[indice_min], precios[indice_min])

print("Paquete más económico en S/ por GB:", mejor_paquete)
print("Costo mínimo por GB:", min_costo)
