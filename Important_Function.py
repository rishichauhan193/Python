from functools import lru_cache
@lru_cache(maxsize=3)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
def recursiveGP(a, r, n):
    if n == 1:
        return a
    else:
        return recursiveGP(a, r, n-1) * r

def recursiveAP(a, d, n):
    if n == 1:
        return a
    else:
        return recursiveGP(a, d, n-1) + d
    
def recursiveFact(n):
    if n == 0:
        return 1
    else:
        return n * recursiveFact(n - 1)
    
PI = 3.14

class Royal():
    pass

# print(__name__)
if __name__ == "__main__":
    a = int(input())
    d = int(input())
    n = int(input())
    print("factorial =", recursiveFact(a))
    print("AP: ", recursiveAP(a, d, n))
    print("GP: ", recursiveGP(a, d, n))
    print("Fibonacci: ", fibo(n))