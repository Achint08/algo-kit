# Seive of eraosthenes is used to get prime numbers uptil number n.
# There are two central ideas here:
# 1. We can loop over multiple of prime number encountered to mark them as non-prime, incrementally.
# 2. We only need to check the multiples till square root of n.
#
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/


def soe(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):

        if is_prime[p]:
            for k in range(p * 2, n + 1, p):
                is_prime[k] = False

    return is_prime


if __name__ == '__main__':
    for idx, k in enumerate(soe(1000)):
        if k:
            print(idx)
