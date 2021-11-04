// Determinar el sueldo semanal de un trabajador basándose en sus horas trabajadas y su salario de hora hombre

Proceso ejercicio_6
	salario()
FinProceso

funcion salario()
	definir salario_hora, horas_trabajadas Como Real
	
	Escribir "Calcular sueldo semanal de trabajador"
	Escribir "Ingrese el salario ganado por hora"
	Leer salario_hora
	Escribir "Ingrese las horas trabajadas por semana"
	Leer horas_trabajadas
	
	Escribir "El salario semanal es de S/" salario_hora*horas_trabajadas
FinFuncion
