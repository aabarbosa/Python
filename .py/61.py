# coding: utf-8

x = float(raw_input())
y = float(raw_input())

# Estrutura de verificação do Quadrante
if x>0 and y>0:
	print 'Primeiro quadrante'
elif x<0 and y<0:
	print 'Terceiro quadrante'
elif x>0 and y<0:
	print 'Quarto quadrante'
elif x<0 and y>0:
	print 'Segundo quadrante'
elif not x== 0 and y==0:
	print 'Eixo das abscissas'
elif x==0 and not y==0:
	print 'Eixo das ordenadas'
else:
	print 'Origem'