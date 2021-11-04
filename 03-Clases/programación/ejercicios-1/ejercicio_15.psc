Proceso ejercicio_15
	definir edad Como Entero
	
	Escribir "Ingrese su edad"
	leer edad
	votacion(edad)
	
FinProceso

Funcion votacion(a)
	a = a+ 5
	si a>=18 & a<=70 Entonces
		Escribir "Si podrá votar en las próximas elecciones presidenciales"
	SiNo
		Escribir "No cumples con el rango de edad para votar"
	FinSi
FinFuncion
	