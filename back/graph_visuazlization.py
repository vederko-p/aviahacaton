
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import graph


fig, ax = plt.subplots(figsize=(10, 10))
# img = mpimg.imread('b1.png')
# imgplot = plt.imshow(img)
for i in graph.lv:  # links
    ax.plot([graph.vv[i[0]][0], graph.vv[i[1]][0]], [graph.vv[i[0]][1], graph.vv[i[1]][1]], c='black')
ax.scatter(graph.vv[:, 0], graph.vv[:, 1], c='red', linewidths=3)  # vertex
plt.show()
