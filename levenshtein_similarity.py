from google.colab import drive
drive.mount('/content/drive')

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
import pandas as pd
import random

def lev(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([lev(s[:-1], t)+1,
               lev(s, t[:-1])+1, 
               lev(s[:-1], t[:-1]) + cost])

    return res

s_att="ahemedabad"
d_att="amdavad"

# measuring attribute similarity using the Levenshtein similarity ratio
att_similarity=(len(s_att)+len(d_att)-lev(s_att,d_att))/(len(s_att)+len(d_att))

print("The atttribite similarity between neighboring nodes using the Levenshtein similarity ratio:",att_similarity)
