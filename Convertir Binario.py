import numpy as np
cedula = np.array([1, 2, 0, 5, 4, 5, 9, 0, 1])
sumai = np.sum(cedula[1:8:2])
sumap = np.sum(cedula[0:9:2])
print("Los valores en las posiciones pares son", cedula[0:9:2])
print("Los valores en las posiciones impares son", cedula[1:8:2])
print(cedula[1:8:2])
print("Suma pares", sumai)
sumap = cedula[0:9:2] * 2
for i in range(0, len(sumap)):
    if sumap[i] > 9:
        sumap[i] -= 9
print(sumap)
sumap = np.sum(sumap)
print(sumap)
sumatotal = sumai + sumap
udc = sumatotal % 10 - 10
print(udc)