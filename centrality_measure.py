from google.colab import drive
drive.mount('/content/drive')

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

# loading soc-karate dataset 
g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/soc-karate.net')

# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/socfb-Bowdoin47.net')
# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/socfb-Brandeis99.net')
# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/soc-advogato.net')
# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/soc-epinions.net')


# Measuring degree centrality of each node in the soc-karate network graph
print("The degree centrality of each node in the soc-karate network graph is as follows")
deg_cent=nx.degree_centrality(g1)
print(deg_cent)

# Measuring closeness centrality of each node in the soc-karate network graph
print("The closeness centrality of each node in the soc-karate network graph is as follows")
close_cent=nx.closeness_centrality(g1)
print(close_cent)

# Measuring betweenness centrality of each node in the soc-karate network graph
print("The betweenness centrality of each node in the soc-karate network graph is as follows")
g2=nx.karate_club_graph()
betwn_cent=nx.betweenness_centrality(g2, k=None, normalized=True, weight=None, endpoints=False, seed=None)
print(betwn_cent)
