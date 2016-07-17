from os import walk
from collections import Counter

def puntos(point_file):
	with open(point_file, 'r') as pf:
		rtn = pf.readlines()
	return rtn

rankeados = "./data/primeros400.att"

with open(rankeados, 'r') as rankfile:
	ranking = rankfile.readlines()

points_f1 = "./data/att_genetic_cfssubset"
points_f2 = "./data/att_greedy_cfssubset"

ranking = map(lambda x: int(x), ranking)
points1 = puntos(points_f1)
points2 = puntos(points_f2)

apariciones = Counter(ranking)

for r in ranking:
	apariciones[r] += int(points1[r-1][11]) + int(points2[r-1][11])

print [x for x,y in apariciones.most_common(39)] + [1583]
