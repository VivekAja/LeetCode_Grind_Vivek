from collections import Counter
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                counts = Counter(nums[i:j])
                #print(counts)
                if counts[target] > len(nums[i:j]) // 2:
                    count +=1
        return count
        """

        balance_counts = {0: 1}
        
        current_balance = 0
        total_subarrays = 0
        

        valid_previous_counts = 0
        
        for num in nums:
            # 1. Update the balance score
            if num == target:
                # If we hit target, the score goes up, making previous equal scores valid
                valid_previous_counts += balance_counts.get(current_balance, 0)
                current_balance += 1
            else:
                # If we hit non-target, score drops, removing previous drop points from validity
                current_balance -= 1
                valid_previous_counts -= balance_counts.get(current_balance, 0)
            
            # 2. Add all valid configurations found so far to our total
            total_subarrays += valid_previous_counts
            
            # 3. Store the current balance state in our history tracking
            balance_counts[current_balance] = balance_counts.get(current_balance, 0) + 1
            
        return total_subarrays