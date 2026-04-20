# PROBLEM

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


def moveZeroes(nums):
    # By two pointers
    left = 0
    right = 0

    # Here we store the previous values which are
    # nums[left] and nums[right]
    new_left = None
    new_right = None

    while right < len(nums):
        # With right we look for the numbers distinct to zero
        # and left is used to store the index where there is a zero
        if nums[right] != 0:
            # Store the previous values
            new_right = nums[right]
            new_left = nums[left]
            # swap the values
            nums[left] = new_right
            nums[right] = new_left

            left += 1
        # move over the array
        right += 1

    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))
