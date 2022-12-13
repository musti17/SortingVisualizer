




# Heap Sort in python

import time
import sys
from algs.heapify import heapify

sys.setrecursionlimit(100000000)
  
def heapSort(data, drawdata, speed):
      n = len(data)
  
      # Build max heap
      for i in range(n//2, -1, -1):
          heapify(data, n, i)
  
      for i in range(n-1, 0, -1):
          # Swap
        data[i], data[0] = data[0], data[i]
        drawdata(data, ['red' if x == i or x == 0 else ['black'] for x in range(len(data))])
        time.sleep(speed)

          # Heapify root element
        heapify(data, i, 0)
  
