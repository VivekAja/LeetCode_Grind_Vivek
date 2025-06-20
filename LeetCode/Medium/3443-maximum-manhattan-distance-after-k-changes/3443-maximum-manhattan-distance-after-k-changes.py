class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        no , so, w, e = 0, 0, 0 ,0
        max_md = 0
        
        east = west = north = south = 0

        for i in range(len(s)):
            c = s[i]

            if c == 'E':
                east += 1
            elif c == 'W':
                west += 1
            elif c == 'N':
                north += 1
            elif c == 'S':
                south += 1

            curr_md = abs(east - west) + abs(north - south)

            steps = i + 1
            wasted = steps - curr_md

            extra = min(2 * k, wasted)

            final_current_md = curr_md + extra

            max_md = max(max_md, final_current_md)

        return max_md