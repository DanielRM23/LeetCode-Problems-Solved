# PROBLEM

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


def maxArea(height):
    # height = List[int]
    # Solution by using two pointers
    # One at the begginig and other at the end, these one are indices, don´t forget it
    # They advance until finding each other

    left = 0
    right = len(height) - 1
    # We need a variable to store the actual area
    area = 0

    while left <= right:
        # Compute the actual area
        base = right - left  # container's base
        min_height = min(
            height[left], height[right]
        )  # We need to take the min height, a bigger hight can't store all the water
        actual_area = base * min_height

        # Compare both areas, if the actua it's better, store it
        if actual_area > area:
            area = actual_area

        # We need to change the pointer that has the min height if the area is not maximum
        if min_height == height[left]:
            left += 1
        else:
            right -= 1

    return area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 1]
print(maxArea(height))
