import astar
import pandas as pd
import numpy as np





def euclidean_distance(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2)**0.5


vertex = pd.read_csv('b_1f_edges_coords_px.csv', header=None)
vertex.columns = ['x', 'y']
links = pd.read_csv('b_1f_links.csv', header=None)
links.columns = ['i', 'j']

lv = links.values
vv = vertex.values  # Координаты вершин. Порядок точек в файле представляет нумерацию вершин.
# (на нулевой позиции: vv[0] кординаты первой вершины и так далее)

weights = np.zeros((vertex.size, vertex.size))
for i in lv:
    weights[i[0], i[1]] = euclidean_distance(vv[i[0]][0], vv[i[0]][1], vv[i[1]][0], vv[i[1]][1])
    # weights - треугольная матрица весов, все значения весов лежат в верхнем треугольнике (weights[i, j], i < j)


# словарь координаты номер и наоборот
vertexes = {}
vertexes_reversed = {}
for i in range(len(vv)):
    vertexes[i] = tuple(vv[i])
    vertexes_reversed[tuple(vv[i])] = i

# список списков смежных вершин

graph_connected = {}
for v in lv:
    v0 = vertexes[v[0]]
    v1 = vertexes[v[1]]
    if v0 in graph_connected:
        graph_connected[v0].append(v1)
    else:
        graph_connected[v0]=[v1]
    if v1 in graph_connected:
        graph_connected[v1].append(v0)
    else:
        graph_connected[v1]=[v0]
# a*
path = astar.a(vertexes[0],vertexes[5],graph_connected)
# итоговый путь
print(vertexes_reversed[vertexes[0]])
for v in path:
    print(vertexes_reversed[v])
