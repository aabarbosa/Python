# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 151

def procura_elemento(M,e):
	for i in range(len(M)):
		for j in range(len(M[0])):
			if M[i][j] == e:
				return i,j
	return (-1,-1)


m = [[6, 2],[ 6, 4], [5,6]]
print procura_elemento(m,6) == (0,0)
print procura_elemento(m,7) == (-1,-1)




