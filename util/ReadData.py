
#to read data into the sys
import time
import csv
import redis
r = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True)
MY_DATA_PATH = r'/Users/Chen/Desktop/计算社会学/smallDataset/twitter_combined.csv'


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
    print("====start converting file to a dict...")
    startTime = time.time()
    d = createDict(MY_DATA_PATH)
    print("====finish dict creation, saving into redis...")
    r.hmset("twitterLarge", d)
    r.save()
    print("====redis save finished;")
    print("====elapsed time: ", time.time() - startTime)

    # TODO: save my dict into Redis database