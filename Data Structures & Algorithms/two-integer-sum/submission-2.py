class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            #dic[nums[i]] = target - nums[i]
            if target - nums[i] in dic:
                return[dic[target - nums[i]],i]
            dic[nums[i]] = i # stores the index and number