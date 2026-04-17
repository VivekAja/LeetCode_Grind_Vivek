class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
    
        chars = "0123456789abcdef"
        result = []
    
        for _ in range(8):  # Max 8 hex digits for 32 bits
            rem = num & 0xF
            result.append(chars[rem])
            num >>= 4   # In Python, >> on negative works with sign extension, but since we limit to 8 shifts, it's fine after masking if needed
        
        # Alternative clean way with mask:
        # num = num & 0xFFFFFFFF  # Force 32-bit unsigned
        
        return ''.join(reversed(result)).lstrip('0') or '0'  # Remove leading zeros