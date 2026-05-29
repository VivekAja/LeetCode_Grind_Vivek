class Solution:
    def minElement(self, nums: List[int]) -> int:
        summ = 0
        res = []
        for i in range(len(nums)):
            m = nums[i]
            
            """
            while m> 0 or summ > 9:
                if m == 0:
                    m = summ
                    summ = 0
                lastnumber = m%10
                summ += lastnumber
                m//=10
            res.append(summ)

            """
            while m> 0:
                
                lastnumber = m%10
                summ += lastnumber
                m//=10
            res.append(summ) 
            summ = 0        
        
        return min(res)

