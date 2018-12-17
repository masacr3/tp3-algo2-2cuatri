def f_cmp_tiempo(vuelo1,vuelo2):
	tiempo1 = int(vuelo1[0])
	tiempo2 = int(vuelo2[0])
	return (tiempo1>tiempo2)-(tiempo1<tiempo2)

def f_cmp_precio(vuelo1,vuelo2):
	precio1 = int(vuelo1[1])
	precio2 = int(vuelo2[1])
	return (precio1>precio2)-(precio1<precio2)

def f_cmp_escalas(vuelo1,vuelo2):
	escalas1 = int(vuelo1[2])
	escalas2 = int(vuelo2[2])
	return (escalas1>escalas2)-(escalas1<escalas2)
