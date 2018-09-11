# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 98

def min_max(times, value):
	i_min,i_max = 0,0
	max,min = value[0],value[0]
	
	for i in range(len(value)):
		if value[i] > max:
			max = value[i]
			i_max = i
		if value[i] < min:
			min = value[i]
			i_min = i
	return i_min, i_max
	
value = map(float, raw_input().split())
times = raw_input().split()
assert len(value) >= 1 and len(value) == len(times)

i_min, i_max = min_max(times, value)

print "Min:", times[i_min], "%.2f" % value[i_min]
print "Max:", times[i_max], "%.2f" % value[i_max]
