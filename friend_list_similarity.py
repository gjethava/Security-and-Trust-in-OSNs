from google.colab import drive
drive.mount('/content/drive')

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
import pandas as pd
import random

# suspicious and real nodes' neighbours.
s_node = np.array([9,1,3])
r_node = np.array([7,1,4])
# computing mutual friend list similarity between nodes using cosine similarity measure
MF_similarity=np.dot(s_node,r_node)/(norm(s_node)*norm(r_node))

# suspicious and real nodes' suggested friends.
s_node = np.array([7,5,4])
r_node = np.array([7,1,4])
# computing mutual friend list similarity between nodes using cosine similarity measure
SF_similarity=np.dot(s_node,r_node)/(norm(s_node)*norm(r_node))

# suspicious and real nodes' requeted friends.
s_node = np.array([11,5,3])
r_node = np.array([7,5,4])
# computing mutual friend list similarity between nodes using cosine similarity measure
RF_similarity=np.dot(s_node,r_node)/(norm(s_node)*norm(r_node))

# calculating overall friend list similarity between the nodes
FL_similarity=MF_similarity+SF_similarity+RF_similarity

print("Overall friend list similarity between the suspicious and genune nodes is:",FL_similarity)
