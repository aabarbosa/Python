# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 97

def n_esimo_indice_de(n,list):
	new_list = []
	n_esimo_indice = 0
	for i in range(len(list)):
		if list[i] == n:
			new_list.append(list[i])
			n_esimo_indice = i
			
	if len(new_list) >= 2:
		return n_esimo_indice
	else:
		return -1
			
num = int(raw_input())
list_integers = map(int, raw_input().split())

print n_esimo_indice_de(num, list_integers)
