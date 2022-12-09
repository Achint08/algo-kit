class Solution:
    def permute(self, nums):
        def backtrack(first):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        output = []
        backtrack(0)
        return output
    
s = Solution()
print(s.permute([1,2,3]))