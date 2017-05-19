"""test redis database"""

import redis
r = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True)
print('test globals')

def create1():
    # r.flushall()
    d1 = {'sid':1001, 'sname':'Cheney',
          'addr': {'city': 'Beijing', 'district': 'Haidian', 'School': 'RUC'},
          'birthdate': '1993-09-28'}
    r.hmset('kid1', d1)
    r.save()


def retrive():
    d2 = r.hgetall("student")
    print(d2)
    d3 = r.hgetall("kid1")
    for key in d3.keys():
        if d3[key][0] == '{':
            tempD = eval(d3[key])
            d3[key] = tempD
    print(d3)

if __name__ == "__main__":
    # create()
    retrive()
