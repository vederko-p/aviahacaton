
import pandas as pd
import numpy as np


vertex = pd.read_csv('b_1f_edges_coords_px.csv', header=None)
vertex.columns = ['x', 'y']
links = pd.read_csv('b_1f_links.csv', header=None)
links.columns = ['i', 'j']


def euclidean_distance(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2)**0.5


lv = links.values
vv = vertex.values  # Координаты вершин. Порядок точек в файле представляет нумерацию вершин.
# (на нулевой позиции: vv[0] кординаты первой вершины и так далее)

weights = np.zeros((vertex.size, vertex.size))
for i in lv:
    weights[i[0], i[1]] = euclidean_distance(vv[i[0]][0], vv[i[0]][1], vv[i[1]][0], vv[i[1]][1])
    # weights - треугольная матрица весов, все значения весов лежат в верхнем треугольнике (weights[i, j], i < j)

# print(weights[:5, :5])
