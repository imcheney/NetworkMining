
#to read data into the sys

import csv
MY_DATA_PATH = r'/Users/Chen/Desktop/计算社会学/largeDataset/data/edges10000.csv'


def createDict(DATA_PATH):
    aDict = {}
    with open(DATA_PATH, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # print(row[0])
            if not aDict.__contains__(row[0]): aDict[row[0]] = {}
            aDict[row[0]][row[1]] = 1
    return aDict

if __name__ == "__main__":
    d = createDict(MY_DATA_PATH)
    # print(d['1'])
    # TODO: save my dict into Redis database