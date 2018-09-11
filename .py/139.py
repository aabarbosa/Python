# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 139

def M_input(nlin,ncol):
	M = []
	for i in range(nlin):
		M.append(map(int, raw_input().split()))
		
	escalar = int(raw_input())
	
	for i in range(len(M)):
		for j in range(len(M[0])):
			M[i][j] = escalar * M[i][j]
	
	return M
			
nlin, ncol = map(int, raw_input().split())

print M_input(nlin,ncol)
