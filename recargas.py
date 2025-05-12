import numpy as np

# Paso 1: Crear arrays de GB y precios
gb = np.array([1, 2, 5, 10])
precios = np.array([5, 9, 20, 35])

# Paso 2: Calcular el costo por GB
costo_por_gb = precios / gb
print("Costo por GB:", costo_por_gb)

# Paso 3: Encontrar el paquete más económico por GB
min_costo = np.min(costo_por_gb)
indice_min = np.argmin(costo_por_gb)

print(f"\nEl paquete más económico por GB es el de {gb[indice_min]} GB")
print(f"Precio: S/ {precios[indice_min]} — Costo por GB: S/ {min_costo:.2f}")
