def decorador(func):
  def envoltura():
    print("Esto se añade a mi función original")
    func()
  return envoltura

def mayusculas(func):
  def wrapper(texto):
        return func(texto).upper()
  return wrapper

# @decorador
# def saludo():
#       print('Hola Mundo')

# saludo()

@mayusculas
def mensaje(nombre):
  return 'Hola ' + nombre

print(mensaje("cesar"))