from numpy import *
import time
# 输入测试数据: 收获票数矩阵
# a[2][1]代表结点V[2]收到来自结点V[1]的1个单位投票
# a = array([[0, 1, 1, 0],
#            [1, 0, 0, 1],
#            [1, 0, 0, 1],
#            [1, 1, 0, 0]], dtype=float)  # dtype指定为float

#算法空间复杂度: 内存中需要维持M这个map(80m * 4byte = 320MB)和V向量(10m * 4byte = 40MB),
#算法时间复杂度: 每轮迭代需要做两个矩阵的乘法, O(n^3).


a = {1: {2: 1,3: 1,4: 1}, 2: {1: 1, 4: 1}, 3: {1: 1}, 4: {2: 1, 3: 1}}  #本地测试变量a
b = {1:0,2:0,3:0,4:0}  #本地测试变量

#需要修改的变量值
#/Users/Chen/Desktop/计算社会学/largeDataset/data
#/Users/Chen/Desktop/计算社会学/largeDataset/data/edges.csv
dataFilename = '/Users/Chen/Desktop/计算社会学/smallDataset/twitter_combined.csv'
persistenceFilename = '/Users/Chen/Desktop/计算社会学/pr_small_01.txt'  #存放结果的地址


def graphMove(a):  # 构造转移矩阵
    """生成float型的, 每列和为1的标准列方向上归一化的转移矩阵"""
    m = a
    for key in a.keys():
        sum = len(a[key])
        for k in a[key].keys():
            m[key][k] = 1/sum
    # print("m\n",m, "\n====================================================")
    return m


def initProbOfEachNode(nodes):  # pr值得初始化
    """初始化所有结点的pageank值"""
    N = len(nodes)
    val = float(1) / N  # 把初始值总和1平分给所有的结点
    for key in nodes.keys():
        nodes[key] = val
    print(nodes, "\n===================================================")
    return nodes

#这是算法的瓶颈所在处!!!!! O(n^2)
def multiplyWithIntoRate(m, v, rate):
    '一行一行地给v加值, 输入的m形式类似a'
    print('into multiply...')
    v2 = {}
    for row in v.keys():   # 0~3
        t = 0.0
        for key in m.keys():
            if m[key].__contains__(row):  #如果v[key]有流量流向了v[row]
                t += m[key][row] * v[key]  # t += your share of V[key] * importance of V[key]
        v2[row] = t * rate
    print('exit multiply...')
    return v2


def addTaxationToEveryNode(tax, mainPart):
    for key in mainPart.keys():
        mainPart[key] += tax


def diffSmallEnough(nextV, v, allowedError):
    print('into diffSmallEnough')
    for key in v.keys():
        if nextV[key] - v[key] > allowedError:
            return False
    return True


def pageRank(rate, m, v):  # 计算pageRank值
    """计算pageRank"""
    print('into pageRank...')
    initNodeValue = v[list(v.keys())[0]]
    tax = (1 - rate) * initNodeValue
    allowedError = initNodeValue / 10000  # 算法的误差值设定, 误差在这个范围内认为两个变量相等
    print('allowedError: ', allowedError)
    count = 0
    print('before multiplyWithIntoRate')
    nextV = multiplyWithIntoRate(m, v, rate)
    print('after multiplyWithIntoRate')
    addTaxationToEveryNode(tax, nextV)

    print('before while check')
    while not diffSmallEnough(nextV, v, allowedError):
        print('into a while loop...')
        v = nextV
        nextV = multiplyWithIntoRate(m, v, rate)
        addTaxationToEveryNode(tax, nextV)  # update nextV
        count += 1
        print('round count: %d' % count)
    print("迭代轮数 used rounds count: ", count)
    return v


def retrieveFromFile():
    d1 = {}
    nodes = {}
    with open(dataFilename) as file:  # 可以理解成if xxx is okay : then do sth;
        for line in file:
            head, tail = [int(x) for x in line.split(',')]
            if not d1.__contains__(head):
                d1[head] = {}
                nodes[head] = 0
            d1[head][tail] = 1
            print(head, tail)
    return d1, nodes


def retrieveFromTest():
    return a, b


if __name__ == "__main__":
    print("====PageRank执行, 计时开始")
    startTime = time.time()

    d1, nodes = retrieveFromTest()
    # d1, nodes = retrieveFromTest()
    m = graphMove(d1)
    nodes = initProbOfEachNode(nodes)
    print("node:", nodes)
    rate = 0.8  # 引入浏览当前网页的概率为p,假设p=0.8, 剩下的0.2是抽税, 会被均匀分给所有人
    PageRankResult = pageRank(rate, m, nodes)

    print("result: \n", PageRankResult)  # 计算pr值
    # f = open(persistenceFilename, 'w')
    # f.write(str(PageRankResult))
    # f.close()

    print("====结束时间: ", time.time() - startTime)
