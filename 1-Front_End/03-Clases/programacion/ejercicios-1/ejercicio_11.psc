// Se les dará un bono por antigüedad a los empleados de una tienda. Si tienen un año, se les dará $100; si tienen 2 años, $200, y así sucesivamente hasta los 5 años. Para los que tengan más de 5, el bono será de $1000. Realice un algoritmo y represéntelo ,que permita determinar el bono que recibirá un trabajador

Proceso ejercicio_11
	bono()
FinProceso

Funcion bono()
	Definir años Como Entero
	Escribir "Indique cuántos años viene trabajando en la empresa"
	leer a
	Si (a>0 & a<6) Entonces // si el valor está en el rango de 1 a 5 se multiplica el año por $100
		Escribir "Recibirá el bono de $" a*100
	SiNo
		Escribir "Recibirá el bono de $1000" // a todos lo que tengan más de 6 años de antiguedad, se les dará $1000 de bono
	FinSi
FinFuncion
	