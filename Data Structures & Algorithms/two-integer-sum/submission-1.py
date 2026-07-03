class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm_nums = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hm_nums:
                print(f'Needed: {needed}, num: {nums[i]}')
                return [hm_nums[needed], i]
            hm_nums[nums[i]] = i