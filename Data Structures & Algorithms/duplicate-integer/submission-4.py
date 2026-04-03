class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        """
        map = set()
        for i in nums:
            if i in map:
                return True
            map.add(i)
        return False
        """