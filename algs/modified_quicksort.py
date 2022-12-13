import time

from algs.insertion_sort import insertion

k=7

def getcolorarray(datalen, head, tail, border, currindx, isSwaping = False):
    colorarray = []
    for i in range(datalen):
        if i >= head and i <= tail:
            colorarray.append("gray")
        else:
            colorarray.append('black')

        if i == tail:
            colorarray[i] = 'blue'
        elif i == border:
            colorarray[i] = 'red'
        elif i == currindx:
            colorarray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currindx:
                colorarray[i] = 'green'

    return colorarray

def partition(data, head, tail, drawdata, speed):
    border = head
    pivot = data[tail]

    drawdata(data, getcolorarray(len(data), head, tail, border, border))
    time.sleep(speed)

    for j in range(head, tail):
        if data[j] < pivot:
            drawdata(data, getcolorarray(len(data), head, tail, border, j, True))
            time.sleep(speed)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawdata(data, getcolorarray(len(data), head, tail, border, j))
        time.sleep(speed)

    drawdata(data, getcolorarray(len(data), head, tail, border, tail, True))
    time.sleep(speed)

    data[border], data[tail] = data[tail], data[border]

    return border

def limited_quick_sort(data, head, tail, drawdata, speed,k):

    if tail-head > k:
        partindex=partition(data,head,tail,drawdata,speed)
        print('Line 12')
        #left
        limited_quick_sort(data, head, partindex, drawdata, speed,k)
        print('Line 15')
        #right
        limited_quick_sort(data, partindex+1, tail, drawdata, speed,k)
        print('Line 18')

def modified_quick_sort(data,head,tail,drawdata,speed):

    limited_quick_sort(data,head,tail,drawdata,speed,k)
    insertion(data,drawdata,speed)
    print('Line 24')
