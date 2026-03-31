# Problem
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

# There are two answers using python Sintax, and another one using arrays


def getConcatenation(nums):
    # This is a python sintax
    return nums * 2


def getConcatenation2(nums):
    # This is a python sintax
    return nums[::] + nums[::]


def getConcatenation3(nums):
    # We need to create a new array to store the new values
    # It has to be the double size of nums
    n = len(nums)
    ans = [0] * 2 * n

    # We use two variables to go over the array
    i = 0
    j = 0
    while i < 2 * n:
        # Copy the element
        ans[i] = nums[j]
        # Walk by the array
        i += 1
        j += 1
        if j == n:  # If this happens, it's time to copy the array
            j = 0

    return ans


nums = [1, 2, 1]
nums2 = [1, 3, 2, 0, 0]
print(getConcatenation3(nums2))
