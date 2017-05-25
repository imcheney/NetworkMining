from numpy import *
import time
# import redis
# 输入测试数据: 收获票数矩阵
# a[2][1]代表结点V[2]收到来自结点V[1]的1个单位投票
# a = array([[0, 1, 1, 0],
#            [1, 0, 0, 1],
#            [1, 0, 0, 1],
#            [1, 1, 0, 0]], dtype=float)  # dtype指定为float

#算法空间复杂度: 内存中需要维持M这个map(80m * 4byte = 320MB)和V向量(10m * 4byte = 40MB),
#算法时间复杂度: 每轮迭代需要做两个矩阵的乘法, O(n^3).
#这个版本的pageRank效率不好, 已经淘汰...

# r = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True)
a = {1: {2: 1,3: 1,4: 1}, 2: {1: 1, 4: 1}, 3: {1: 1}, 4: {2: 1, 3: 1}}  #本地测试变量a

#需要修改的变量值
# DICT_NAME = "twitterLarge"
dataFilename = '/Users/Chen/Desktop/计算社会学/smallDataset/twitter_combined.csv'
persistenceFilename = '/Users/Chen/Desktop/计算社会学/pr_test_0526_nx01.txt'  #存放结果的地址


def graphMove(a):  # 构造转移矩阵
    """生成float型的, 每列和为1的标准列方向上归一化的转移矩阵"""
    m = a
    for key in a.keys():
        sum = len(a[key])
        for k in a[key].keys():
            m[key][k] = 1/sum
    # print("m\n",m, "\n====================================================")
    return m


def initPr(N):  # pr值得初始化
    """初始化所有结点的pageank值"""
    pr = zeros((N, 1), dtype=float)  # 构造一个存放pr值得矩阵
    val = float(1) / N  # 把初始值总和1平分给所有的结点
    for i in range(N): pr[i] = val
    print(pr, "\n===================================================")
    return pr


def multiply(m, v):
    L = []
    for i in range(len(v)):  # 0~3
        t = 0.0
        for key in m.keys():
            if m[key].__contains__(i+1): t += m[key][i + 1] * v[key - 1]  # t += your share of V[key] * importance of V[key]
        L.append(t)
    # print("L", L)
    return array(L)


def pageRank(p, m, v):  # 计算pageRank值
    """计算pageRank"""
    e = v  # e = [1/n, 1/n ... , 1/n] with n dimension
    print(e, type(e))
    h = e/1000000  #算法的误差值, 误差在这个范围内认为两个变量相等
    print(h)
    count = 0
    nextV = p*multiply(m, v) + (1-p)*e
    while not (v-nextV <= h).all():
        v = nextV
        nextV = p * multiply(m, v) + (1 - p) * e  # update nextV
        count += 1
    print("迭代轮数 used rounds count: ", count)
    return v


# def retrieveFromRedis():
#     d1 = r.hgetall(DICT_NAME)
#     for key in d1.keys():
#         if d1[key][0] == '{':
#             tempD = eval(d1[key])
#             d1[key] = tempD
#     return d1

def retrieveFromFile():
    d1 = {}
    v = {}
    with open(dataFilename) as file:  # 可以理解成if xxx is okay : then do sth;
        for line in file:
            head, tail = [int(x) for x in line.split(',')]
            if not d1.__contains__(head):
                d1[head] = {}
            d1[head][tail] = 1
            print(head, tail)
    return d1, v

def retrieveFromTest():
    return a


if __name__ == "__main__":
    print("====PageRank执行, 计时开始")
    startTime = time.time()
    d1 = retrieveFromTest()
    m = graphMove(d1)
    N = len(m)
    pr = initPr(N)
    p = 0.8  # 引入浏览当前网页的概率为p,假设p=0.8, 剩下的0.2是抽税, 会被均匀分给所有人
    PRresult = pageRank(p, m, pr)
    print("result: \n", PRresult)  # 计算pr值
    f = open(persistenceFilename, 'w')
    f.write(str(PRresult))
    f.close()
    # r.set("pageRankResult", PRresult.tolist())
    print("====结束时间: ", time.time() - startTime)
