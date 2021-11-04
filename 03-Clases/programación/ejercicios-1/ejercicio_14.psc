Proceso ejercicio_14
	definir num,residuo,count Como Entero
	Dimension matriz[3]
	
	Escribir "cantidad de focos en lote"
	leer num
	
	Para x=1 Hasta 3 Hacer
		matriz[x] = azar(redon(num/3))
		residuo = residuo + matriz[x]
	FinPara
	
	residuo = num - residuo
	
	para x=1 hasta 3 Hacer
		matriz[x] = matriz[x] + redon(residuo/3)
		count = count + matriz[x]
	FinPara
	
	para x=-2 Hasta 2 Hacer
		si (num-count)== x Entonces
			matriz[1] = matriz[1]+x
		FinSi
	FinPara
		
	escribir "Cuenta con " matriz[1] " focos verdes"
	escribir "Cuenta con " matriz[2] " focos rojos"
	escribir "Cuenta con " matriz[3] " focos blancos"
	
FinProceso
