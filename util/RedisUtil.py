import redis
r = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True)
# GRAPH_VERTICES =

def redisSet(key, value):
    strValue = str(value)
    r.set(key, strValue)
    r.save()


def redisGet(key):
    strValue = r.get(key)
    return eval(strValue)


def redisHmset(name, aDict):
    res = r.hmset(name, aDict)
    print("Hmset result: ", res)


def redisHmget(name, keys):
    return r.hmget(name, keys)


# def redisGetWholeDict(name):
#     return r.hmget(name, GRAPH_VERTICES)


# let's do some tests
if __name__ == "__main__":
    d1 = {'name': 'Alison', 'age': 22, 'addr': 'Beijing'}
    redisSet('stu01', d1)
    d2 = redisGet('stu01')
    print(d2)
    print(type(d2))