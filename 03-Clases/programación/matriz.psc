Proceso matriz
	Dimension datos[4]
	dimension datoSuma[4]
	datos[1] = 0
	datos[2] = 1
	datos[3] = 2
	datos[4] = 3
	
	Escribir "El primer dato es " datos[1]
	Escribir "El segundo dato es " datos[2]
	
	para x=1 hasta 4 Con Paso 1 Hacer
		Escribir "Posición " x " = " datos[x]
		datoSuma[x] = x + 10
	FinPara
	
	para x=1 hasta 4 con paso 1 Hacer
		Escribir "Posicion datosuma " x " = " datoSuma[x]
	FinPara
	
FinProceso
