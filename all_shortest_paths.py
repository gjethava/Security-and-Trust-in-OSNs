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

for path in nx.all_shortest_paths(g1, source='2', target='33', method='bfs'):
  print(path)
