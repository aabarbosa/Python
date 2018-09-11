# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 143

def clicou_no_retangulo(ponto_1, ponto_2, click):
	if (ponto_1.x <= click.x <= ponto_2.x and ponto_1.y <= click.y <= ponto_2.y) or (ponto_1.x >= click.x >= ponto_2.x and ponto_1.y >= click.y >= ponto_2.y):
		return True
	return False
