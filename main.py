from time import perf_counter

from eratosthenes import eratosthenes
from atkin import atkin

if __name__ == "__main__":

    n = 1_000

    eratosthenes_start = perf_counter()
    eratosthenes_sieve = eratosthenes(n)
    eratosthenes_end = perf_counter()

    atkin_start = perf_counter()
    atkin_sieve = atkin(n)
    atkin_end = perf_counter()

    print(eratosthenes_sieve.sum())
    print(eratosthenes_end - eratosthenes_start)

    print(atkin_sieve.sum())
    print(atkin_end - atkin_start)
