# PROBLEM

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.
# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


def removeDuplicates(nums):
    # By two pointers using a for loop
    left = 0  # left pointer
    k = 1  # Here we count unique elements

    # Remember that the other pointer is here, at the for loop
    for right in range(len(nums)):
        # if both pointers don't point the same value, advance one value in left and replace the value in left for the right one
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
            # Count one diferent number
            k += 1

    return k, nums


def removeDuplicates(nums):
    # By two pointers using a while loop
    left = 0  # left pointer
    right = 0  # right pointer
    k = 1  # Here we count unique elements

    while right < len(nums):
        # if both pointers don't point the same value, advance one value in left and replace the value in left for the right one
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
            # Count one diferent number
            k += 1
        else:
            # if both pointers point the same value, advance one value in right
            right += 1

    return k, nums


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
