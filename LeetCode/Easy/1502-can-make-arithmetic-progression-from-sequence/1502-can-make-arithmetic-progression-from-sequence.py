class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 1:
            return False
        arr= sorted(arr)
        saved = arr[0] - arr[1]

        for i in range(len(arr)-1):
            if arr[i] - arr[i+1] != saved:
                return False
        return True
