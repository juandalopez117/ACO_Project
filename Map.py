#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 14:30:20 2021

@author: juan
"""
import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt

dist = pd.read_csv("MtxDistancia.csv")
Adj = pd.read_csv("MtxAdjacencia.csv")

class Map:
    def __init__(self, dist, Adj):
        self.dist = dist
        self.Adj = Adj
        Coordinates = []
        for pair in self.dist[self.dist.columns[0]]:
            pos = re.search('\+', pair)
            a = pos.span()[0]
            lat, long = pair[:a], pair[a+1:]
            Coordinates.append([float(lat), float(long)])
            
        self.Coordinates = np.array(Coordinates)
        self.dist1 = (np.array(self.dist)[:,1:]).astype(float)
        self.Adj1 = (np.array(self.Adj)[:,1:]).astype(float)
        self.Distances = np.zeros_like(self.dist1)
        
        for j in range(len(self.dist1)):
            for i in range(len(self.dist1)):
                if self.dist1[j,i] * self.Adj1[j,i] != 0:
                    self.Distances[j,i] = self.dist1[j,i] * self.Adj1[j,i]
                else:
                    self.Distances[j,i] = np.inf
        self.Coord = np.array(self.Coordinates)
        self.pairs = []
        for i in range(len(self.Coordinates[:,1])):
            self.pairs.append((self.Coordinates[:,1][i], 
                          self.Coordinates[:,0][i]))
    
    def Graph_Map(self):
        
        plt.figure(figsize=(10,10))
        
        plt.scatter(self.Coord[:,1][:21], 
            self.Coord[:,0][:21], color = 'blue', s = 100)
        for j in range(len(self.Coord[:,1][:21])):
            for i in range((len(self.Coord[:,1][:21]))):
                a = [(self.Coord[i][1]), (self.Coord[j])[1]]
                b = [(self.Coord[i][0]), (self.Coord[j])[0]]
                thickness = self.Distances[j,i]
                plt.plot(a,b, color = 'black', 
                         linewidth = 0.00005 * thickness)
        
        plt.scatter(self.Coord[:,1][21:33], 
                    self.Coord[:,0][21:33], color = 'red', s = 100)
        
        for j in range(len(self.Coord[:,1][:21])):
            for i in range((len(self.Coord[:,1][21:33]))):
                a = [(self.Coord[j][1]), (self.Coord[21+i])[1]]
                b = [(self.Coord[j][0]), (self.Coord[21+i])[0]]
                thickness1 = self.Distances[j,i]
                if thickness1 != np.inf:
                    plt.plot(a,b, color = 'black', 
                         linewidth = 0.00005 * thickness1)
                else:
                    pass
        
        plt.scatter(self.Coord[:,1][33:], self.Coord[:,0][33:], 
                    color = 'green', s = 100)
        for j in range(len(self.Coord[:,1][33:])):
            for i in range((len(self.Coord[:,1][33:]))):
                a = [(self.Coord[33+j][1]), (self.Coord[33+i])[1]]
                b = [(self.Coord[33+j][0]), (self.Coord[33+i])[0]]
                thickness2 = self.Distances[i,j]
                plt.plot(a,b, color = 'black', 
                         linewidth = 0.00005 * thickness2)
        
        for j in range(len(self.Coord[:,1][21:33])):
            for i in range((len(self.Coord[:,1][33:]))):
                a2 = [(self.Coord[21+j][1]), (self.Coord[33+i])[1]]
                b2 = [(self.Coord[21+j][0]), (self.Coord[33+i])[0]]
                thickness2 = self.Distances[j,i]
                if thickness2 != np.inf:
                    plt.plot(a2,b2, color = 'black', 
                             linewidth = 0.00005 * thickness2)
                else:
                    pass
        
        for i in range(len(self.Coord)):
            plt.annotate(str(i), (self.Coord[i][1], self.Coord[i][0]),
                         color = 'm')
    def Scatter_Graph(self):
        
         plt.scatter(self.Coord[:,1][:21], 
            self.Coord[:,0][:21], color = 'blue', s = 100)
         
         
         plt.scatter(self.Coord[:,1][21:33], 
                    self.Coord[:,0][21:33], color = 'red', s = 100) 
         
         plt.scatter(self.Coord[:,1][33:], self.Coord[:,0][33:], 
                    color = 'green', s = 100)
         
         #for i in range(len(self.Coord[:,1])):
         #   plt.annotate(' ' + str(i), self.pairs[i])
             
         
    def Distances_Matrix(self):
        plt.matshow(self.Distances)
        plt.title("Matriz de Distancias")
        
    def Graph_route(self, shortest_path):
        self.Scatter_Graph()
        for j in range(len(shortest_path[0])):
            for i in range(len(shortest_path[0])):
                a = shortest_path[0][i]
                b = [self.pairs[a[0]], self.pairs[a[1]]]
                if self.dist1[j,i] != np.inf and self.dist1[i,j] != np.inf:
                    plt.plot((b[0][0], b[1][0]), (b[0][1], b[1][1]))
                    plt.annotate("", xy=(b[0][0], b[0][1]), xytext=(b[1][0], 
                                                                    b[1][1]),
                                 arrowprops = dict(arrowstyle="<-",  
                                                   color = 'yellow',
                                                   lw = 1.5))
   
        
    
                
                
                        

                


        
 