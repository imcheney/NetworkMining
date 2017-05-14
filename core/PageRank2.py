from numpy import *

# 输入测试数据: 收获票数矩阵
# a[2][1]代表结点V[2]收到来自结点V[1]的1个单位投票
# a = array([[0, 1, 1, 0],
#            [1, 0, 0, 1],
#            [1, 0, 0, 1],
#            [1, 1, 0, 0]], dtype=float)  # dtype指定为float

a = {1: {2: 1,3: 1,4: 1}, 2: {1: 1, 4: 1}, 3: {1: 1}, 4: {2: 1, 3: 1}}


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
    # print(pr, "\n===================================================")
    return pr


def multiply(m, v):
    L = []
    for i in range(len(v)):  # 0~3
        t = 0.0
        for key in m.keys():
            if (m[key].__contains__(i+1)): t += m[key][i+1] * v[key-1]  # t += your share of V[key] * importance of V[key]
        L.append(t)
    # print("L", L)
    return array(L)


def pageRank(p, m, v):  # 计算pageRank值
    """初始化"""
    e = v  # e = [1/n, 1/n ... , 1/n] with n dimension
    h = e/1000
    count = 0
    nextV = p*multiply(m, v) + (1-p)*e
    while not (v-nextV <= h).all():
        v = nextV
        nextV = p * multiply(m, v) + (1 - p) * e  # update nextV
        count += 1
    print("used rounds count: ", count)
    return v


if __name__ == "__main__":
    print("input graph in dict structure: ", a)
    m = graphMove(a)
    N = len(m)
    pr = initPr(N)
    p = 0.8  # 引入浏览当前网页的概率为p,假设p=0.8, 剩下的0.2是抽税, 会被均匀分给所有人
    print("result: \n", pageRank(p, m, pr))  # 计算pr值
