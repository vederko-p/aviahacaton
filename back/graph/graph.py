
import pandas as pd
import numpy as np


# Первый граф - первый этаж терминала B
# вершины:
vertex_1f = pd.read_csv('graph_vertexes/b_1f_vertexes_coords_px.csv', header=None)
vertex_1f.columns = ['x', 'y', 'z']
# ребра
links_1f = pd.read_csv('graph_edges/b_1f_links.csv', header=None)
links_1f.columns = ['i', 'j']

# Второй граф - второй этаж терминала B
# вершины:
vertex_2f = pd.read_csv('graph_vertexes/b_2f_vertexes_coords_px.csv', header=None)
vertex_2f.columns = ['x', 'y', 'z']
# ребра
links_2f = pd.read_csv('graph_edges/b_2f_links.csv', header=None)
links_2f.columns = ['i', 'j']


def euclidean_distance(x0, y0, z0, x1, y1, z1):
    return ((x1-x0)**2 + (y1-y0)**2 + (z1-z0)**2)**0.5


lv_1f = links_1f.values  # Ребра графа. Каждая строчка - пара номеров вершин, соединенных ребром.
vv_1f = vertex_1f.values  # Координаты вершин. Порядок точек в файле представляет нумерацию вершин.
# (на нулевой позиции: vv[0] кординаты первой вершины и так далее)
lv_2f = links_2f.values
vv_2f = vertex_2f.values


def get_weights(vv, lv):
    # vv - vertexes, lv - edges
    weights = np.zeros((vv.shape[0], vv.shape[0]))
    for i in lv:
        weights[i[0], i[1]] = euclidean_distance(vv[i[0]][0], vv[i[0]][1], vv[i[0]][2], vv[i[1]][0], vv[i[1]][1], vv[i[1]][2])
        # weights - треугольная матрица весов, все значения весов лежат в верхнем треугольнике (weights[i, j], i < j)
    return weights


# print(get_weights(vv_1f, lv_1f)[:5, :5])


def adjacent_list(n, edges_list):
    # edges_list - lv
    # n - количество вершин (vv_1f.shape[0])
    els = range(n)
    adj_vertexes = []
    for i in els:
        t = np.unique(np.append(edges_list[edges_list[:, 0] == i], edges_list[edges_list[:, 1] == i]))
        adj_vertexes.append(list(t[t != i]))
    return adj_vertexes


def graph_join(g1, g2, edges):
    # g1 - список из координат вершин и списка ребер: vv и lv
    # edges - вершины соединения графов (номера):
    # edges = [[vv11, vv21], [vv12, vv22], ..., [vvk, vvk]];
    # Имеются в виду номера вершин, не координаты!
    g2_new_links = (g2[1] + g1[0].shape[0])[:]
    common_graph_links = np.append(g1[1], g2_new_links, axis=0)
    for i in edges:
        new_edge = np.array([[i[0], i[1] + g1[0].shape[0]]])
        common_graph_links = np.append(common_graph_links, new_edge, axis=0)
    common_graph_vertexes = np.append(g1[0], g2[0], axis=0)
    return common_graph_vertexes, common_graph_links


# Пример объединения графов:
# Объединить первый и второй граф так, чтобы пятая вершина первого графа
# Соединялась с восьмой вершиной второго графа:
# print(graph_join([vv_1f, lv_1f], [vv_2f, lv_2f], [[5, 8]]))
# Возвращается кортеж: вершины графа, ребра графа
