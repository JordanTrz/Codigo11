# Realizar programa que te pida ingresar una cantidad de números
# El programa debe pedirte cuántos números ingresar
# Al final debe mostrar el número mayor, menor y el promedio
# Y debe mostrar todos los números ordenados en una tupla

entrada = int(input("Ingrese la cantidad de números a ingresar: "))
valores = []

for i in range(entrada):
  valores.append(int(input("ingrese el valor #" + str(i+1) + ": ")))

print("El número mayor es : ", max(valores))
print("El número menor es : ", min(valores))
print("El promedio es     : ", sum(valores)/len(valores))
valores2 = sorted(tuple(valores))
print(valores2)