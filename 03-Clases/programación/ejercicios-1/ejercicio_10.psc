Proceso ejercicio_10
	Definir edad_1, edad_2, edad_3 Como Entero
	Definir nombre_1, nombre_2, nombre_3 Como Caracter
	Escribir "Saber qu� persona tiene menor edad"
	Escribir "Ingrese nombre y edad"
	Leer nombre_1
	Leer edad_1
	
	Escribir "Ingrese nombre y edad"
	Leer nombre_2
	Leer edad_2
	
	Escribir "Ingrese nombre y edad"
	Leer nombre_3
	Leer edad_3
	
	Si edad_1 < edad_2 Entonces
		si edad_1 < edad_3 Entonces
			Escribir "La persona con menor edad es " nombre_1 " ya que tiene " edad_1 " a�os"
		SiNo
			Escribir "La persona con menor edad es " nombre_3 " ya que tiene " edad_3 " a�os"
		FinSi
	SiNo
		si edad_2 < edad_3 Entonces
			Escribir "La persona con menor edad es " nombre_2 " ya que tiene " edad_2 " a�os"
		SiNo
			Escribir "La persona con menor edad es " nombre_3 " ya que tiene " edad_3 " a�os"
		FinSi
	Fin Si
	
FinProceso
