
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import graph
import graph_with_path
import numpy as np

# start = 0
# end = 81
# p = graph_with_path.path(start, end, graph_with_path.graph_connected)
# x = np.array([[graph.vv[p[i-1]], graph.vv[p[i]]] for i in range(1, len(p))]).transpose()
# print(x)
# print(p)

fig, ax = plt.subplots(figsize=(10, 7))
img = mpimg.imread('airport_b2.jpg')
imgplot = plt.imshow(img)
for i in graph.lv:  # links
    ax.plot([graph.vv[i[0]][0], graph.vv[i[1]][0]], [graph.vv[i[0]][1], graph.vv[i[1]][1]], c='black')
ax.scatter(graph.vv[:, 0], graph.vv[:, 1], c='r', linewidths=2)  # vertex
# ax.plot(x[0], x[1], c='orange', linewidth=3)  # path
plt.show()
