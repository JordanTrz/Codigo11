# crear clase
class Automovil:
  # crear atributos
  def __init__(self,aa,pl,col,mar):
    self.año = aa
    self.placa = pl
    self.color = col
    self.marca = mar
    self.motor = 1000

  def encender(self):
    print('encender' + self.marca)

  def avanzar(self):
    print('avanzar' + self.marca)

  def acelerar(self):
    print('acelerar' + self.marca)

  def frenar(self):
    print('frenar' + self.marca)

# crear objetos
vw = Automovil(1970, 'CH-1234', 'Amarillo', 'Volkswagen')
tico = Automovil(1985, 'EJ-2345', 'Rojo', 'Tico')
lamborghini = Automovil(2018, 'E7P-367','Amarillo','Lamborgini')

# Utilizar objetos
vw.encender()
print("la placa es: " + vw.placa)
vw.acelerar()
vw.frenar()

tico.encender()
tico.acelerar()
tico.frenar()

lamborghini.encender()
lamborghini.acelerar()
lamborghini.frenar()

print("el color del automovil" + vw.marca + " ahora es " + vw.color)
vw.color = 'NEGRO'
print("el color del automovil " + vw.marca + " ahora es " + vw.color)
print("el color del automovil " + vw.marca + " ahora es " + str(vw.motor))
# del vw.motor
# print("el color del automovil " + vw.marca + " ahora es " + str(vw.motor))