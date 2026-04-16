# PROBLEM

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


def sort_arrays_into_one(nums1, nums2):
    # Arrays' length
    length_nums1 = len(nums1)
    length_nums2 = len(nums2)

    # Create one array to store the new sorted array, it takes O(n+m) in space
    sorted_array = [0] * (length_nums1 + length_nums2)

    # i to move over nums1
    # j to move over nums2
    # k to mover over the new array
    i = 0
    j = 0
    k = 0

    # Compare the elements and srting them if the condition is satisfied
    while i < length_nums1 and j < length_nums2:
        if nums1[i] <= nums2[j]:
            sorted_array[k] = nums1[i]
            # Move one step in array 1
            i += 1
        else:
            sorted_array[k] = nums2[j]
            # Move one step in array 2
            j += 1
        # Move one step in the new array
        k += 1

    # Move the missing elements in nums2, this happens only if j< length_nums2
    while j < length_nums2:
        sorted_array[k] = nums2[j]
        j += 1
        k += 1

    # Move the missing elements in nums1, this happens only if j< length_nums1
    while i < length_nums1:
        sorted_array[k] = nums1[i]
        i += 1
        k += 1

    return sorted_array


def findMedianSortedArrays(nums1, nums2):
    # Sort the arrays
    sorted_array = sort_arrays_into_one(nums1, nums2)
    # Find the mid term
    mid_term = len(sorted_array) // 2
    median = None
    # If len(sorted_array) is even, compute the media
    if len(sorted_array) % 2 == 0:
        median = (sorted_array[mid_term - 1] + sorted_array[mid_term]) / 2
    else:
        # If not, just return the mid value
        median = sorted_array[mid_term]

    return median


nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print(findMedianSortedArrays(nums1, nums2))
