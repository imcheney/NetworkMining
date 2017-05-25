from numpy import *
import time

# 输入测试数据: 收获票数矩阵
# a[2][1]代表结点V[2]收到来自结点V[1]的1个单位投票
# a = array([[0, 1, 1, 0],
#            [1, 0, 0, 1],
#            [1, 0, 0, 1],
#            [1, 1, 0, 0]], dtype=float)  # dtype指定为float

#算法空间复杂度: 内存中需要维持M这个map(80m * 4byte = 320MB)和V向量(10m * 4byte = 40MB),
#算法时间复杂度: 每轮迭代需要做两个矩阵的乘法, O(V + E).
#小数据集测试成功, 285s

##############这些是本地的测试变量###############
linkOut = {1: {2:1, 3:1, 4:1}, 2: {1:1, 4:1}, 3: {1:1}, 4: {2:1, 3:1}}  #本地测试变量a
linkIn = {1: {2:1,3:1}, 2:{1:1,4:1}, 3:{1:1,4:1}, 4:{1:1, 2:1}}
testV = {1: 0, 2: 0, 3: 0, 4: 0}  #本地测试变量
##############################################


#需要修改的变量值
dataFilename = '/Users/Chen/Desktop/计算社会学/largeDataset/data/edges.csv'
# dataFilename = '/Users/Chen/Desktop/计算社会学/smallDataset/twitter_combined.csv'
persistenceFilename = '/Users/Chen/Desktop/计算社会学/pr_large_0525_my01.txt'  #存放结果的地址


def initProbOfEachNode(nodes):  # pr值得初始化
    """初始化所有结点的pageank值"""
    N = len(nodes)
    print('N:', N)
    # pr = zeros((N, 1), dtype=float)  # 构造一个存放pr值的矩阵
    val = float(1) / N  # 把初始值总和1平分给所有的结点
    for key in nodes.keys():
        nodes[key] = val
    print(nodes, "\n===================================================")
    return nodes


def multiplyWithIntoRate(linkIn, linkOut, v, rate):
    '对v列向量上的每个结点计算其本轮最后的pagerank值'
    print('into multiply...')
    v2 = {}
    for row in v.keys():   # 0~3
        print('row:', row)
        t = 0.0
        if linkIn.__contains__(row):
            for fromNodeKey in linkIn[row].keys():
                # print(fromNodeKey)
                t += 1/len(linkOut[fromNodeKey]) * v[fromNodeKey]  # t += your share of V[key] * importance of V[key]
            v2[row] = t * rate
        else:
            v2[row] = 0
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


def pageRank(rate, linkIn, linkOut, v):  # 计算pageRank值
    """计算pageRank"""
    print('into pageRank...')
    initNodeValue = v[list(v.keys())[0]]
    tax = (1 - rate) * initNodeValue
    allowedError = initNodeValue / 10000  # 算法的误差值 = 每个元素初始值 x 10^-4, 误差在这个范围内认为两个变量相等, 这是经过精心选择的误差值, 平衡计算成本和结果的精确程度
    count = 0
    print('before multiplyWithIntoRate')
    nextV = multiplyWithIntoRate(linkIn, linkOut, v, rate)
    print('after multiplyWithIntoRate')
    addTaxationToEveryNode(tax, nextV)

    print('before while check')
    while not diffSmallEnough(nextV, v, allowedError):
        print('into a while loop...')
        v = nextV
        nextV = multiplyWithIntoRate(linkIn, linkOut, v, rate)
        addTaxationToEveryNode(tax, nextV)  # update nextV
        count += 1
        print('round count: %d' % count)
    print("迭代轮数 used rounds count: ", count)
    return v


def retrieveFromFile():
    linkOut = {}
    linkIn = {}
    nodes = {}
    with open(dataFilename) as file:  # 可以理解成if xxx is okay : then do sth;
        for line in file:
            head, tail = [int(x) for x in line.split(',')]
            if not linkOut.__contains__(head):
                linkOut[head] = {}
                nodes[head] = 0
            if not linkIn.__contains__(tail):
                linkIn[tail] = {}
                nodes[tail] = 0

            linkOut[head][tail] = 1
            linkIn[tail][head] = 1

            print(head, tail)
    return linkOut, linkIn, nodes


def retrieveFromTest():
    return linkIn, linkOut, testV


if __name__ == "__main__":
    print("====PageRank执行, 计时开始")
    startTime = time.time()

    linkIn, linkOut, nodes = retrieveFromTest()
    # linkIn, linkOut, nodes = retrieveFromTest()
    nodes = initProbOfEachNode(nodes)
    rate = 0.8  # 引入浏览当前网页的概率为p,假设p=0.8, 剩下的0.2是抽税, 会被均匀分给所有人
    PageRankResult = pageRank(rate, linkIn, linkOut, nodes)

    print("result: \n", PageRankResult)  # 计算pr值
    f = open(persistenceFilename, 'w')
    f.write(str(PageRankResult))
    f.close()

    print("====消耗时间: ", time.time() - startTime)
