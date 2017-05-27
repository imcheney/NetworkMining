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

#PageRank算法
##计算表达式
v' = p * dot(M,v) + (1-p)*e / n
##M矩阵存储方案
python: dict -> list
M = {3: {19:1, 112:1, 3700:1, 3789:1, ... , 892303:1}, 4: [71:1, 123:1, 980:1, ..., 12303:1], ...}

1) 获取某个结点的出度: len(M[3])
2) 

##测试用数据
输入测试数据: 收获票数矩阵
`a[2][1]`代表结点V[2]收到来自结点V[1]的1个单位投票(得分), 即V[1]有边指向了V[2].
````
a = array([[0, 1, 1, 0],
           [1, 0, 0, 1],
           [1, 0, 0, 1],
           [1, 1, 0, 0]], dtype=float)  # dtype指定为float
           
linkOut = {1: [2, 3, 4], 2: [1, 4], 3: [1], 4: [2, 3]}  #本地测试变量a
linkIn = {1: [2,3], 2:[1,4], 3:[1,4], 4:[1, 2]}
testV = {1: 0, 2: 0, 3: 0, 4: 0}  #本地测试变量
````
算法空间复杂度: 内存中需要维持M这个map(80m * 4byte * 2 * 2 = 1280MB)和V向量(10m * 4byte * 2 = 80MB)
这是粗略的估计, 实际上可能还有额外的内存开销, 但是大概可以看出8GB内存肯定能够装下大数据集;

算法时间复杂度: 每轮迭代需要实现multiplyWithIntoRate这个函数, O(V + E).
有k轮迭代, 所以算法时间复杂度可以写作O(k•(V+E))

##数据集试验结果
170525: 使用双层字典作为存储方式, 消耗时间280s左右;
170526: 减少字典层数, 在小数据集测试成功, 114s, 对比之下networkx的实现是48s (Macbook Pro 8G i5);
170526 22:46: 使用了pypy JIT以后, 时间下降到9.71秒;
170526 23:44: 使用了pypy JIT, 大数据集在2774s(46.5min)完成;

##可视化
常规的nx.draw()方法, 会发现由于图太大, 画不出来. 这还仅仅是在小图上.