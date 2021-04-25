
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import graph
import graph_with_path
import numpy as np

start = 0
end = 100
p = graph_with_path.path(start, end, graph_with_path.graph_connected)
x = np.array([[graph.vv_1f[p[i-1]], graph.vv_1f[p[i]]] for i in range(1, len(p))]).transpose()
# print(x)
# print(p)

fig, ax = plt.subplots(figsize=(10, 7))
img = mpimg.imread('airport_b1.jpg')
imgplot = plt.imshow(img)
# for i in graph.lv_1f:  # links
    # ax.plot([graph.vv_1f[i[0]][0], graph.vv_1f[i[1]][0]], [graph.vv_1f[i[0]][1], graph.vv_1f[i[1]][1]], c='black')
# ax.scatter(graph.vv_1f[:, 0], graph.vv_1f[:, 1], c='r', linewidths=2)  # vertexes
ax.plot(x[0], x[1], c='orange', linewidth=3)  # path
plt.show()
