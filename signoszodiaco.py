# Construir un programa que calcule y presente por pantalla el signo del zodiaco a partir de la introducción por
# teclado del día y mes de nacimiento como números enteros.

# Capricornio del 22 de diciembre al 20 de enero
# Acuario del 21 de enero al 19 de febrero
# Piscis del 20 de febrero al 20 de marzo
# Aries del 21 de marzo al 19 de abril
# Tauro del 20 de abril al 20 de mayo
# Géminis del 21 de mayo al 21 de junio
# Cáncer del 22 de junio al 21 de julio
# Leo del 22 de julio al 21 de agosto
# Virgo del 22 de agosto al 22 de septiembre
# Libra del 23 de septiembre al 22 de octubre
# Escorpio del 23 de octubre al 21 de noviembre
# Sagitario del 22 de noviembre al 21 de diciembre

dia= int(input('ingrese el dia: '))
mes= int(input('ingrese el mes: '))

if(mes==12 and dia>=22 and dia<=31) or (mes== 1 and dia>=1 and dia<=20):
	print('capricornio')

elif(mes==1 and dia>=21 and dia<=31) or (mes== 2 and dia>=1 and dia<=19):
	print('acuario')
	
elif(mes==2 and dia>=20 and dia<=29) or (mes== 3 and dia>=1 and dia<=20):
	print('piscis')

elif(mes==3 and dia>=21 and dia<=31) or (mes== 4 and dia>=1 and dia<=19):
	print('aries')

elif(mes==4 and dia>=20 and dia<=30) or (mes== 5 and dia>=1 and dia<=20):
	print('tauro')

elif(mes==5 and dia>=21 and dia<=31) or (mes== 6 and dia>=1 and dia<=21):
	print('geminis')
	
elif(mes==6 and dia>=22 and dia<=30) or (mes== 7 and dia>=1 and dia<=21):
	print('cancer')

elif(mes==7 and dia>=22 and dia<=31) or (mes== 8 and dia>=1 and dia<=21):
	print('leo')

elif(mes==8 and dia>=22 and dia<=31) or (mes== 9 and dia>=1 and dia<=22):
	print('virgo')

elif(mes==9 and dia>=23 and dia<=30) or (mes== 10 and dia>=1 and dia<=22):
	print('libra')

elif(mes==10 and dia>=23 and dia<=31) or (mes== 11 and dia>=1 and dia<=21):
	print('escorpio')

elif(mes==11 and dia>=22 and dia<=31) or (mes== 12 and dia>=1 and dia<=21):
	print('sagitario')
