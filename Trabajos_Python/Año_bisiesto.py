print("Como saber si un año es bisiesto o no")

numero_agno=float(input("Digita el año que deseas calcular: "))

if numero_agno%4==0:
	if numero_agno%100==0:
		if numero_agno%400==0:
			print("El año es bisiesto")
		else:
			print("El año no es bisiesto")
	else:
		print("El año es bisiesto")
else:
	print("El año no es bisiesto")	


	


