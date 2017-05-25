persistenceFilename = '/Users/Chen/Desktop/计算社会学/pr_small_01.txt'  #存放结果的地址

def getDictFromRedis():
    f = open(persistenceFilename)
    string = f.read()
    return eval(string)


if __name__ == "__main__":
    d = getDictFromRedis()
    print(d[16977983])