# Problem:
# Given an integer x, return true if x is a palindrome, and false otherwise.
# There are two solutions here


def isPalindrome(x: int):
    # The number must be greater than zero
    if x < 0:
        return False

    x_string = str(x)  # It takes O(log n)
    n = len(x_string)
    # Compare the first elements with the finals, if they not match
    # the number is not a palindrome
    is_palindrome = None
    for i in range(n):
        if x_string[i] != x_string[n - i - 1]:
            is_palindrome = False
            break  # It is very important to break the cicle
        else:
            is_palindrome = True

    return is_palindrome


def isPalindrome2(x: int):
    x_string = str(x)
    x_inverse = x_string[::-1]  # The reverse of the string
    if x_string != x_inverse:  # Just compare both strings
        return False

    return True


x = 100001
print(isPalindrome2(x))


def isPalindrome3(n: int):
    if n < 0:
        return False

    actual = n  # Store a copy of the original number
    reversed_num = (
        0  # In this variable we'll build a new number, readed in reverse order
    )

    while n > 0:
        # With this operation we take the last digit of a number
        # For example 127%10 = 7
        digit = n % 10
        # With this operation we move one position to the left, adding a zero
        reversed_num = reversed_num * 10 + digit
        # By doing this operation, we drop the last digit
        n = n // 10

    if reversed_num == actual:
        return True
    else:
        return False


print("Rsultado de la función 3:", isPalindrome3(x))
