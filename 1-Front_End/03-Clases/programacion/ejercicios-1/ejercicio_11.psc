// Se les dar� un bono por antig�edad a los empleados de una tienda. Si tienen un a�o, se les dar� $100; si tienen 2 a�os, $200, y as� sucesivamente hasta los 5 a�os. Para los que tengan m�s de 5, el bono ser� de $1000. Realice un algoritmo y repres�ntelo ,que permita determinar el bono que recibir� un trabajador

Proceso ejercicio_11
	bono()
FinProceso

Funcion bono()
	Definir a�os Como Entero
	Escribir "Indique cu�ntos a�os viene trabajando en la empresa"
	leer a
	Si (a>0 & a<6) Entonces // si el valor est� en el rango de 1 a 5 se multiplica el a�o por $100
		Escribir "Recibir� el bono de $" a*100
	SiNo
		Escribir "Recibir� el bono de $1000" // a todos lo que tengan m�s de 6 a�os de antiguedad, se les dar� $1000 de bono
	FinSi
FinFuncion
	