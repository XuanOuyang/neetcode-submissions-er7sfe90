class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        max = len(nums)
        min = 0

        while min < max:
            middle = (max + min) // 2
            if target == nums[middle]:
                return middle
            
            elif nums[middle] > target: #middle = is bigger than target
                max = middle
            
            elif nums[middle] < target:
                min = middle + 1

        return -1
        
                


            