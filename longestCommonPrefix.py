# PROBLEM

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


def longestCommonPrefix(strs):
    # Check if there are no strings
    if len(strs) == 0:
        return ""

    # by using divide and conquer
    left = 0
    right = len(strs) - 1
    return divide_and_conquer(strs, left, right)


def divide_and_conquer(strs, left, right):
    # left and right are indices, since where we're gonna look for

    # Base case, if the indices are the same we return the string
    if left == right:
        return strs[left]
    else:
        # split into half
        mid = (left + right) // 2
        # We do operate since [left, mid]
        string_left = divide_and_conquer(strs, left, mid)
        # We do operate since [mid, right]
        string_right = divide_and_conquer(strs, mid + 1, right)

        # At this point, I have to compare two strings
        # So, string_left and string_right are strings
        solution = findLongestCommonPrefix(string_left, string_right)

        return solution


def findLongestCommonPrefix(string_left, string_right):
    # We need to iterate over the min length of both strings
    # There is no sense if we do it on the max length
    min_length = min(len(string_left), len(string_right))
    # Store the letters in commun of each word
    commun_string = ""
    for i in range(0, min_length):
        # If the letter i is the same, the store it in commun_string
        if string_left[i] == string_right[i]:
            commun_string += string_left[i]
        else:
            # If not, just break the cicle
            break
    return commun_string


strs = ["leetcode", "leet", "lee", "le"]
strs = ["flower", "flow", "flight"]

# print(findLongestCommonPrefix(strs[0], strs[1]))
print(longestCommonPrefix(strs))
