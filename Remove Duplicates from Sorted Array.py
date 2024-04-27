class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                continue
            else:
                nums[count] = nums[i]
                count+=1
        return count
