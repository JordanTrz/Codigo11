// Realice un algoritmo para determinar si una persona puede votar con base en su edad en las pr�ximas elecciones. 

Proceso ejercicio_15
	votacion()
FinProceso

Funcion votacion()
	definir a Como Entero
	
	Escribir "Ingrese su edad"
	leer a
	a = a + 5 // sumo 5 ya que las pr�ximas elecciones presidenciales se realizar�n en 5 a�os
	si a>=18 & a<=70 Entonces // las personas que hoy tienen 13 a�os, en 5 a�os podr�n votar ya que tendr�n 18 a�os
		Escribir "Si podr� votar en las pr�ximas elecciones presidenciales"
	SiNo
		Escribir "No cumples con el rango de edad para votar"
	FinSi
FinFuncion
	