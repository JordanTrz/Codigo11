//Registrar el ingreso de notas de 4 examenes y calcular el promedio de estos.

Proceso ejercicio_2
	Definir cantidad, promedio Como Real
	Escribir "Ingresar la cantidad de notas a promediar"
	Leer cantidad
	Dimension nota[cantidad] //No se puede declarar matriz sin definir. por eso debe ir después de definir "cantidad"
	para x=1 Hasta cantidad Hacer
		Escribir "Escribe la nota del examen #" x
		leer nota[x] 
		Mientras nota[x] < 0 | nota[x] > 20 Hacer // Si la nota ingresada es negativa o mayor a 20 no lo considera
			escribir "Nota inválida, valor debe estar entre 0 y 20"
			Escribir "vuelva a ingresar nota"
			leer nota[x]
		FinMientras
		promedio = promedio + nota[x]
	FinPara
	promedio = promedio/cantidad
	Escribir "El promedio de los " cantidad " exámenes es " promedio
		
FinProceso
