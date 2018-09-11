# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 106

def maior_palavra(list):
	if len(list) >= 1:
		maior_pal = list[0]
		for pal in list:
			if len(pal) > len(maior_pal):
				maior_pal = pal
		return maior_pal

list_words = raw_input().split()
print maior_palavra(list_words)