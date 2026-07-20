class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_list=nums1+nums2
        new_list.sort()
        length=len(new_list)
        if len(new_list)%2==1:
            return new_list[length//2]
        else:
            x=new_list[length//2]
            y=new_list[length//2 -1]
            return float((x+y)/2.0)

        
        