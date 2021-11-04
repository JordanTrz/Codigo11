// Una modista, para realizar sus prendas de vestir, encarga las telas al extranjero. Para cada pedido, tiene que proporcionar las medidas de la tela en pulgadas, pero ella generalmente las tiene en metros. Realice un algoritmo para ayudar a resolver el problema, determinando cuantas pulgadas debe pedir con base en los metros que requiere. (1 pulgada = 0.0254 m).

Proceso ejercicio_7
	pulgada_metros()
FinProceso

Funcion pulgada_metros()
	Definir metros_pedido Como Real
	
	Escribir "Calcular pulgadas"
	Escribir "Ingresar los metros que utilzará para calcular las pulgadas"
	Leer metros_pedido
	
	Escribir "Se debe pedir la siguiente cantidad en pulgadas: " metros_pedido*39.3701
FinFuncion
	