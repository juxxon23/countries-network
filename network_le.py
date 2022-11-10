import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy  as np
import collections
import pylab

def get_filtered_data():
    df = pd.read_csv("Life_Expectancy_Data.csv")
    cols = df.columns
    life_expectancy = df[cols[3]]
    countries_expectancy = [df.loc[df[cols[3]] == life, [cols[0], cols[3]]] for life in life_expectancy]
    CE = {}
    for country in countries_expectancy:
        countries = []
        for row in country.index:
            countries.append(country.loc[row][cols[0]])
            CE[country.loc[row][cols[3]]] = countries 
    return countries_expectancy, cols

"""
def plotDegDistLogLog(G, loglog = True):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True) 
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    frac = [n/G.number_of_nodes() for n in cnt]
    fig, ax = plt.subplots()
    plt.plot(deg, frac, '-o')
    if loglog:
        ax.set_yscale('log')
        ax.set_xscale('log')
    plt.ylabel("Fraction of nodes")
    plt.xlabel("Degree")
"""

def create_network():
    G = nx.Graph()
    fd, cols = get_filtered_data()
    # Se debe verificar que los nodos tengan la misma expectativa de vida.



    #test = [G.add_edge(fd.loc[i][cols[0]], fd.loc[i][cols[3]]) for i in range(len(fd))]
    #nx.draw(G, with_labels=(True))
    #pylab.show()
    #plotDegDistLogLog(G)
    #pylab.show()



create_network()