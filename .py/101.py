# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 101

def tempo_oscioso(N,horarios):
	soma_osciosos = 0
	for i in range(1,len(horarios)-1, 2):
		osciosos = horarios[i] - horarios[i+1]
		soma_osciosos += osciosos
	return abs(soma_osciosos)

N = int(raw_input())
horarios = []
for i in range(N):
	t_i,t_f = map(int, raw_input().split())
	horarios.append(t_i)
	horarios.append(t_f)
print tempo_oscioso(N,horarios)
	
	
	