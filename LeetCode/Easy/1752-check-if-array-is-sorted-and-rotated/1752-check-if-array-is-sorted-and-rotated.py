class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        count, dupli = 0,0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                dupli+=1
            elif nums[i]+1 == nums[i+1]:
                count+=1
        print(count+dupli)
        if count+dupli+1 == len(nums):
            
            return True
        else:
            return False
            
        count, dupli, a = 0,0,0
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                count+=1
            elif nums[i] == nums[i+1]:
                dupli+=1
            else:
                a +=1
        print(count,dupli, a)
        if a>=2:
            
            return False
        else:
            return True
            """
        
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%(len(nums))]:
                count += 1
        return not count>1

        