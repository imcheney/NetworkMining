"""
apply networkx to calculate PageRank
"""

import time

import matplotlib.pyplot as plt
import networkx as nx

'''some static vars need to set before pageRank goes'''
# filename = '/Users/Chen/Desktop/计算社会学/largeDataset/data/edges.csv'
filename = '/Users/Chen/Desktop/计算社会学/smallDataset/twitter_combined.csv'
persistenceFilename = '/Users/Chen/Desktop/计算社会学/0526_prSmall_nx02.txt'

linkOut = {1: {2: 1, 3: 1, 4: 1}, 2: {1: 1, 4: 1}, 3: {1: 1}, 4: {2: 1, 3: 1}}  # 本地测试变量a
linkIn = {1: {2: 1, 3: 1}, 2: {1: 1, 4: 1}, 3: {1: 1, 4: 1}, 4: {1: 1, 2: 1}}
testV = {1: 0, 2: 0, 3: 0, 4: 0}


def retrieveFromTest(G):
    for nodeOut in linkOut.keys():
        for nodeIn in linkOut[nodeOut].keys():
            G.add_edge(nodeOut, nodeIn)
    return G


def retrieveFromFile(G):
    global file
    with open(filename) as file:  # 可以理解成if xxx is okay : then do sth;
        for line in file:
            head, tail = [int(x) for x in line.split(',')]
            print(head, tail)
            G.add_edge(head, tail)
    return G


if __name__ == "__main__":
    'main part of program'
    beginTime = time.time();
    G = nx.DiGraph()
    # G = retrieveFromTest(G)
    G = retrieveFromFile(G)
    PageRankResult = nx.pagerank(G, alpha=0.80)
    nx.draw(G)  # 画出图G
    plt.show()  # 显示出来
    # data persistence
    # f = open(persistenceFilename, 'w')
    # f.write(str(PageRankResult))
    # f.close()

    print("PageRank Result:", PageRankResult)
    print("elapsed time: ", time.time() - beginTime)
