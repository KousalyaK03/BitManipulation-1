# Approach:
# We can solve this problem efficiently using XOR. The XOR operation has the following properties:
# 1. a^a = 0 (XOR of a number with itself is 0)
# 2. a^0 = a (XOR of a number with 0 is the number itself)
# 3. XOR is commutative and associative, meaning the order of operations doesn't matter.
# So, when we XOR all the numbers in the array, the numbers that appear twice will cancel each other out, 
# and we will be left with the number that appears only once.
# Time Complexity: O(n), where n is the number of elements in the array
# Space Complexity: O(1), constant space

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Step 1: Initialize result variable to 0
        result = 0
        
        # Step 2: XOR all elements in the array
        for num in nums:
            result ^= num
        
        # Step 3: Return the result, which will be the single number
        return result

# Test cases
solution = Solution()
print(solution.singleNumber([2,2,1]))  # Output: 1
print(solution.singleNumber([4,1,2,1,2]))  # Output: 4
print(solution.singleNumber([1]))  # Output: 1
