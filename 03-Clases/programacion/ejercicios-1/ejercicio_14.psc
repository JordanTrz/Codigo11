// Una compañía, fabrica focos de colores (verdes, blancos y rojos). Se desea contabilizar, de un lote de N focos(matrices), el número de focos de cada color que hay en existencia. 

Proceso ejercicio_14
	focos()
FinProceso

Funcion focos()
	definir num,residuo,count Como Entero
	Dimension matriz[3]
	
	Escribir "Ingrese cantidad de focos en lote" //Se define la cantidad de focos que se tienen en lote"
	leer num
	
	Para x=1 Hasta 3 Hacer
		matriz[x] = azar(redon(num/3)) // Se crea al azar cantidad de focos para cada color
		residuo = residuo + matriz[x]
	FinPara
	
	residuo = num - residuo // como el "azar" hace que no siempre se llegue al valor del lote, se calcula el residuo"
	
	para x=1 hasta 3 Hacer
		matriz[x] = matriz[x] + redon(residuo/3) // El residuo se divide entre 3 y se suma a los 3 colores
		count = count + matriz[x]
	FinPara
	
	para x=-1 Hasta 1 Hacer // en momentos el residuo hará que no se llegue al total de focos, por lo que, si hay un desfase, se suma ese valor al primer índice
		si (num-count)== x Entonces
			matriz[1] = matriz[1]+x
		FinSi
	FinPara
	
	escribir "Cuenta con " matriz[1] " focos verdes"
	escribir "Cuenta con " matriz[2] " focos rojos"
	escribir "Cuenta con " matriz[3] " focos blancos"
FinFuncion
	