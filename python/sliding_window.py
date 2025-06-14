# Template

# end expands, while start pointer tries to contract
# def some_start_condition(s, e):
#     pass

# def process_logic_2(s, e):
#     pass

# def process_logic_1(s, e):
#     pass

# def sliding_window(arr):

#     n = len(arr)
#     start = end = 0
#     while(end < n):
#         end += 1
#         while(some_start_condition(start, end)):
#             process_logic_1(start, end)
#             start += 1

#         process_logic_2(start, end)


# Given a string S and a string T, find the minimum window in S which will contain all the characters in T.

from collections import Counter


def find_min_substring(s, t):
    start = end = 0
    counter = Counter(t)
    count = len(t)
    res = float('inf')
    while(end < len(s)):
        counter[s[end]] -= 1

        if counter[s[end]] >= 0:
            count -= 1
        end += 1

        while(count == 0):
            if end - start < res:
                res = end - start

            counter[s[start]] += 1
            if counter[s[start]] > 0:
                count += 1
            start += 1

    return res


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(find_min_substring(s, t))
