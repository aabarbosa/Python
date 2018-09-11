# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 108

def prevogais(palavra):
	prevogais = []
	for i in range(len(palavra)-1):
		if palavra[i+1] in 'aeiouAEIOU':
			prevogais.append(palavra[i])
	return prevogais

print prevogais("exemplo")
print prevogais("hiato")
print prevogais("exemplo") == ['x', 'l']
print prevogais("hiato") == ['h', 'i', 't']
print prevogais("abadaA") == ['b', 'd', 'a']
print prevogais("hiato") == ['h', 'i', 't']
print prevogais("AeAeo") == ['A','e' , 'A', 'e']