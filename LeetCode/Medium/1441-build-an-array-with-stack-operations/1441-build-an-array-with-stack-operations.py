class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        cur = 1
        ops = []
        for i in target:
            while cur < i:
                ops.extend(["Push", "Pop"])
                cur+=1
            ops.append("Push")
            cur+=1
        return ops