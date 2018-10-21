import sympy

n = 100000000 #tested until this treshold (5,761,455 primes)

class Solution:
    def countPrimes(n):
        count = 0
        for i in range(n):
            if (sympy.isprime(i) == True):
                count += 1

        print(count)

Solution.countPrimes(n)
