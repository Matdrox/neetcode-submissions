class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 4, 6]
        output = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        
        # [1, 1, 2, 8]
        print(f"FORWARD: {output}")

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post
            post *= nums[i]

        print(f"BACKWARD: {output}")
        return output