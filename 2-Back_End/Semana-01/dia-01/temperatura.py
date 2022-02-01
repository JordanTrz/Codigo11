# Programa para poder calcular temperatura

# Inputs
a = input("Ingrese la temperatura en celcius: ")
while(not a.isnumeric()):
      print("Solo se acepta valores numéricos")
      a = input("Ingrese la temperatura en celcius: ")

tipoCalculo = input("Ingrese a qué escala quiere convertir \n"
                    "A: Farenheit \n"
                    "B: Kelvin \n"
                    "C: Rankine \n")

# Proceso
while(tipoCalculo != "A" and tipoCalculo != "B" and tipoCalculo != "C"):
      print("Opción inválida, ingrese una de las siguientes opciones: ")
      tipoCalculo = input("Ingrese a qué escala quiere convertir \n"
                    "A: Farenheit \n"
                    "B: Kelvin \n"
                    "C: Rankine \n")

# Output
if(tipoCalculo == "A"):
    c = "{:.1f}".format((float(a)*9/5)+32)
    print("La conversión de " + str(a) + "°C a Farenheit es " + str(c) + "°F")
elif(tipoCalculo == "B"):
    c = "{:.1f}".format(float(a)+273.15)
    print("La conversión de " + str(a) + "°C a Kelvin es " + str(c) + "K")
elif(tipoCalculo == "C"):
    c = "{:.1f}".format((float(a)*9/5)+491.67)
    print("La conversión de " + str(a) + "°C a Kelvin es " + str(c) + "°R")
else:
      print("Error")