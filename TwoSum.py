nums = [2,3,4,1]
target = 7

def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        # """
        # for i in nums:
            
        #     if((target - i) in nums):
        #         if(i != target - i):
        #             return [nums.index(i),nums.index(target-i)]

        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(i!=j):
                    if(nums[j] == target - nums[i]):
                        return [i,j]


print(twoSum(nums,target))