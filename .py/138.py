# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 138

def M_input(nlin,ncol):
	M = []
	for i in range(nlin):
		M.append(map(int, raw_input().split()))
		
		try:
			assert len(M[i]) == ncol
		except:
			return None
	return M
			
nlin, ncol = map(int, raw_input().split())
