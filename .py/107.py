# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 107

def divisor(num,list):
	for i in range(len(list)):
		if list[i]%num == 0:
			return i
	return -1
	
print divisor(10,[100,10,40,50]) == 0
print divisor(10,[-10]) == 0
print divisor(10,[-1,-1,-2,-3,-4,-4,-20]) == 6
print divisor(5, [3,15,50,23,5]) == 1

