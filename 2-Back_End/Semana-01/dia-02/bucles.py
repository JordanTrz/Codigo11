while(True):
  entrada = int(input("Ingrese la tabla de multiplicar: "))
  for i in range(10):
    c = i*entrada
    print(entrada, "x", i, "es: ", c)
  if(entrada == 999):
    break