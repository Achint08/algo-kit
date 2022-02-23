# The idea is to use D&C to reduce the complexity of the algorithm, by
# dividing the problem into two halves.
#
# https://codecrucks.com/exponential-problem-solving-using-divide-and-conquer/

def cal_pow(x, n):
    if n == 0:
        return 1

    # Here, we are performing AND operation of 1 with n,
    # to know if the number is odd or even. This is computationally
    # better than using mod.
    half_expo = cal_pow(x, n//2)
    ans = half_expo * half_expo
    if n & 1:

        return x * ans
    else:
        return ans


if __name__ == '__main__':
    print(cal_pow(2, 10))
    print(cal_pow(2, 11))
