import numpy as np


presupuesto = 15.00  # soles
precios = np.array([2.50, 3.00, 1.80])  
viajes = np.floor(presupuesto / precios)


medios = ["bus", "combi", "tren"]

for i, cant in enumerate(viajes):
    print(f"Con {medios[i]} puede hacer {int(cant)} viajes.")


mejoropc = np.argmax(viajes)
print(f"\nLa mejor opción es el {medios[mejoropc]}, con {int(viajes[mejoropc])} viajes.")