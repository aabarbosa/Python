# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 100

def verifica_seguranca(senha):
	geral,impares = 0,0 
	for i in range(0,len(senha),2):
		geral += 1
		if int(senha[i])%2 == 1:
			impares += 1
	
	geral_2,pares = 0,0
	for i in range(1,len(senha),2):
		geral_2 += 1
		if int(senha[i])%2 == 0:
			pares += 1

	if (geral == impares) and (geral_2 == pares):
		return 'segura'
	else:
		return 'insegura'
		
print verifica_seguranca(raw_input())