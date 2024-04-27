class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if count < 2 or n!=nums[count-2]:
                nums[count] = n
                count+=1
            else:
                continue
        return count
