class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice = True
        stones = 10

        while n >= stones and stones > 0:
            n -= stones
            stones -= 1
            alice = not alice
        
        return not alice