class Solution:
    def subsets(self, nums):
        def backtrack(first, curr):
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
        n = len(nums)
        output = []
        for k in range(n+1):
            backtrack(0, [])
        return output
    
s = Solution()
print(s.subsets([1,2,3]))