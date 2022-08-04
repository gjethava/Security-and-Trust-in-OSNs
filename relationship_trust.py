from google.colab import drive
drive.mount('/content/drive')

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

r_ty=["family member","close friend","acquaintance"]

rty=random.choice(r_ty)

if rty=="family member":
  RT=1
elif rty=="close friend":
  RT=0.90
elif rty=="acquaintance":
  RT=0.70
else:
  RT=0

print("Relationship:",rty)
print('The relationship trust value between neighbouring nodes:',RT)
