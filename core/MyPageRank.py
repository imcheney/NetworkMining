'''
PageRankMy是我为这个项目写的, 占小内存, 消耗时间O(V+E)的实现.
效率上大概耗时是networkx包的pagerank函数的两倍左右, 但是我的空间开销更加小, 因此能够放得下更大的数据集.
'''

# from numpy import *
import time

##############这些是本地的测试变量###############
linkOut = {1: [2, 3, 4], 2: [1, 4], 3: [1], 4: [2, 3]}  #本地测试变量a
linkIn = {1: [2,3], 2:[1,4], 3:[1,4], 4:[1, 2]}
testV = {1: 0, 2: 0, 3: 0, 4: 0}  #本地测试变量
##############################################


#需要修改的变量值
# dataFilename = '/Users/Chen/Desktop/计算社会学/largeDataset/data/edges.csv'
dataFilename = '/Users/Chen/Desktop/计算社会学/smallDataset/twitter_combined.csv'
persistenceFilename = '/Users/Chen/Desktop/计算社会学/0527_PrSmallWithPypyCompatible_V2.txt'  #存放结果的地址


def initProbOfEachNode(nodes):  # pr值得初始化
    """初始化所有结点的pageank值"""
    N = len(nodes)
    val = 1.0 / N  # 把初始值总和1平分给所有的结点
    for key in nodes.keys():
        nodes[key] = val
    return nodes


def multiplyWithIntoRate(linkIn, linkOut, v, rate):
    '''对v列向量上的每个结点计算其本轮最后的pagerank值.
    函数需要遍历所有的结点, 对每个结点遍历所有的入度, 因此会遍历所有的边, 这个函数的时间复杂度是O(V+E)
    '''
    print('into multiply...')
    v2 = {}
    for row in v.keys():   # 0~3
        # print('row:', row)
        t = 0.0
        if linkIn.__contains__(row):  # 由于并非每一个图中的结点都有入度, 因此这个if条件判断是必要的, 否则将报出key not found error
            for fromNode in linkIn[row]:
                t += 1.0/len(linkOut[fromNode]) * v[fromNode]  # t += your share of V[key] * importance of V[key]
            v2[row] = t * rate
        else:
            v2[row] = 0.0
    print('exit multiply...')
    return v2


def addTaxationToEveryNode(tax, mainPart):
    for key in mainPart.keys():
        mainPart[key] += tax


def diffSmallEnough(nextV, v, allowedError):
    for key in v.keys():
        if nextV[key] - v[key] > allowedError:
            return False
    return True


def pageRank(rate, linkIn, linkOut, v):  # 计算pageRank值
    """计算pageRank"""
    print('into pageRank...')
    initNodeValue = v[list(v.keys())[0]]
    tax = (1 - rate) * initNodeValue
    allowedError = initNodeValue / 10000.0  # 算法的误差值 = 每个元素初始值 x 10^-4, 误差在这个范围内认为两个变量相等, 这是经过精心选择的误差值, 平衡计算成本和结果的精确程度
    count = 0
    nextV = multiplyWithIntoRate(linkIn, linkOut, v, rate)
    addTaxationToEveryNode(tax, nextV)

    while not diffSmallEnough(nextV, v, allowedError):
        v = nextV
        nextV = multiplyWithIntoRate(linkIn, linkOut, v, rate)
        addTaxationToEveryNode(tax, nextV)  # update nextV
        count += 1
        print('round count: %d' % count)
    print("exit, total rounds count: ", count)
    return v


def retrieveFromFile():
    linkOut = {}
    linkIn = {}
    nodes = {}
    with open(dataFilename) as file:  # 可以理解成if xxx is okay : then do sth;
        for line in file:
            head, tail = [int(x) for x in line.split(',')]
            if not linkOut.__contains__(head):
                linkOut[head] = []
                nodes[head] = 0
            if not linkIn.__contains__(tail):
                linkIn[tail] = []
                nodes[tail] = 0

            linkOut[head].append(tail)
            linkIn[tail].append(head)

            print(head, tail)
    return linkOut, linkIn, nodes


def retrieveFromTest():
    return linkIn, linkOut, testV


def go():
    global linkIn, linkOut
    print("====PageRank starts, time count starts too...")
    startTime = time.time()
    linkIn, linkOut, nodes = retrieveFromFile()
    # linkIn, linkOut, nodes = retrieveFromTest()
    nodes = initProbOfEachNode(nodes)
    rate = 0.8  # 引入浏览当前网页的概率为p,假设p=0.8, 剩下的0.2是抽税, 会被均匀分给所有人
    PageRankResult = pageRank(rate, linkIn, linkOut, nodes)
    print("result: \n", PageRankResult)  # 计算pr值
    f = open(persistenceFilename, 'w')
    f.write(str(PageRankResult))
    f.close()
    print("====elapsed time: ", time.time() - startTime)


if __name__ == "__main__":
    go()
