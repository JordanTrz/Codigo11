Proceso funciones
	Definir a,b Como Entero
	Definir operacion Como Caracter
	
	Escribir "Por favor ingrese el primer n�mero"
	leer a
	
	Escribir "Por favor ingrese el segundo n�mero"
	leer b
	
	Escribir "Por favor ingrese la operaci�n *,/,-,+"
	leer operacion
	
	Segun operacion Hacer
		"+":
			Suma(a,b)
		"-":
			Resta(a,b)
		"*":
			multiplicacion(a,b)
		"/":
			division(a,b)
		De Otro Modo:
			Escribir "Por favor ingrese un operador valido"
	Fin Segun
	
FinProceso

Funcion Suma(a,b)
	Imprimir a + b
FinFuncion

Funcion Resta(a,b)
	Imprimir a - b
FinFuncion

Funcion multiplicacion(a,b)
	Imprimir a*b
FinFuncion

Funcion division(a,b)
	imprimir a/b
FinFuncion
	