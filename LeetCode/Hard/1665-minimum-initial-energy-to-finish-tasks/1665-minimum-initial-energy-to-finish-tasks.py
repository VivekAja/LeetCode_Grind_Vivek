class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        sorted_tasks = sorted(tasks, key=lambda task: task[0] - task[1])
        init = 0
        cur = 0
        for i, j in sorted_tasks:
            if cur < j:
                deficit = j - cur
                init += deficit
                cur = j
            cur -=i
        return init