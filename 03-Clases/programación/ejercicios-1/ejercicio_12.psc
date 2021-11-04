Proceso ejercicio_12
	Definir años Como Entero
	Definir salario Como Real
	salario = 1500
	años = 6
	Escribir "Salario recibido en 6 años"
	
	Para x=1 Hasta años-1 Hacer
		salario = salario + salario*0.1
		Escribir "Se recibió el salario de " salario " el año " x
	FinPara
	
	Escribir "Luego de 6 años, se recibió la cantidad de " salario+salario*0.1
FinProceso
