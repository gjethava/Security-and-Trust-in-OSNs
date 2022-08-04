from google.colab import drive
drive.mount('/content/drive')

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

# loading dataset 
#g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/soc-karate.net')
g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/socfb-Bowdoin47.net')
# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/socfb-Brandeis99.net')
# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/soc-advogato.net')
# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/soc-epinions.net')

print("Neighbors of node '4'")
print(list(g1.neighbors('4')))

print("Neighbors of node '34'")
print(list(g1.neighbors('34')))

print("Common neighbors of node '4' and '34'")
print(list(nx.common_neighbors(g1, '4', '34')))

# Computing mutual frind list similarity using the Jaccard-coefficient similarity metric
MF_similarity=len(list(nx.common_neighbors(g1, '4', '34')))/(len(list(g1.neighbors('4')))+len(list(g1.neighbors('34')))-len(list(nx.common_neighbors(g1, '4', '34'))))
print('Mutual friend list similarity between the nodes:',MF_similarity)

#print("suggested friends of node '4'")
#print(list(g1.neighbors('4')))

#print("suggested friends of node '34'")
#print(list(g1.neighbors('34')))

#print("Common suggested friends of node '4' and '34'")
#print(list(nx.common_neighbors(g1, '4', '34')))

# Computing suggested frind list similarity using the Jaccard-coefficient similarity metric
SF_similarity=len(list(nx.common_neighbors(g1, '4', '34')))/(len(list(g1.neighbors('4')))+len(list(g1.neighbors('34')))-len(list(nx.common_neighbors(g1, '4', '34'))))
print('Suggested friend list similarity between the nodes:',SF_similarity)

#print("requested friends of node '4'")
#print(list(g1.neighbors('4')))

#print("requested friends of node '34'")
#print(list(g1.neighbors('34')))

#print("Common requested friends of node '4' and '34'")
#print(list(nx.common_neighbors(g1, '4', '34')))

# Computing requested frind list similarity using the Jaccard-coefficient similarity metric
RF_similarity=len(list(nx.common_neighbors(g1, '4', '34')))/(len(list(g1.neighbors('4')))+len(list(g1.neighbors('34')))-len(list(nx.common_neighbors(g1, '4', '34'))))
print('Requested friend list similarity between the nodes:',RF_similarity)

# Computing overall friend list similarity between the nodes
FL_similarity=MF_similarity+SF_similarity+RF_similarity

print("Overall friend list similarity between the nodes",FL_similarity)
