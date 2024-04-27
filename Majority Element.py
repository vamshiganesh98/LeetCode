class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candElement = 0
        count = 0
        for i in range(0, len(nums)):
            if count == 0:
                candElement = nums[i]
            if nums[i] == candElement:
                count+=1
            else:
                count -=1
        return candElement


        
