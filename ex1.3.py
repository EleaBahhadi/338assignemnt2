def func(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = func(n-1, memo) + func(n-2, memo)
        return memo[n]

for i in range(1, 11):
     print("fib({}) = ".format(i), func(i))