class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(number):
            if number < 100:
                return 0
            digits = str(number)
            @cache
            def dfs(pos, tight, started,pp,p):
                #Base Case
                if pos == len(digits):
                    return 1, 0

                #Placing valid digits
                limit = int(digits[pos]) if tight else 9
                totalcount, totalwavy = 0, 0
                #shift window forward
                for d in range(limit+1):
                    newtight = tight and d == limit
                    newstarted = started and d == 0

                    if newstarted:
                        npp, np = -1, -1
                    elif started:
                        npp, np = -1, d
                    else:
                        npp, np = p, d
                    #Subproblem Result
                    nextcount, nextwavy= dfs(pos+1, newtight, newstarted, npp, np)
                    #Check if prev is wavyyy
                    mahol_pura_wavy = 0
                    if pp != -1 and p!= -1:
                        if (pp<p>d) or (pp>p<d):
                            mahol_pura_wavy = 1
                    # aggregate the result
                    totalcount += nextcount

                    totalwavy  += nextwavy + (mahol_pura_wavy * nextcount)

                return totalcount, totalwavy
            return dfs(0, True, True,-1,-1)[1]
        return solve(num2) - solve(num1 -1) 

