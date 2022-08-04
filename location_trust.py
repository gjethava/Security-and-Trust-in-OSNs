from google.colab import drive
drive.mount('/content/drive')

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

s_node={"neighbor":"yes","home town":"bhavnagar","current city":"vadodara","province":"gujarat","country":"india","region":"asia"}
d_node={"neighbor":"no","home town":"ahmedabad","current city":"vadodara","province":"gujarat","country":"india","region":"asia"}

if s_node["neighbor"]==d_node["neighbor"]:
  LT=0.80
elif s_node["home town"]==d_node["home town"]:
  LT=0.50
elif s_node["current city"]==d_node["current city"]:
  LT=0.40
elif s_node["province"]==d_node["province"]:
  LT=0.30
elif s_node["country"]==d_node["country"]:
  LT=0.20
elif s_node["region"]==d_node["region"]:
  LT=0.10
else:
  LT=0

print("The location trust value between the neighboring nodes is:",LT)
