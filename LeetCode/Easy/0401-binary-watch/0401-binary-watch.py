from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
               # This list comprehension will collect all possible time formats
        time_formats = [
            '{:d}:{:02d}'.format(hour, minute)
            for hour in range(12)       # Loop through the 12 hours
            for minute in range(60)     # Loop through the 60 minutes
            if (bin(hour) + bin(minute)).count('1') == turnedOn
            # Check if the sum of the bits set to '1' in both the hour's and 
            # minute's binary representation equals the number of LEDs that are lit
        ]
      
        return time_formats