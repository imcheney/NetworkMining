##项目要求
完成对如下三个方面的挖掘任务:
1)结点重要性计算;
2)三角形个数统计;
3)Transitive Closure 结点的可达性计算;

##项目数据集
###1)Big dataset
http://socialcomputing.asu.edu/datasets/Twitter
>this one requires good algorithm performance to carry.

百度网盘镜像: https://pan.baidu.com/s/1pKKn1zH

###2)Small dataset
https://snap.stanford.edu/data/egonets-Twitter.html
>small dataset to test code

##Deadline
5月26日 星期五

#PageRank
##计算表达式
v' = p * dot(M,v) + (1-p)*e / n
##M矩阵存储方案
python: dict -> list
M = {3: {19:1, 112:1, 3700:1, 3789:1, ... , 892303:1}, 4: [71:1, 123:1, 980:1, ..., 12303:1], ...}

1) 获取某个结点的出度: len(M[3])
2)