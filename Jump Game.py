class Solution:
    def canJump(self, nums: List[int]) -> bool:
        boundary = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= boundary:
                boundary = i
            
        return True if boundary == 0 else False
        
