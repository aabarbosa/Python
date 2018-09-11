# coding: utf-8

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

if (abs(b-c) < a < b+c) and (abs(a-c) < b < a+c) and (abs(a-b) < c < a+b):

	if a==c and a==b:
		print 'Equilátero'
	elif (a==b and a!=c) or (a==c and a!=b)	or (b==c and b!=a):
		print 'Isósceles'
	elif a!=b and a!=c and b!=c:
		print 'Escaleno'
		
else:
	print 'Não é triângulo'