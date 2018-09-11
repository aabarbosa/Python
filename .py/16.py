import math
a = float(raw_input())
b = float(raw_input())
c = float(raw_input())

D = b**2 - 4*a*c

if D>0:
	x1 = (-b + math.sqrt(D)) / (2*a)
	x2 = (-b - math.sqrt(D)) / (2*a)
	print 'x1 = %.2f' % x1
	print 'x2 = %.2f' % x2
elif D==0:
	x = (-b + math.sqrt(D)) / (2*a)
	print 'x = %.2f' % x
else:
	print 'sem raizes reais'