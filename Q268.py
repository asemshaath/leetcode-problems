class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            
            
            if nums[i] != i:
                return i
        
        return n
        
