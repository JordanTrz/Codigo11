Proceso ejercicio_11
	Definir años Como Entero
	
	Escribir "Indique cuántos años viene trabajando en la empresa"
	leer años
	bono(años)
FinProceso

Funcion bono(a)
	Si (a>0 & a<6) Entonces
		Escribir "Recibirá el bono de $" a*100
	SiNo
		Escribir "Recibirá el bono de $1000" 
	FinSi
FinFuncion
	