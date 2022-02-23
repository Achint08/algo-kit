# Euclid algoritm is based on the idea that
# let's say we have to find gcd of a and b, i.e. x.
# here, let's say a is greater than b, then, if x divides
# a and b, then x also divides a % b since a can also be written
# as a = quo * b + remain, i.e., for a to be divisible by x, remain should be
# divisible by x. We can now, reduce the problem recursively to a base case, when
# one of either x or y is zero, in that case, other number is the GCD.
#
# Link - https://www.youtube.com/watch?v=B5HKW99AvV0


def euclid_gcd(x, y):
    if y == 0:
        return x

    return euclid_gcd(y, x % y)


if __name__ == '__main__':
    print(euclid_gcd(15, 10))
