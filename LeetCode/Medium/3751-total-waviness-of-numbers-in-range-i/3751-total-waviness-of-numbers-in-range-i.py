class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wavy = 0
        for i in range(num1, num2+1):
            numb = str(i)
        #for index, num in enumerate(num1, num2+1, 1):\
            for i in range(1,len(numb)-1):
                if numb[i] < numb[i-1] and numb[i] < numb[i+1]:
                    #print(numb,numb[i])
                    wavy +=1
                elif numb[i] > numb[i-1] and numb[i] > numb[i+1]:
                    #print(numb,numb,numb[i])
                    wavy+=1
        return wavy
             