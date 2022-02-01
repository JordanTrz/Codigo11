// Realice un algoritmo para leer las calificaciones de N alumnos y determine el número de aprobados y reprobados.

Proceso ejercicio_13
	definir alumnos, nota, aprobado Como Entero
	
	Escribir "Ingrese la cantidad de alumnos"
	Leer alumnos
	Dimension notas[alumnos] // matriz definida según cantidad ingresada de alumnos
	
	para x=1 Hasta alumnos Hacer
		Escribir "Ingrese la nota del alumno #" x
		Leer nota
		
		Mientras nota<0 | nota>20 Hacer // Si la nota no se encuentra entre 0 a 20 salta mensaje error
			Escribir "nota incorrecta, ingresar valor entre 0 y 20"
			Leer nota
		Fin Mientras
		
			notas[x]=nota
			si notas[x] > 10.5 Entonces // Si la nota es mayor a 10.5 se considera aprobado
				aprobado = aprobado + 1
			FinSi
	FinPara
	
	Escribir "Número de alumnos aprobados: " aprobado
	Escribir "Número de alumnos desaprobados: " alumnos-aprobado
FinProceso
