#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:25:01 2021

@author: juan
"""

import numpy as np
from Ant_Colony import AntColony
import pandas as pd
import Map as Map

A = np.inf
dist = pd.read_csv("MtxDistancia.csv")
Adj = pd.read_csv("MtxAdjacencia.csv")

dist1 = (np.array(dist)[:,1:]).astype(float)
Adj1 = (np.array(Adj)[:,1:]).astype(float)
Distances = np.zeros_like(dist1)

for j in range(len(dist1)):
        for i in range(len(dist1)):
            if dist1[j,i] * Adj1[j,i] != 0:
                Distances[j,i] = dist1[j,i] * Adj1[j,i]
            else:
                Distances[j,i] = A

# los dos primeros números son los nodos de inicio y final
ant_colony = AntColony(38, 17, Distances, 1, 1, 100, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
print ("Ruta mínima: {}".format(shortest_path))
B = Map.Map(dist, Adj)
B.Graph_Map()
B.Graph_route(shortest_path)
B.Distances_Matrix()
