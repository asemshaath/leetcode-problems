class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if n == 1:
            return

        p1 = 0

        for p2 in range(1,n):

            if nums[p1] == 0 and nums[p2] != 0:
                temp = nums[p1]
                nums[p1] = nums[p2]
                nums[p2] = temp
                p1 += 1
            elif (nums[p2] == 0 and nums[p1] != 0) or (nums[p1] != 0 and nums[p2] != 0):
                p1 += 1


        
