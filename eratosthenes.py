import numpy as np
import numba as nb
import numpy.typing as npt

@nb.jit(nopython = True, cache = True, nogil = True, fastmath = True, boundscheck = False)
def eratosthenes(n: int) -> npt.NDArray[bool]:
    length = n + 1
    sieve = np.full(length, True, dtype = np.bool)
    sieve[0:2] = False

    for i in range(2, int(np.sqrt(length)) + 1):
        if sieve[i]:
            sieve[2*i:length:i] = False

    return sieve
