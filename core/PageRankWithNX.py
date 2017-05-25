# apply networkx

import time
import networkx as nx


'''some static vars need to set before pageRank goes'''
# filename = '/Users/Chen/Desktop/计算社会学/largeDataset/data/edges.csv'
filename = '/Users/Chen/Desktop/计算社会学/smallDataset/twitter_combined.csv'
persistenceFilename = '/Users/Chen/Desktop/计算社会学/pr_small_0525_nx01.txt'

'main part of program'
beginTime = time.time();
G = nx.DiGraph()
with open(filename) as file:  # 可以理解成if xxx is okay : then do sth;
    for line in file:
        head, tail = [int(x) for x in line.split(',')]
        print(head, tail)
        G.add_edge(head, tail)

pr = nx.pagerank(G, alpha=0.85)

# data persistence
with open(persistenceFilename) as file:
    file.write(str(pr))

print("elapsed time: ", time.time() - beginTime)