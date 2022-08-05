from google.colab import drive
drive.mount('/content/drive')

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

# loading dataset 
# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/soc-karate.net')
# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/socfb-Bowdoin47.net')
# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/socfb-Brandeis99.net')
g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/soc-advogato.net')
# g1=nx.read_pajek('/content/drive/MyDrive/Colab Notebooks/soc-epinions.net')

print("Suggested friends of node '44'")
print(list(g1.predecessors('44')))

print("Requested friends of node '44'")
print(list(g1.successors('44')))

print("Suggested friends of node '34'")
print(list(g1.predecessors('34')))

print("Requested friends of node '34'")
print(list(g1.successors('34')))

# Calculating mutual frind list similarity using the Jaccard-coefficient similarity metric
MF_similarity=len((set(g1.neighbors('44')).intersection(g1.neighbors('34'))))/(len(set(g1.neighbors('44')))+len(set(g1.neighbors('34')))-len((set(g1.neighbors('44')).intersection(g1.neighbors('34')))))
print('Mutual friend list similarity between the nodes:',MF_similarity)

# Calculating suggested frind list similarity between nodes using the Jaccard-coefficient similarity metric
SF_similarity=len(set(g1.predecessors('44')).intersection(g1.predecessors('34')))/(len(set(g1.predecessors('44')))+len(set(g1.predecessors('34')))-len(set(g1.predecessors('44')).intersection(g1.predecessors('34'))))
print('Suggested friend list similarity between the nodes:',SF_similarity)

# Calculating requested frind list similarity between nodes using the Jaccard-coefficient similarity metric
RF_similarity=len(set(g1.successors('44')).intersection(g1.successors('34')))/(len(set(g1.successors('44')))+len(set(g1.successors('34')))-len(set(g1.successors('44')).intersection(g1.successors('34'))))
print('Requested friend list similarity between the nodes:',RF_similarity)

# Computing overall friend list similarity between the nodes
FL_similarity=MF_similarity+SF_similarity+RF_similarity

print("Overall friend list similarity between the nodes",FL_similarity)
