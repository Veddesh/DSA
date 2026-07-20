class Solution(object):
    def twoSum(self, nums, target):
        list_sum=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j==i:
                    continue
                elif nums[j]+nums[i]==target:
                    list_sum.append(i)
                    list_sum.append(j)
                    return list_sum
                    
                    
            