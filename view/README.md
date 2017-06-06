WebPageDependencyVisualization
==============================

<b>This is a project to visualize web pages dependency and links generated using page rank algorithm. Project uses d3.js to graphically visualize web page data</b>
<br/>
<b>Page Rank Visualization with D3.js </b>
<p>
This project is a simple visualization of web page graphs with individual significance assigned to individual web page node.
I have calculated rough significance of each node based on the toal number of incoming and outgoing links to and from the given node. Incoming and
</p>
<p>
outgoing links increase and decrease the significance values respectively.
Input is given as a form of csv file which contains the data node as a part of node pair and link between them.
Users can vary number of links they want to see on the screen and change the presentation appearance.
</p>
Demo of this project could be viewed at http://jayeshkawli.com/PageRanksVisualization/mainPointsPlotter.html

==============Cheney's interpretation===============
- data中`pagerankVisualizationOutput.csv`这个文件是数据的来源;
- pagerankVisualizationOutput.csv文件中, 每一行代表一条有向边. source代表源节点, target是目标节点, value代表的是源节点自己的得分(PageRank值, 或者说是重要度, 图中就是圆形的半径r, 这其实有一点点不合理)
```
source,target,value
0,4,332
1,2,10
2,0,199
3,14,0
4,34,285
5,0,0
5,4,0
5,6,0
5,18,0
5,60,0
6,2,108
6,16,108
6,92,108
```
- force.csv暂时没看出有任何作用;
- pageRankPointsParser.py用来帮助把`pagerank.input.1000.1`转化成为`pagerankVisualizationOutput.csv`这样格式的文件
