# apply networkx

import time
import networkx as nx
from util import RedisUtil as ru

'''some static vars need to set before pageRank goes'''
filename = '/Users/Chen/Desktop/计算社会学/largeDataset/data/edges.csv'
    # '/Users/Chen/Desktop/计算社会学/smallDataset/twitter_combined.csv'
pageRank_redis_key = 'pr_L_0518_01'

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
ru.redisSet(pageRank_redis_key, pr)
# ru.redisHmset('pr_hash_0518_01')

print("elapsed time: ", time.time() - beginTime)