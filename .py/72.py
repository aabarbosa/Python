# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 72


def more_prolonged_of(N, shipments):
	intervals = []
	for shipment in shipments:
		intervals.append(shipment[1] - shipment[0])
		 
	interval_max, indice = intervals[0], 0
	for i in range(len(intervals)):
		if intervals[i] >= interval_max:
			interval_max = intervals[i]
			indice = i
			
	return 'carregamento %d' % (indice + 1)
	
			
### Data Entry ###
			
N, shipments = int(raw_input()), []			 # number of shipments
for i in range(N):
	begin_end = map(int, raw_input().split())
	shipments.append(begin_end)
###    End    ###

print more_prolonged_of(N, shipments)
