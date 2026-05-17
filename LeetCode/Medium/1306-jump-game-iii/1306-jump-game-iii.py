from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])

        while queue:
            cur = queue.popleft()

            if arr[cur] == 0:
                return True
            jump = arr[cur]
            arr[cur] = -1
            for next_i in (cur+jump, cur-jump):
                if 0<= next_i < len(arr) and arr[next_i] >= 0:
                    queue.append(next_i)

        return False
 