# PROBLEM

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


def merge(nums1, nums2, m, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    # Check if there is an empty array
    if nums1 == [] and nums2 != []:
        nums1 = nums2
        return nums1
    if nums1 != [] and nums2 == []:
        nums1 = nums1
        return nums1

    # "i" to move over nums1 and "j" to move over nums2
    i = m - 1
    j = n - 1
    # position where to put the element
    position = n + m - 1

    # We move over the array from the end to the start, that's why we substract -1 if the conditions of compare are satisfied
    while i >= 0 and j >= 0:
        if nums1[i] <= nums2[j]:
            nums1[position] = nums2[j]
            j -= 1
            position -= 1
        else:  # nums1[i - 1] >= nums2[j - 1]
            nums1[position] = nums1[i]
            i -= 1
            position -= 1

    # Move the missing elements in nums2, this happens only if j>=0
    while j >= 0:
        nums1[position] = nums2[j]
        j -= 1
        position -= 1
    return nums1


nums1 = [2, 0, 0]
m = 1
nums2 = [1, 1]
n = 2

print(merge(nums1, nums2, m, n))
