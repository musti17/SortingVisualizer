


import time

def counting(data, drawdata, speed):
    mval = 0
    for i in range(len(data)):
        drawdata(data, ['red' if x == i else ['black'] for x in range(len(data))])
        time.sleep(speed)
        if data[i] > mval:
            mval = data[i]

    buckets = [0 for i in range(mval + 1)]

    for i in data:
        buckets[i] += 1

    i = 0
    for j in range(mval + 1):
        for _ in range(buckets[j]):
            data[i] = j
            i += 1

    drawdata(data, ['green' for x in range(len(data))])
    time.sleep(speed)

    return data 

def count_range(data,drawdata,speed):
    d=[]
    d=counting(data,drawdata,speed)
    a=5
    b=7
    for i in range(len(d)):
        if(d[i]>d[a-1] and d[i]<d[b]):
            drawdata(d, ['red' if x > a and x < b else ['black'] for x in range(len(d))])
    print(d[b]-d[a]+1)
    print(d)