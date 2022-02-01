import locale
# locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
locale.setlocale(locale.LC_ALL, '')

# Conversor de monedas

# Datos de entrada
cambioDolar = [4.1,4.2,4.3,4.4,4.5]
monedaInicial = input ("Ingrese moneda a convertir: \n"
                       "A: Dólares \n"
                       "B: Euros \n")
print(monedaInicial)
while(monedaInicial != "A" and monedaInicial != "B"):
  print("Valor ingresado erróneo")
  monedaInicial = input ("Ingrese moneda a convertir: \n"
                       "A: Dólares \n"
                       "B: Euros \n")
if(monedaInicial == "A"):
  montoInicial = float(input("ingrese el monto en dólares: "))
  montoInicialFormato = "${:.1f}".format(montoInicial)
  tipoCambio = 4.067
elif(monedaInicial == "B"):
  montoInicial = float(input("ingrese el monto en Euros: "))
  montoInicialFormato = "€{:.1f}".format(montoInicial)
  tipoCambio = 4.886
else:
  print("No selecciono una moneda válida")
  # quit()
# Proceso
montoFinal = montoInicial*tipoCambio

# Datos de Salida
print("El monto de " + montoInicialFormato + " es igual a " + locale.currency(montoFinal))
print("===== Cambio de dólares =====")
for cambio in cambioDolar:
  print(cambio*montoInicialFormato)