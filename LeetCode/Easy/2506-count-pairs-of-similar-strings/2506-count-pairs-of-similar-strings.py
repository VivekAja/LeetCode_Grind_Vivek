
class Solution:
    def similarPairs(self, strs: List[str]) -> int:
    
        counts = {}
    
        for s in strs:
            unique_key = "".join(sorted(set(s)))
            counts[unique_key] = counts.get(unique_key, 0) + 1
            total_pairs = 0 
        for n in counts.values():
            if n > 1:
                total_pairs += (n * (n - 1)) // 2          
        return total_pairs


            