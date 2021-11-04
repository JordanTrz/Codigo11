// Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años. ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años? Realice el algoritmo y representan la solución, utilizando el ciclo apropiado.

Proceso ejercicio_12
	salario_total()
FinProceso

Funcion salario_total()
	Definir años Como Entero
	Definir salario Como Real
	salario = 1500
	años = 6
	Escribir "Salario recibido en 6 años"
	
	Para x=1 Hasta años-1 Hacer
		salario = salario + salario*0.1 // El salario aumento 10% CADA AÑO, por lo que el siguiente año se debe calcular el 10% en base al aumentado el año anterior
		Escribir "Se recibió el salario de " salario " el año " x
	FinPara
	
	Escribir "Luego de 6 años, se recibirá la cantidad de " salario+salario*0.1
FinFuncion
	