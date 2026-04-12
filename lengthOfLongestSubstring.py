# PROBLEM

# Given a string s, find the length of the longest substring without duplicate characters.

from collections import defaultdict


def lengthOfLongestSubstring(s):
    index_left = 0
    elements = defaultdict(str)
    length_best_string = 0

    # We need a for to walk over the string
    for index_right in range(0, len(s)):
        # STEP 1: check if the condition is not valid
        # If the letter is in the hash table (is repeated) we need to remove the letter at index_left and then advance for the left one step
        while s[index_right] in elements:
            del elements[s[index_left]]
            index_left += 1

        # STEP 2: If the condition is not broken, add the element, and advance one step to the right
        # Advance to the right in the foor loop, we don't need to do it explicity
        elements[s[index_right]] = s[index_right]

        # Calculate the window's length
        # Remember that we start to count since 0, that's why add a one
        length_window = index_right - index_left + 1

        # STEP 3: Update the variable that you are looking for
        # Update the length of the window
        # We want the maximum length
        length_best_string = max(length_best_string, length_window)

    return length_best_string


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
