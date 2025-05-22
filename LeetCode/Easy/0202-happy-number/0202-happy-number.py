class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True

        
        seen = set()
        while True:
            temp = 0
            for c in str(n):
                temp += int(c)* int(c)
            print(temp)
            #if temp == 1:
                #return True
            if temp not in seen:
                seen.add(temp)
            elif temp ==1:
                return True   
            else:
                return False
            n = temp
            