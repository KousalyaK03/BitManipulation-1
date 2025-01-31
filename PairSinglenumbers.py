# Approach: 
# We will use XOR to solve this problem in linear time and constant space. XOR has the property that:
# 1. a^a = 0 (XOR of a number with itself is 0)
# 2. a^0 = a (XOR of a number with 0 is the number itself)
# Thus, if we XOR all the numbers in the array, the numbers that appear twice will cancel out, 
# and we will be left with the XOR of the two unique numbers. To find these two numbers, 
# we can use the rightmost bit that is set in the XOR result and divide the numbers into two groups 
# based on whether the bit is set or not. Finally, XOR each group to get the two unique numbers.

# Time Complexity: O(n), where n is the number of elements in the array
# Space Complexity: O(1), constant space

def singleNumber(nums):
    # Step 1: XOR all elements to get the XOR of the two unique numbers
    xor_result = 0
    for num in nums:
        xor_result ^= num
    
    # Step 2: Find the rightmost set bit (this bit is different between the two unique numbers)
    rightmost_set_bit = xor_result & -xor_result
    
    # Step 3: Divide the numbers into two groups and XOR each group to get the two unique numbers
    num1, num2 = 0, 0
    for num in nums:
        if num & rightmost_set_bit:
            num1 ^= num
        else:
            num2 ^= num
    
    # Step 4: Return the two unique numbers
    return [num1, num2]

# Test cases
print(singleNumber([1,2,1,3,3,4,4,8,2,5]))  # Output: [8, 5]
print(singleNumber([4,1,2,1,2]))  # Output: [4]
