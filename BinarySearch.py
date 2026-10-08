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


def binarySearchRecursive(nums, target, left, right):
    # By recursion

    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    else:
        if nums[mid] < target:
            return binarySearchRecursive(nums, target, mid + 1, right)
        else:
            return binarySearchRecursive(nums, target, left, mid - 1)


nums = [-1, 0, 3, 5, 9, 12]
target = 9
left = 0
right = len(nums) - 1

print(binarySearchRecursive(nums, target, left, right))


def binarySearchRecursivePractice(array, target, left, right):
    if left > right:
        return -1  # en este caso no se encontró el elemento

    # Partimos el arreglo por la mitad
    mid = (left + right) // 2

    # Si el elemento que queremos es el de la mitad, terminamos
    if array[mid] == target:
        return mid
    else:
        # De lo contrario se busca en otras regiones
        # Si el elemento de la mitad es menor al target, entonces buscamos
        # a la derecha
        if array[mid] < target:
            return binarySearchRecursivePractice(array, target, mid + 1, right)
        else:  # array[mid] > target
            return binarySearchRecursivePractice(array, target, left, mid - 1)


print(binarySearchRecursivePractice(nums, target, left, right))
