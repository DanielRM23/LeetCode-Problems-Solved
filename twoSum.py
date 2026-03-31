def twoSum(nums, target):
    # We create a hash table to store the values
    visited = {}
    # Number of elements
    n = len(nums)

    # Do the search
    for i in range(n):
        difference = target - nums[i]
        # If the difference is in the dict, we return the indexes
        if difference in visited:  # O(1) because is a hash table
            return [i, visited[difference]]
        else:
            # If not, we add the number at the hash map
            # key = nums[i], value = index[nums[i]]
            visited[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
