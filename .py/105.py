# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 105

def conta_palavras(k,palavras):
	palavras = palavras.split(":")
	num_maiorigual_k = 0
	if len(palavras) == 1 and palavras[0] == '':
		return num_maiorigual_k
	else:
		for pal in palavras:
			if len(pal) >= k:
				num_maiorigual_k += 1
		return num_maiorigual_k

# apenas teste
num = int(raw_input())
words = raw_input()

print conta_palavras(num,words)