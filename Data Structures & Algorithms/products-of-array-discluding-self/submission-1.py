class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prev = [0] * n
        post = [0] * n
        res = [0] * n

        # [1, 0, 0, 0]
        prev[0] = 1
        # [0, 0, 0, 1]
        post[n - 1] = 1

        for i in range(1, n):
            prev[i] = nums[i - 1] * prev[i - 1]
        
        for i in range(n-2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
        
        for i in range(n):
            res[i] = prev[i] * post[i]

        return res