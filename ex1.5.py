
import timeit
import matplotlib.pyplot as plt

def func2(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = func2(n-1, memo) + func2(n-2, memo)
        return memo[n]

n_values = list(range(37))
times = []
times2 = []

for n in n_values:
    t = timeit.timeit(lambda: func2(n), number=100)
    times.append(t)

plt.plot(n_values, times)
plt.xlabel('n')
plt.ylabel('time')
plt.title('Time to calculate the nth Fibonacci number for func2')
plt.show()

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
for n in n_values:
    t2 = timeit.timeit(lambda: func(n), number=10)
    times2.append(t2)

plt.plot(n_values, times2)
plt.xlabel('n')
plt.ylabel('time2')
plt.title('Time to calculate the nth Fibonacci number for func')
plt.show()  