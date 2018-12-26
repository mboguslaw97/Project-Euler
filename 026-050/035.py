import helper

def rotate(s, n):
    return s[len(s) - n:] + s[:len(s) - n]

def rotations(s):
    return set(rotate(s, x) for x in range(len(s)))

def solution(n):
    result = 0
    tried = set()
    primes = set(helper.primes(n))
    for prime in primes:
        s = str(prime)
        if s not in tried:
            rots = rotations(s)
            tried |= rots
            for rot in rots:
                if int(rot) not in primes:
                    break
            else:
                result += len(rots)
    return result

print(solution(100)) #13
print(solution(1000000)) #55
        
