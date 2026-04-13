# PROBLEM

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


def minSubArrayLen(target, nums):
    index_left = 0
    max_sum = 0
    minimal_length = float("inf")

    # We need a for to walk over the string
    for index_right in range(0, len(nums)):
        # if the condition is not broken, add the element to the subarray and advance one step
        max_sum += nums[index_right]
        # check if the condition is broken
        while max_sum >= target:
            window_size = index_right - index_left + 1
            minimal_length = min(minimal_length, window_size)
            # if the condition is broken we need to subtract the number since the beggining
            max_sum -= nums[index_left]

            # Advance one step
            # It always goes to the end of the while-loop
            index_left += 1

    # Compare the minimal_length, and return it
    if minimal_length != float("inf"):
        return minimal_length
    else:
        return 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))
