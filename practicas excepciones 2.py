def divide():
	try:
		
		op1=(float(input("introduce el primer numero")))
		op2=(float(input("introduce el segundo numero")))

		print ("la division es: " + str(op1/op2))

# la funcion except puede usarce de forma continua para cubrir el error espcifico que deseemos	
	except ValueError:
		print ("El valor introducido es erroneo")

	except ZeroDivisionError:
		print ("no se puede dividir entre 0!")

# lo que se colocoque en el finally se ejecuta siempre, aunque no se cubran los errores
	finally:
		print ("calculo finalizado")

divide ()