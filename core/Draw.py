
import matplotlib.pyplot as plt
import networkx as nx

G = nx.binomial_graph(10, 0.3, directed=True)
layout = nx.spring_layout(G)
plt.figure(1)
nx.draw(G, pos=layout, node_color='y')

pr=nx.pagerank(G,alpha=0.85)
print(pr)
for node, pageRankValue in pr.items():
    print("%d,%.4f" %(node,pageRankValue))

plt.figure(2)
nx.draw(G, pos=layout, node_size=[x * 6000 for x in pr.values()],node_color='m',with_labels=True)
plt.show()