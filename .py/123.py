# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 123

def lanchemaispedido(pedidos):
	for lanche in pedidos:
		conter = 0
		for i in range(len(pedidos)):
			if pedidos[i] == lanche:
				conter += 1
				
		perc_lanche = float(conter)/len(pedidos)
		if perc_lanche > 0.5:
			return lanche

ines = ['tapioca','suco']
marcos = ['suco','coxinha','suco','misto','folhado']
print lanchemaispedido(ines) == None
print lanchemaispedido(marcos) == None

