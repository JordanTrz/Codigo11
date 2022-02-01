capitales = {'Peru': 'Lima',
             'Ecuador' : 'Quito',
             'Chile' : 'Santiago',
             'Uruguay' : 'Montevideo'}

print(capitales)
capital = {'Brasil' : 'Brasilia'}
capitales.update(capital)
print(capitales)
c = capitales.pop('Bolivia','No existe el país')
print(c)
capitales2 = capitales.copy() # Se tiene que realizar la copia del diccionario
print(capitales2)

capitales.pop('Uruguay')
print(capitales)
print(capitales2)

# Existen 3 formas de poder recorrer un diccionario

for capital in capitales:
      print(capital, ":", capitales[capital])

print(capitales.keys())
print(capitales.values())

for clave in capitales.keys():
      print(clave, ":", capitales[clave])

for key,value in capitales.items():
  print(key, ":", value)
