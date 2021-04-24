
import pandas as pd
import numpy as np


vertex = pd.read_csv('b_1f_edges_coords_px.csv', header=None)
vertex.columns = ['x', 'y']
links = pd.read_csv('b_1f_links_old.csv', header=None)
links.columns = ['i', 'j']


def euclidean_distance(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2)**0.5


(links-1).to_csv('b_1f_links.csv', index=False, header=False)
# print(.head(5))
