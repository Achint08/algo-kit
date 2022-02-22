# The purpose of rolling hash is to store the string efficiently
# in a manner that we can reduce the time of string matching to
# linear time complexity. If we use brute force or naive approach,
# the time complexity is O(n^2).
# Checkout - https://codeforces.com/blog/entry/60445
# Hash matching never guarantees string exists as substring. We need to
# perform the action to ensure that hypothesis actually exists.
# Note -
# 1. It's a good time to revise some basic properties about modulus.
# https://math.stackexchange.com/questions/147140/what-are-the-properties-of-the-modulus


def count_rolling_hash(s1, s2):

    P1 = 51
    P2 = 57
    m1 = 2 ** 32
    m2 = 2 ** 31 - 1
    l1_hash_val = 0
    l2_hash_val = 0
    n = len(s1)
    check_l1_hash_val = 0
    check_l2_hash_val = 0
    count = 0

    for idx, c in enumerate(s1):
        l1_hash_val += (((ord(c) - ord('a') + 1) * (P1 ** idx))) % m1
        l2_hash_val += (((ord(c) - ord('a') + 1) * (P2 ** idx))) % m2

    for idx, c in enumerate(s2[:n]):
        check_l1_hash_val += (((ord(c) - ord('a') + 1) * (P1 ** idx))) % m1
        check_l2_hash_val += (((ord(c) - ord('a') + 1) * (P2 ** idx))) % m2

    if check_l1_hash_val == l1_hash_val and check_l2_hash_val == l2_hash_val:
        for i in range(n):
            if s1[i] != s2[i]:
                break
        else:
            count += 1

    for idx, c in enumerate(s2[n:]):
        comp1 = ((ord(c) - ord('a') + 1) * (P1 ** n)) % m1
        comp2 = ((ord(s2[idx]) - ord('a') + 1)) % m1
        check_l1_hash_val = ((check_l1_hash_val - comp2 + comp1) // P1) % m1
        comp1 = ((ord(c) - ord('a') + 1) * (P2 ** n)) % m2
        comp2 = ((ord(s2[idx]) - ord('a') + 1)) % m2

        check_l2_hash_val = ((check_l2_hash_val - comp2 + comp1) // P2) % m2

        if check_l1_hash_val == l1_hash_val and check_l2_hash_val == l2_hash_val:
            for i in range(n):
                if s1[i] != s2[n:][i - n + 1 + idx]:
                    break
            else:
                count += 1

    return count


if __name__ == '__main__':

    print(count_rolling_hash('ach', 'achintach'))
