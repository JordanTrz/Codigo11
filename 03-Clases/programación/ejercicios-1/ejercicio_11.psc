Proceso ejercicio_11
	Definir a�os Como Entero
	
	Escribir "Indique cu�ntos a�os viene trabajando en la empresa"
	leer a�os
	bono(a�os)
FinProceso

Funcion bono(a)
	Si (a>0 & a<6) Entonces
		Escribir "Recibir� el bono de $" a*100
	SiNo
		Escribir "Recibir� el bono de $1000" 
	FinSi
FinFuncion
	