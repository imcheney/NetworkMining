"""
读取twitter-combined.csv文件, 在每行的末尾, 根据第一个数字来获取到这个数字对应结点的PageRank得分,
把这个得分加到本行的末尾
"""
import util.ReadAndEvalResult as rae
import time

# 常量
SOURCE_FILE = '/Users/Chen/Desktop/计算社会学/smallDataset/twitter_combined.csv'
TARGET_FILE = '/Users/Chen/Desktop/计算社会学/170527_formattedBiggerThan30_V5.txt'


def createFormatted():
    startTime = time.time()
    res = rae.getDictFromFile()
    d = {}
    f = open(TARGET_FILE, 'w')
    f.write('source,target,value\n')
    count = 0
    with open(SOURCE_FILE) as file:  # 可以理解成if xxx is okay : then do sth;
        for line in file:
            # if count > 1000:
            #     break
            head, tail = [int(x) for x in line.split(',')]
            # if d.__contains__(head):  # 如果有过这个结点了, 跳过
            #     continue
            normalizedVal = round(1e5 * res[head], 2)
            if normalizedVal >= 30:
                # d[head] = 1
                count += 1
                print(normalizedVal)
                newLine = str(head) + ',' + str(tail) + ',' + str(normalizedVal)
                f.write(newLine + '\n')
    print('count: ', count)
    print('Task over, elapsed time: ', time.time() - startTime)


def test():
    createFormatted()


if __name__ == "__main__":
    test()