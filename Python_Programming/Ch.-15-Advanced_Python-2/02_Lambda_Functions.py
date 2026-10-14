# ===============================================================================================================================
#                                       PYTHON LAMBDA FUNCTIONS
# ===============================================================================================================================


# ===============================================================================================================================
# PART 1: WHAT IS A LAMBDA FUNCTION?
# ===============================================================================================================================

# DEFINITION & SYNTAX:
# - A lambda function is a small, anonymous (nameless) function in Python.
# - Unlike standard functions defined using `def`, lambda functions are defined using the `lambda` keyword.
# - Syntax: lambda arguments: expression
# - Note: It can take any number of arguments, but can only have ONE expression. The expression is evaluated and returned automatically.

print("=== PART 1: Basic Lambda Function Demo ===")

# Example 1: A simple lambda function that adds 10 to a number
add_ten = lambda x: x + 10
print(f"Result of add_ten(5): {add_ten(5)}")

# Example 2: Lambda with multiple arguments
multiply = lambda a, b: a * b
print(f"Result of multiply(4, 5): {multiply(4, 5)}\n")


# ===============================================================================================================================
# PART 2: REGULAR FUNCTIONS VS. LAMBDA FUNCTIONS
# ===============================================================================================================================

# COMPARISON & USE CASES:
# - Regular Function (`def`): Used for complex logic, multi-line blocks, and reusable components with a proper name.
# - Lambda Function: Used for short, throwaway operations where defining a full `def` function is unnecessary or too verbose.
# - They are commonly passed as arguments to higher-order functions (functions that take other functions as arguments).

print("=== PART 2: Regular vs Lambda Function Comparison ===")

# Equivalent Regular Function:
def square_regular(x):
    return x * x

# Equivalent Lambda Function:
square_lambda = lambda x: x * x

print(f"Regular function output for 6: {square_regular(6)}")
print(f"Lambda function output for 6: {square_lambda(6)}\n")


# ===============================================================================================================================
# PART 3: USING LAMBDA WITH BUILT-IN FUNCTIONS (MAP, FILTER, SORTED)
# ===============================================================================================================================

# USAGE WITH HIGHER-ORDER FUNCTIONS:
# 1. map(function, iterable): Applies the lambda function to every item in an iterable.
# 2. filter(function, iterable): Filters items based on whether the lambda expression returns True.
# 3. sorted(iterable, key=function): Sorts an iterable based on a custom key returned by the lambda function.

print("=== PART 3: Lambda with Map, Filter, and Sorted Demo ===")

numbers = [1, 2, 3, 4, 5]

# 1. MAP: Double each number in the list
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"Original numbers: {numbers}")
print(f"After map (doubled): {doubled_numbers}")

# 2. FILTER: Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"After filter (evens only): {even_numbers}")

# 3. SORTED: Sort a list of tuples (names and ages) by age
people = [("Alice", 25), ("Bob", 22), ("Charlie", 28)]
sorted_people = sorted(people, key=lambda person: person[1])
print(f"Sorted people by age: {sorted_people}\n")


# ===============================================================================================================================
# PART 4: QUICK SUMMARY & BEST PRACTICES
# ===============================================================================================================================

# KEY TAKEAWAYS:
# - Lambda functions are anonymous and defined using the `lambda` keyword.
# - Restricted to a single expression (no complex loops, assignments, or multiple statements).
# - Best used for short operations or as arguments for functions like `map`, `filter`, and `sorted`.
# - If the logic becomes complex or needs reuse, always switch back to a standard `def` function for readability.

def print_summary():
    print("=== PART 4: Lambda Quick Summary ===")
    print("Syntax: lambda args: expression")
    print("Rule of Thumb: Keep it short, simple, and readable!")
    print("\n[Lambda Masterclass execution completed successfully!]")

if __name__ == "__main__":
    print_summary()