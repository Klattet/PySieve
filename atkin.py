import numpy as np
import numpy.typing as npt
import numba as nb

nb.jit(nopython = True, cache = True, nogil = True, fastmath = True, boundscheck = False)
def atkin(n: int) -> npt.NDArray[bool]:
    limit = n + 1
    sieve = np.full(limit, False)
    n_root = int(np.sqrt(n)) + 1

    n_root_range = np.square(np.arange(1, n_root))

    for x in n_root_range:
        for y in n_root_range:
            sol = 4 * x + y
            if sol < limit:
                mod = sol % 6
                if mod == 1 or mod == 5:
                    sieve[sol] ^= True

            sol -= x
            if sol < limit and sol % 12 == 7:
                sieve[sol] ^= True

            if x > y:
                sol -= 2 * y
                if sol < limit and sol % 6 == 5:
                    sieve[sol] ^= True

    for i in np.arange(5, n_root):
        if sieve[i]:
            i_squared = i*i
            sieve[i_squared:limit:i_squared] = False


    sieve[2:4] = True

    return sieve
