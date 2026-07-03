class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in counter.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) -1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res