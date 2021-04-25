
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import graph
import graph_with_path
import numpy as np


def plot_airport(airport_floor_image, graph_vertexes, graph_links, path=None, graph=None):
    # airport_floor_image - путь к картинке этажа
    # graph_vertexes - вершины графа
    # graph_links - Ребра графа
    # path - Путь, если его необходимо отрисовать - принимает путь как список вершин
    # Граф, если его необходио отрисовать - принимает True
    # Загрузка картинки этажа
    fig, ax = plt.subplots(figsize=(10, 7))
    img = mpimg.imread(airport_floor_image)
    imgplot = plt.imshow(img)
    # Отрисовка графа
    if graph is not None:
        for i in graph_links:  # links
            ax.plot([graph_vertexes[i[0]][0], graph_vertexes[i[1]][0]], [graph_vertexes[i[0]][1], graph_vertexes[i[1]][1]], c='black')
        ax.scatter(graph_vertexes[:, 0], graph_vertexes[:, 1], c='r', linewidths=2)  # vertexes
    # Отрисовка пути
    if path is not None:
        x = np.array([[graph_vertexes[path[i - 1]], graph_vertexes[path[i]]] for i in range(1, len(path))]).transpose()
        ax.plot(x[0], x[1], c='orange', linewidth=3)  # path
    plt.show()


# Пример
airport_floor_image = r'images\airport_b2.jpg'
graph_vertexes = graph.vv_2f
graph_links = graph.lv_2f
start, end = 0, 29
path = graph_with_path.path(start, end, graph_with_path.graph_connected)
# Отрисовка только этажа:
# plot_airport(airport_floor_image, graph_vertexes, graph_links)
# Отрисовка этажа и пути:
# plot_airport(airport_floor_image, graph_vertexes, graph_links, path=path)
# Отрисовка этажа, пути и самого графа:
plot_airport(airport_floor_image, graph_vertexes, graph_links, path=path, graph=True)
