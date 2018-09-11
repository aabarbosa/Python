# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 148


def devedores(contas):
	contador = 0
	for v in contas.values():
		if v < 0:
			contador += 1
	return contador
	
contas = { 'Ana':1000, 'Antonio':-500, 'William':0, 'Carlos':2500, 'Kate':-1300 }
assert devedores(contas) == 2

