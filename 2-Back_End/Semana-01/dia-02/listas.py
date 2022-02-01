dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes","Sabado","Domingo"]
primos = [2,3,5,7,11,13]



print(dias[0])
print(len(dias))
print(primos)
primos.append(17)
print(primos)
primos.pop()
print(primos)
dias[0] = "Lunes"
print(dias)

for dia in dias:
  print("dia: " + dia)

for dia in range(len(dias)):
  print(dias[dia])