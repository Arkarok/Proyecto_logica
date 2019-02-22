print("Calcular un numero mayor que otro numero")

num1=float(input("Digita un numero: "))
num2=float(input("Digita un numero: "))

if num1>num2:
	print("El numero " + str(num1) + " es mayor que " + str(num2))
elif num1==num2:
	print("Los numeros son iguales")
else:
	print("El numero " + str(num2) + " es mayor que " + str(num1))

