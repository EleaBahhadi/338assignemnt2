import sys
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2.json", 'r') as f:
    data = json.load(f)

import threading
threading.stack_size(33554432)

times = []
array_sizes = []
for i in range(len(data)):
    t = timeit.timeit(lambda: func1(data[i], 0, len(data[i])-1), number=10)
    times.append(t)
    array_sizes.append(len(data[i]))

plt.plot(array_sizes, times)
plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.title('Time vs Array Size (10 runs per input)')
plt.show()
