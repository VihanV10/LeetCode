class Solution:
    def myAtoi(self, s: str) -> int:
        # Strip leading whitespace
        s = s.lstrip()

        # Check for empty string
        if not s:
            return 0

        # Check for sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Convert digits to integer
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        # Apply sign
        result *= sign

        # Clamp result to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result