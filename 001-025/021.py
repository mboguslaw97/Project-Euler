from math import sqrt


def gen_proper_divisors(n):
	yield 1
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
		 yield i
		 yield n / i


def solution(n):
    def is_amicable(n):
        d1 = d(n)
        return d1 != n and n == d(d1)
    
    def d(n):
        return sum(gen_proper_divisors(n))

    result = 0
    for i in range(1, n):
        if is_amicable(i):
            result += i
    return result


print(solution(10000))  #31626
