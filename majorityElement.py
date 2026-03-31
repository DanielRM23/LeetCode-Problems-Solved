# Problem

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

from collections import defaultdict


def majorityElement(nums: int):
    # Use a defaultdict to store the numbers' frequencies
    frequencies = defaultdict(int)
    for num in nums:
        frequencies[num] += 1

    # Take the max value, which has more appearances
    majority_element = max(frequencies, key=frequencies.get)

    return majority_element


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
