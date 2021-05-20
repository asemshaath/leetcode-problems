class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        includedNums = set()
        smallest = list() # smallest list
        biggest = list()
        intersected = list() 
        
        if len(nums1) > len(nums2):
            smallest = nums2
            biggest = nums1
        else:
            smallest = nums1
            biggest = nums2
            
        # add smallest values to the set
        for i in range(len(smallest)):
            includedNums.add(smallest[i])
        
        for i in range(len(biggest)):
            
            if biggest[i] in includedNums:
                intersected.append(biggest[i])
                includedNums.remove(biggest[i])
                
        return intersected
        
