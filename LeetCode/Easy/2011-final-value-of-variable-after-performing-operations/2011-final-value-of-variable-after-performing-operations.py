class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for x in operations:
            if "+" not in x:
                count-=1
            else:
                count+=1
        return count