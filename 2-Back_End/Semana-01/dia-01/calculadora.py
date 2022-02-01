# Programa para poder calcular temperatura

# Inputs
a = input("Ingrese el primer valor: ")
while(not a.isnumeric()):
      print("Solo se acepta valores numéricos")
      a = input("Ingrese el primer valor: ")

b = input("Ingrese el segundo valor: ")
while(not b.isnumeric()):
      print("Solo se acepta valores numéricos")
      b = input("Ingrese el segundo valor: ")

# tipoCalculo = input("Ingrese qué tipo de cálculo desea realizar \n"
#                     "A: Suma \n"
#                     "B: Resta \n"
#                     "C: Multiplicación \n"
#                     "D: División \n")

tipoCalculo = input("""Ingrese qué tipo de cálculo desea realizar
                    A: Suma
                    B: Resta
                    C: Multiplicación
                    D: División""")

# Proceso
while(tipoCalculo != "A" and tipoCalculo != "B" and tipoCalculo != "C" and tipoCalculo != "D"):
      print("Opción inválida, ingrese una de las siguientes opciones: ")
      tipoCalculo = input("Ingrese qué tipo de cálculo desea realizar \n"
                    "A: Suma \n"
                    "B: Resta \n"
                    "C: Multiplicación \n"
                    "D: División \n")

# Output
if(tipoCalculo == "A"):
    c = float(a)+float(b)
    print("La suma de " + str(a) + " y " + str(b) + " es: " + str(c))
elif(tipoCalculo == "B"):
    c = float(a)-float(b)
    print("La resta de " + str(a) + " y "  + str(b) + " es: " + str(c))
elif(tipoCalculo == "C"):
    c = float(a)*float(b)
    print("La multiplicación de " + str(a) + " y "  + str(b) + " es: " + str(c))
elif(tipoCalculo == "D"):
    c = float(a)/float(b)
    print("La división de " + str(a) + " y "  + str(b) + " es: " + str(c))
else:
      print("Error")