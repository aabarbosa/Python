# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 121

def eh_bissexto(ano):
	if (ano%400 == 0) or (ano%4 == 0 and ano%100 != 0):
		return True 
	return False

def conta_dias(dia,mes,ano):
	if eh_bissexto(ano) == True and mes > 2:
		contador = dia + 1
	else:
		contador = dia
		
	for mes in range(1,mes):
		if mes in [1,3,5,7,8,10]:
			contador += 31
		elif mes in [4,6,9,11,12]:
			contador += 30
		else:
			contador += 28
			
	return contador


