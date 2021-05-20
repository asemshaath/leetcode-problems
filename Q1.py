class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                
                try:
                    if(i == j):
                        continue
                    elif(nums[i] + nums[j] == target):
                        return [i, j]
                
                except(IndexError):
                    continue
