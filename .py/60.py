# coding: utf-8

multas = map(str, raw_input().split())
pontos = 0

# Verificação do tipo de multa e devida soma de pontos
for i in range(len(multas)):
	if multas[i].capitalize() == 'Gravíssima' or multas[i].capitalize() == 'Gravissima':
		pontos += 7
	elif multas[i].capitalize() == 'Grave':
		pontos += 5
	elif multas[i].capitalize() == 'Média' or multas[i].capitalize() == 'Media':
		pontos += 4
	elif multas[i].capitalize() == 'Leve':
		pontos += 3

if pontos >= 20:
	print '%d pontos. CNH suspensa.' % pontos
else:
	print '%d pontos. CNH válida.' % pontos