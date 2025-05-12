import pandas as pd

# Paso 1: Crear el DataFrame con la lista de gastos
gastos = [4.0, 3.5, 5.0, 4.2, 3.8]
df = pd.DataFrame({'Gasto': gastos}, index=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'])

# Paso 2: Calcular el gasto total y el gasto medio
gasto_total = df['Gasto'].sum()
gasto_medio = df['Gasto'].mean()

# Mostrar resultados
print("Gasto total de la semana:", gasto_total)
print("Gasto medio diario:", gasto_medio)

# Paso 3: Identificar los días con gasto mayor que el promedio
dias_mayor_promedio = df[df['Gasto'] > gasto_medio]

print("\nDías con gasto mayor al promedio:")
print(dias_mayor_promedio)
