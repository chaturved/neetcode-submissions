class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        sum_pair = defaultdict(set)
        res = set()

        for k in range(length):
            for l in range(k + 1, length):
                need = target - nums[k] - nums[l]
                for a, b in sum_pair.get(need, ()):
                    res.add((a, b, nums[k], nums[l]))
            for i in range(k):
                sum_pair[nums[i] + nums[k]].add((nums[i], nums[k]))

        return [list(q) for q in res]