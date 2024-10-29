# def greetings(name):
#     return f"hello {name}"
# print(greetings('faith')

# def WordCount(strParam):
#     new = strParam.split()
#     return len(new)
# print(WordCount(input()))

# def Palindrome(strParam):
#     cleaned = strParam.replace(" ","").lower()
#     if cleaned == cleaned[::-1]:
#       return "true"
#     else:
#       return "false"
# print(Palindrome(input()))


# Question2: 👇👇                                                                                    from collections import Counter


# Question3: 👇👇                                                                               def sort_array(arr):
    """
    Sort the array in ascending order.

    Parameters:
    - arr: List of integers.

    Returns:
    - A sorted list in ascending order.
    """
    return sorted(arr)

input_array = [5, 1, 3, 4, 2, 8, 7, 6, 10]
print(f"Sorted array: {sort_array(input_array)}")