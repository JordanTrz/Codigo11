// Realice un algoritmo para determinar si una persona puede votar con base en su edad en las próximas elecciones. 

Proceso ejercicio_15
	votacion()
FinProceso

Funcion votacion()
	definir a Como Entero
	
	Escribir "Ingrese su edad"
	leer a
	a = a + 5 // sumo 5 ya que las próximas elecciones presidenciales se realizarán en 5 años
	si a>=18 & a<=70 Entonces // las personas que hoy tienen 13 años, en 5 años podrán votar ya que tendrán 18 años
		Escribir "Si podrá votar en las próximas elecciones presidenciales"
	SiNo
		Escribir "No cumples con el rango de edad para votar"
	FinSi
FinFuncion
	