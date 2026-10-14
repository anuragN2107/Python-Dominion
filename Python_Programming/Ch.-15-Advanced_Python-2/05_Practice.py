# ===============================================================================================================================
#                                      PYTHON PRACTICE SET (LAMBDAS, STRINGS, & HIGHER-ORDER FUNCTIONS)
# ===============================================================================================================================

from functools import reduce


# ===============================================================================================================================
# PROBLEM 1: Lambda Function for Cube Calculation
# ===============================================================================================================================
# Question: Write a lambda function that calculates the cube of a given number and test it with an integer.

print("=== PROBLEM 1: Lambda Cube Calculator ===")

# Defining a lambda function to calculate the cube
cube_lambda = lambda x: x ** 3

test_number = 4
result = cube_lambda(test_number)
print(f"The cube of {test_number} is: {result}\n")


# ===============================================================================================================================
# PROBLEM 2: String `join()` for CSV Generation
# ===============================================================================================================================
# Question: Given a list of employee names, write a program using the `join()` method to combine them into a single comma-separated string.

print("=== PROBLEM 2: String `join()` CSV Generation ===")

employees = ["Alice", "Bob", "Charlie", "Diana"]

# Using join with a comma-space separator
csv_employees = ", ".join(employees)
print(f"Employee list: {employees}")
print(f"Formatted CSV string: {csv_employees}\n")


# ===============================================================================================================================
# PROBLEM 3: String `format()` with Named Keywords
# ===============================================================================================================================
# Question: Write a template string using `str.format()` with named placeholders for product name, price, and stock status.

print("=== PROBLEM 3: String `format()` Named Arguments ===")

template = "Product: {name} | Price: ${price:.2f} | In Stock: {status}"
formatted_product = template.format(name="Wireless Mouse", price=29.99, status=True)

print(formatted_product)
print()


# ===============================================================================================================================
# PROBLEM 4: Using `map()` to Square Numbers
# ===============================================================================================================================
# Question: Given a list of integers, use `map()` combined with a lambda function to generate a new list containing the square of each number.

print("=== PROBLEM 4: `map()` Function to Square Numbers ===")

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}\n")


# ===============================================================================================================================
# PROBLEM 5: Using `filter()` for Positive Numbers
# ===============================================================================================================================
# Question: Given a list containing both positive and negative integers, use `filter()` and a lambda function to extract only the positive numbers.

print("=== PROBLEM 5: `filter()` for Positive Numbers ===")

mixed_numbers = [-5, 12, -3, 0, 8, -1, 22]
positive_numbers = list(filter(lambda x: x > 0, mixed_numbers))

print(f"Original mixed numbers: {mixed_numbers}")
print(f"Filtered positive numbers: {positive_numbers}\n")


# ===============================================================================================================================
# PROBLEM 6: Using `reduce()` to Find Product of Elements
# ===============================================================================================================================
# Question: Use `reduce()` from the `functools` module to calculate the product of all elements in a given numeric list.

print("=== PROBLEM 6: `reduce()` for Product Calculation ===")

factors = [2, 3, 4, 5]
# Multiplies sequential items cumulatively: ((2 * 3) * 4) * 5 = 120
total_product = reduce(lambda x, y: x * y, factors)

print(f"Factors list: {factors}")
print(f"Total product: {total_product}\n")


# ===============================================================================================================================
# PROBLEM 7: Combining `map()` and `filter()` Pipeline
# ===============================================================================================================================
# Question: Write a program that first filters out numbers less than 10 from a list, and then cubes the remaining numbers using `map()`.

print("=== PROBLEM 7: `filter()` and `map()` Pipeline ===")

raw_data = [5, 12, 8, 15, 3, 20]

# Step 1: Filter numbers >= 10
filtered_data = filter(lambda x: x >= 10, raw_data)
# Step 2: Cube the filtered numbers using map
final_result = list(map(lambda x: x ** 3, filtered_data))

print(f"Raw data: {raw_data}")
print(f"Filtered (>=10) and Cubed result: {final_result}\n")


# ===============================================================================================================================
# PROBLEM 8: Advanced `str.format()` Padding and Alignment
# ===============================================================================================================================
# Question: Write a script that formats a table row with left-aligned product names and right-aligned prices using `str.format()` specifiers.

print("=== PROBLEM 8: Advanced Formatting & Alignment ===")

item_name = "Keyboard"
item_price = 45.5

# Left align item name in 12 spaces, right align price in 8 spaces with 2 decimals
table_row = "| {:<12} | {:>8.2f} |".format(item_name, item_price)
print("Formatted Table Row:")
print(table_row)
print()


# ===============================================================================================================================
# PROBLEM 9: Lambda with `sorted()` for Custom Sorting
# ===============================================================================================================================
# Question: Given a list of student score tuples `(name, score)`, use `sorted()` with a lambda key to sort the students by score in descending order.

print("=== PROBLEM 9: Lambda with `sorted()` Custom Key ===")

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]

# Sort by score (index 1 of tuple) in descending order using reverse=True
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)

print(f"Original students: {students}")
print(f"Sorted students by score (High to Low): {sorted_students}\n")


# ===============================================================================================================================
# PROBLEM 10: Comprehensive Pipeline (Lambda, Join, and Filter)
# ===============================================================================================================================
# Question: Given a list of words, filter out words with a length less than 5, convert the remaining to uppercase via `map`, and join them with hyphens.

print("=== PROBLEM 10: Comprehensive Pipeline Practice ===")

words_collection = ["python", "ai", "code", "developer", "lambda", "web"]

# Step 1: Filter words with length >= 5
long_words = filter(lambda w: len(w) >= 5, words_collection)

# Step 2: Convert filtered words to uppercase
upper_words = map(lambda w: w.upper(), long_words)

# Step 3: Join them together using hyphens
result_slug = "-".join(upper_words)

print(f"Original collection: {words_collection}")
print(f"Processed hyphen slug: {result_slug}\n")
