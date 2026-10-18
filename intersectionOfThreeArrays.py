def contains(A, x):
    """
    A : An array of integers
    x : int
    Retuns True if the element "x" is in A
    """
    for i in range(len(A)):
        if A[i] == x:
            return True
    return False  # This is because we checked all the array and "x" is not in A


def intersect(A, B):
    """
    A, B : Arrays of integers
    Returns the common values of A and B without duplicates
    """
    AB = []
    for i in range(len(A)):
        if contains(B, A[i]) and not contains(AB, A[i]):
            AB.append(A[i])

    return AB


def intersectThree(A, B, C):
    AB = intersect(A, B)
    return intersect(AB, C)


from collections import defaultdict


def unique(arr):
    """Returns arr without repeated values"""
    seen = defaultdict(int)
    result = []
    for x in arr:
        if seen[x] == 0:  # first time we see x
            result.append(x)
            seen[x] = 1
    return result


def intersectThree2(A, B, C):
    """
    A, B, C : Arrays of integers
    return : The intersection of the three arrays
    """

    # The first step is to remove duplicates
    A = unique(A)
    B = unique(B)
    C = unique(C)

    # MERGE THE ARRAYS
    # this take us O(n1 + n+2 + n3) = O(max(n_i))
    # Create an array of lenght len(A) + len(B) + len(C).
    N = len(A) + len(B) + len(C)
    merge_array = N * [0]

    i = 0
    while i < len(A):
        merge_array[i] = A[i]
        i += 1

    j = 0
    while j < len(B):
        merge_array[len(A) + j] = B[j]
        j += 1

    k = 0
    while k < len(C):
        merge_array[len(A) + len(B) + k] = C[k]
        k += 1

    hash_table = defaultdict(
        int
    )  # Here we store how many times does every number appear
    for i in range(len(merge_array)):
        hash_table[merge_array[i]] += 1

    intersection = [key for key, value in hash_table.items() if value == 3]

    return intersection


print(intersectThree2([1, 2, 2, 3, 5], [2, 3, 3, 5, 7], [2, 5, 5, 8]))  # [2, 5]
print(intersectThree2([2, 2, 2], [5], [7]))  # []
print(intersectThree2([2, 2], [2], [2]))  # [2]
