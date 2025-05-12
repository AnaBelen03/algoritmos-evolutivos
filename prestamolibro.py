import pandas as pd


datos = {
    "Estudiante": ["Rosa", "David", "Elena", "Mario", "Paula"],
    "Días_prestamo": [7, 10, 5, 12, 3]
}

df = pd.DataFrame(datos)


print("Datos de préstamo:\n")
print(df)


print("\nResumen estadístico:")
print(df["Días_prestamo"].describe())

# Filtrar estudiantes con préstamo mayor a 8 días
mayores_a_8 = df[df["Días_prestamo"] > 8]

print("\nEstudiantes que retuvieron el libro más de 8 días:")
print(mayores_a_8)