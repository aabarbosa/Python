# coding: utf-8

num = int(raw_input())

assert num > 0

# Imprima os divisores menores que Num
for num_prop in range(1,num):
	if num % num_prop == 0:
		print num_prop