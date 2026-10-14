# ===============================================================================================================================
#                                       MASTER NOTES: PYTHON STRING METHODS (`join()` & `format()`)
# ===============================================================================================================================

# ===============================================================================================================================
# PART 1: THE `str.join()` METHOD IN PYTHON
# ===============================================================================================================================

# DEFINITION & BEHAVIOR:
# - The `join()` method is a string method used to concatenate/combine elements of an iterable (such as a list, tuple, or set of strings) into a single string.
# - It is called on the *separator* string, which is placed in between each element of the iterable.
# - Syntax: separator.join(iterable)
# - Important Rules: 
#   1. All items in the iterable must be strings; otherwise, Python will raise a `TypeError`.
#   2. If the iterable is empty, it returns an empty string `""`.

print("=== PART 1: `str.join()` Method Demos ===")

# Example 1: Joining a list of words with a space separator
words_list = ["Python", "is", "awesome"]
sentence = " ".join(words_list)
print(f"1. Space joined: {sentence}")

# Example 2: Joining with a hyphen separator (useful for slugs or dates)
date_parts = ["2026", "10", "14"]
hyphen_date = "-".join(date_parts)
print(f"2. Hyphen joined: {hyphen_date}")

# Example 3: Joining with an empty string separator (gluing characters together)
chars = ["H", "e", "l", "l", "o"]
joined_word = "".join(chars)
print(f"3. No separator (empty string): {joined_word}")

# Example 4: Joining characters with a custom delimiter
csv_string = ",".join(["apple", "banana", "cherry"])
print(f"4. CSV format joined: {csv_string}\n")


# ===============================================================================================================================
# PART 2: THE `str.format()` METHOD IN PYTHON
# ===============================================================================================================================

# DEFINITION & BEHAVIOR:
# - The `format()` method allows you to inject variables, values, or expressions into a string using placeholders denoted by curly braces `{}`.
# - It provides powerful control over layout, positioning, data types, alignment, and numerical formatting.

print("=== PART 2: `str.format()` Method Demos ===")

# 1. BASIC / POSITIONAL PLACEHOLDERS:
# Placeholders can be empty, or contain positional indexes (`0`, `1`, `2`, etc.).
template_basic = "Hello, my name is {} and I am {} years old."
result_basic = template_basic.format("Alice", 25)
print(f"1. Basic positional: {result_basic}")

# 2. INDEXED / ORDERED PLACEHOLDERS:
# You can explicitly specify the order of arguments using numerical indexes inside the braces.
template_indexed = "The {1} animal is faster than the {0} animal."
result_indexed = template_indexed.format("turtle", "cheetah")
print(f"2. Indexed order: {result_indexed}")

# 3. KEYWORD / NAMED PLACEHOLDERS:
# You can use named identifiers inside the braces and pass corresponding keyword arguments.
template_keyword = "User {name} logged in from {location}."
result_keyword = template_keyword.format(name="Bob", location="New York")
print(f"3. Keyword arguments: {result_keyword}")

# 4. ADVANCED FORMAT SPECIFIERS (Padding, Alignment, Decimals):
# - Floating-point rounding: `:.2f` rounds floats to 2 decimal places.
# - Padding/Alignment: `:<10` (left align), `:>10` (right align), `:^10` (center align).
price_text = "The item costs ${:.2f} dollars.".format(49.9)
print(f"4a. Float formatting: {price_text}")

padded_text = "|\x1b[31m{:<10}\x1b[0m|\x1b[32m{:>10}\x1b[0m|".format("left", "right")
# Simplified version for raw output readability:
padding_demo = "|{:<10}|{:>10}|{:^10}|".format("left", "right", "center")
print(f"4b. Alignment padding: {padding_demo}\n")


# ===============================================================================================================================
# PART 3: QUICK SUMMARY & CHEATSHEET
# ===============================================================================================================================

def print_summary():
    print("=== PART 3: Quick Summary Cheatsheet ===")
    print("---------------------------------------------------------------------------------------------------------")
    print("Method                  | Syntax Example                           | Description")
    print("---------------------------------------------------------------------------------------------------------")
    print("str.join()              | ' '.join(['Hello', 'World'])             | Combines iterable strings using separator.")
    print("str.format() (Basic)    | '{} and {}'.format('A', 'B')             | Inserts values sequentially into {} placeholders.")
    print("str.format() (Keyword)  | '{x} and {y}'.format(x=1, y=2)           | Inserts values using explicit keyword matching.")
    print("str.format() (Float)    | '{:.2f}'.format(3.14159)                 | Formats floats to 2 decimal places.")
    print("---------------------------------------------------------------------------------------------------------")
    print("\n[String Methods Masterclass execution completed successfully!]")

if __name__ == "__main__":
    print_summary()