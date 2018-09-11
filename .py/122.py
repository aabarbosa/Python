# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 122

def quantos_comeram(n_feijoadas, fila):
	contador = 0
	for group in fila:
		if n_feijoadas - group >= 0:
			contador += group
			n_feijoadas -= group
		else:
			return contador
	return contador
			
assert quantos_comeram(10, [10, 10]) == 10
assert quantos_comeram(12, [10, 10]) == 10
assert quantos_comeram(2, [10, 10]) == 0
assert quantos_comeram(5, [2, 3, 5]) == 5


		
		
			
		
