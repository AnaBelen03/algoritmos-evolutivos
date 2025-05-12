import numpy as np
presupuesto = 8.00
precio = np.array([0.10, 0.12 ,0.08])
paginas = np.floor(presupuesto/precio)

for i, cant in enumerate(paginas):
    print(f"En la copisteria {i+1} se puede sacar {int(cant)} paginas")

mejoropc = np.argmax(paginas)
print(f" la mejor ocion sera la copisteria{mejoropc +1} porque se puede sacar {int(paginas[mejoropc])}paginas ")