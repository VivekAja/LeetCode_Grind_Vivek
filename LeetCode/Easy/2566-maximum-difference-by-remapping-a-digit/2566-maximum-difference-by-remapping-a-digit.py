class Solution:
    def minMaxDifference(self, num: int) -> int:
        s_num = str(num) # Convert the integer to a string

        # --- Calculate maxNum ---
        max_s_num = list(s_num) # Convert to a list of characters for mutability
        
        # Find the first character that is not '9'
        char_to_replace_for_max = ''
        for char in max_s_num:
            if char != '9':
                char_to_replace_for_max = char
                break
        
        # Replace all occurrences of that character with '9'
        if char_to_replace_for_max != '': # Only proceed if a character to replace was found
            for i in range(len(max_s_num)):
                if max_s_num[i] == char_to_replace_for_max:
                    max_s_num[i] = '9'
        
        max_num_val = int("".join(max_s_num)) # Join list back to string and convert to int

        # --- Calculate minNum ---
        min_s_num = list(s_num) # Convert to a list of characters for mutability
        
        # The logic for minNum is to replace the first digit with '0'.
        # The original C++ code was replacing ALL occurrences of the FIRST digit with '0'.
        # Let's follow that exact logic from the C++ code.
        char_to_replace_for_min = min_s_num[0] # Get the first digit
        
        for i in range(len(min_s_num)):
            if min_s_num[i] == char_to_replace_for_min:
                min_s_num[i] = '0'

        min_num_val = int("".join(min_s_num)) # Join list back to string and convert to int

        return max_num_val - min_num_val