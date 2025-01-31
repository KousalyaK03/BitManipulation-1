# Approach:
# Since we cannot use multiplication, division, or the modulo operator, we will use bitwise shifting.
# The idea is to subtract the divisor from the dividend multiple times efficiently.
# We achieve this by doubling the divisor (using bitwise left shift) until it is close to the dividend.
# Then, we subtract this value from the dividend and repeat the process.
# This allows us to achieve a logarithmic time complexity.
# Finally, we handle edge cases like overflow.
# Time Complexity: O(log n), where n is the absolute value of the dividend
# Space Complexity: O(1), constant space
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Step 1: Handle edge case for overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:  # Overflow case
            return INT_MAX
        
        # Step 2: Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)  # XOR to check if only one is negative
        
        # Step 3: Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        # Step 4: Perform bitwise subtraction using left shift for efficiency
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):  # Double the divisor
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the largest multiple from dividend
            dividend -= temp_divisor
            quotient += multiple
        
        # Step 5: Apply sign to the quotient
        return -quotient if negative else quotient

# Test cases
solution = Solution()
print(solution.divide(10, 3))  # Output: 3
print(solution.divide(7, -3))  # Output: -2
print(solution.divide(-2147483648, -1))  # Output: 2147483647 (to prevent overflow)