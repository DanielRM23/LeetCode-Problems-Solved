# PROBLEM

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        # split in half
        mid = (left + right) // 2

        # Here we found the element
        if nums[mid] == target:
            return mid

        # Look for in the right half
        if nums[mid] < target:
            left = mid + 1
        # Look for in the left half
        else:
            right = mid - 1
    # If the element does not exist in the array
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(binarySearch(nums, target))
