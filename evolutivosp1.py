import numpy as np
import matplotlib.pyplot as plt

# Rango de valores de x
x = np.linspace(0, 80, 400)

# Restricciones
y1 = (120 - 2 * x) / 3       # 2x + 3y <= 120
y2 = np.full_like(x, 5)      # y >= 5
x_lim = np.full_like(x, 10)  # x >= 10

# Crear la figura
plt.figure(figsize=(10, 7))

# Dibujar las restricciones
plt.plot(x, y1, label=r'$2x + 3y \leq 120$', color='blue')
plt.axhline(y=5, label=r'$y \geq 5$', color='green')
plt.axvline(x=10, label=r'$x \geq 10$', color='red')

# Región factible (relleno)
y = np.maximum(5, 0)
plt.fill_between(x, y, np.minimum(y1, 100), where=(x >= 10) & (y1 >= 5), color='gray', alpha=0.3, label='Región factible')

# Evaluamos puntos extremos (vértices)
# Intersección de 2x + 3y = 120 con x = 10
x1, y1_val = 10, (120 - 2 * 10) / 3

# Intersección de 2x + 3y = 120 con y = 5
x2, y2_val = (120 - 3 * 5) / 2, 5

# Intersección de x=10 con y=5
x3, y3_val = 10, 5

# Mostrar vértices
vertices = [(x1, y1_val), (x2, y2_val), (x3, y3_val)]
for vx, vy in vertices:
    z = 50 * vx + 80 * vy
    plt.plot(vx, vy, 'ko')
    plt.text(vx + 0.5, vy + 0.5, f'Z={z:.0f}', fontsize=9)

# Etiquetas
plt.xlabel('x (unidades de A)')
plt.ylabel('y (unidades de B)')
plt.title('Optimización gráfica de producción de artesanías')
plt.legend()
plt.grid(True)
plt.xlim(0, 50)
plt.ylim(0, 50)
plt.show()
