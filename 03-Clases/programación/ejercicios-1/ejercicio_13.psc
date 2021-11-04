Proceso ejercicio_13
	definir alumnos, nota, aprobado Como Entero
	
	Escribir "Ingrese la cantidad de alumnos"
	Leer alumnos
	Dimension notas[alumnos]
	
	para x=1 Hasta alumnos Hacer
		Escribir "Ingrese las notas de los " alumnos " alumnos"
		Leer nota
			notas[x]=nota
			si notas[x] > 10.5 Entonces
				aprobado = aprobado + 1
			FinSi
	FinPara
	
	
	
	Escribir "El número de alumnos aprobados es " aprobado
	Escribir "El número de alumnos desaprobados es " alumnos-aprobado
FinProceso
