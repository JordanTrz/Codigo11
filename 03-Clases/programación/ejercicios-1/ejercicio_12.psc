// Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 a�os. �Cu�l es su salario al cabo de 6 a�os? �Qu� salario ha recibido en cada uno de los 6 a�os? Realice el algoritmo y representan la soluci�n, utilizando el ciclo apropiado.

Proceso ejercicio_12
	salario_total()
FinProceso

Funcion salario_total()
	Definir a�os Como Entero
	Definir salario Como Real
	salario = 1500
	a�os = 6
	Escribir "Salario recibido en 6 a�os"
	
	Para x=1 Hasta a�os-1 Hacer
		salario = salario + salario*0.1 // El salario aumento 10% CADA A�O, por lo que el siguiente a�o se debe calcular el 10% en base al aumentado el a�o anterior
		Escribir "Se recibi� el salario de " salario " el a�o " x
	FinPara
	
	Escribir "Luego de 6 a�os, se recibir� la cantidad de " salario+salario*0.1
FinFuncion
	