# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 99


def dia_seguinte(dia,mes,ano):
	if mes == 2:
		if dia == 28:
			dia = 1
			mes += 1
		else:
			dia += 1
	
	elif mes in [1,3,5,7,8,10]:
		if dia == 31:
			dia = 1
			mes +=1
		else:
			dia += 1
		
	elif mes in [4,6,9,11]:
		if dia == 30:
			dia = 1
			mes += 1
		else:
			dia += 1
	else:
		if dia == 31:
			dia = 1
			mes = 1
			ano += 1
		else:
			dia += 1
	return "%02d" % dia, "%02d" % mes, ano
			
dia = int(raw_input())
mes = int(raw_input())
ano = int(raw_input())

dia, mes, ano = dia_seguinte(dia,mes,ano)
print dia
print mes
print ano




