# ===============================================================================================================================
#                                       PYTHON MAP, FILTER, AND REDUCE
# ===============================================================================================================================

from functools import reduce

# ===============================================================================================================================
# PART 1: UNDERSTANDING HIGHER-ORDER FUNCTIONS
# ===============================================================================================================================

# DEFINITION:
# - In Python, functions are first-class citizens, meaning they can be passed around as arguments just like variables.
# - A "higher-order function" is a function that takes one or more functions as arguments or returns a function.
# - `map`, `filter`, and `reduce` are built-in/standard library higher-order functions designed to process collections (like lists) efficiently.


# ===============================================================================================================================
# PART 2: THE `map()` FUNCTION
# ===============================================================================================================================

# DEFINITION & SYNTAX:
# - The `map()` function applies a given function to all items in an input iterable (like a list) and returns a map object (an iterator).
# - Syntax: map(function, iterable)
# - To view the results easily, we usually wrap the map object in `list()`, `tuple()`, or loop through it.

print("=== PART 2: The `map()` Function Demo ===")

# Example 1: Double every number in a list using a lambda function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

print(f"Original numbers: {numbers}")
print(f"Mapped (doubled) list: {doubled}")

# Example 2: Convert a list of string numbers into actual integers
string_numbers = ["10", "20", "30", "40"]
integers = list(map(int, string_numbers))
print(f"Converted strings to integers: {integers}\n")


# ===============================================================================================================================
# PART 3: THE `filter()` Function
# ===============================================================================================================================

# DEFINITION & SYNTAX:
# - The `filter()` function evaluates each item in an iterable through a boolean function (a function that returns True or False).
# - It keeps only the items for which the function returns `True`.
# - Syntax: filter(function, iterable)

print("=== PART 3: The `filter()` Function Demo ===")

# Example 1: Filter out only the even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original numbers: {numbers}")
print(f"Filtered (evens only) list: {evens}")

# Example 2: Filter out empty strings from a list of words
words = ["apple", "", "banana", "   ", "cherry", ""]
non_empty_words = list(filter(lambda w: w.strip() != "", words))
print(f"Filtered non-empty words: {non_empty_words}\n")


# ===============================================================================================================================
# PART 4: THE `reduce()` FUNCTION
# ===============================================================================================================================

# DEFINITION & SYNTAX:
# - The `reduce()` function applies a rolling computation to sequential pairs of values in a list, reducing the entire list to a single cumulative value.
# - Note: It is not a built-in global function anymore in Python 3; it must be imported from the `functools` module (`from functools import reduce`).
# - Syntax: reduce(function, iterable)

print("=== PART 4: The `reduce()` Function Demo ===")

# Example 1: Find the sum of all elements in a list
numbers = [1, 2, 3, 4, 5]
# Behind the scenes: ((1 + 2) + 3) + 4) + 5 = 15
total_sum = reduce(lambda x, y: x + y, numbers)

print(f"Original numbers: {numbers}")
print(f"Reduced (Total Sum): {total_sum}")

# Example 2: Find the maximum number in a list using reduce
max_number = reduce(lambda a, b: a if a > b else b, [15, 42, 8, 99, 23])
print(f"Maximum number found via reduce: {max_number}\n")


# ===============================================================================================================================
# PART 5: QUICK SUMMARY CHEATSHEET
# ===============================================================================================================================

# def print_summary():
#     print("=== PART 5: Quick Summary Cheatsheet ===")
#     print("---------------------------------------------------------------------------------------------------------")
#     print("Function        | What it does                             | Output Size (Relative to Input)")
#     print("---------------------------------------------------------------------------------------------------------")
#     print("map()           | Applies a function to ALL items          | Same size as input")
#     print("filter()        | Keeps items that return True             | Equal or smaller than input")
#     print("reduce()        | Rolls items into a SINGLE cumulative value| Single value (scalar)")
#     print("---------------------------------------------------------------------------------------------------------")
#     print("\n[Map, Filter, and Reduce Masterclass execution completed successfully!]")

# if __name__ == "__main__":
#     print_summary()