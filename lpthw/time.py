from time import time

def primeQ(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False

        else:
            pass
    return True


t0 = time()
suspects = []
for k in range(1666):
    suspects.append(6 * k - 1)
    suspects.append(6 * k + 1)
primes1 = []
for suspect in suspects:
    if primeQ(suspect):
        primes1.append(suspect)
    else:
        pass
t1 = time()







t2 = time()
suspects = []
for k in range(10000):
    suspects.append(k)
primes2 = []
for suspect in suspects:
    if primeQ(suspect):
        primes2.append(suspect)
    else:
        pass
t3 = time()






first = t1 - t0
second = t3 - t2

print(bool(primes1 == primes2))

eff = (second / first)
print("First approach is", round(eff, 20), '\bx', 'faster.')
