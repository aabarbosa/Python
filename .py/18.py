# coding: utf-8

ano = int(raw_input())

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
	print '%d' % ano, '� bissexto' 
else:
	print '%d' % ano, 'n�o � bissexto'