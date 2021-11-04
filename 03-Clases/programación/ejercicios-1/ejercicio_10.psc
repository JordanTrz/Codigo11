// Se tiene el nombre y la edad de tres personas. Se desean saber el nombre y la edad de la persona de menor edad. 

Proceso ejercicio_10
	menor_edad()	
FinProceso

Funcion menor_edad()
	definir cantidad, i Como Entero
	Escribir "Ingrese cantidad de personas"
	leer cantidad
	Dimension nombre[cantidad], edad[cantidad] // Se define la matriz según la cantidad de personas ingresada
	Escribir "Qué persona tiene menor edad?"
	
	para x=1 Hasta cantidad Hacer // Se pide en bucle los nombres y edades de las personas
		Escribir "Ingrese nombre y edad de la persona #" x
		leer nombre[x], edad[x]
	FinPara
	i = 1
	para x=1 Hasta cantidad Hacer // Se busca qué persona es la de menor edad y se guarda su índice
		si edad[x] < edad[i]
			i = x
		SiNo
			i=i
		FinSi
	FinPara
	Escribir "La persona con menor edad es " nombre[i] " ya que tiene " edad[i] " años"
	
FinFuncion
	