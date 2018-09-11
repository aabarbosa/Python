N = int(raw_input())
assert N>0
list=[]

for i in range(N):
	nota = float(raw_input())
	list.append(nota)
	
soma = 0	
for notas in list:
	soma += notas
	
print '%.1f' % (soma/len(list))