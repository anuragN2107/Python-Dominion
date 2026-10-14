# ===============================================================================================================================
#                                    CHAPTER 13 PRACTICE SET (VENV & ADVANCED STRINGS)
# ===============================================================================================================================

# ===============================================================================================================================
# PROBLEM 1: Replicating a Virtual Environment
# ===============================================================================================================================
# Question: Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

# NOTES & CONCEPTS:
# - Step 1: Create and activate your first virtual environment:
#     python -m venv venv1
#     venv1\Scripts\activate.bat  (or source venv1/bin/activate on Mac/Linux)
# - Step 2: Install your desired packages in the first environment:
#     pip install requests flask
# - Step 3: Freeze the installed dependencies into a requirements file:
#     pip freeze > requirements.txt
# - Step 4: Create your second virtual environment and activate it:
#     python -m venv venv2
#     venv2\Scripts\activate.bat  (or source venv2/bin/activate on Mac/Linux)
# - Step 5: Install the exact same packages into the second environment using the requirements file:
#     pip install -r requirements.txt

print("=== PROBLEM 1: Virtual Environment Replication Strategy ===")
print("1. Freeze dependencies from env 1: `pip freeze > requirements.txt`")
print("2. Activate env 2 and run: `pip install -r requirements.txt`\n")


# ===============================================================================================================================
# PROBLEM 2: String Formatting Student Details
# ===============================================================================================================================
# Question: Write a program to input name, marks and phone number of a student and format it using the format function like below:
# "The name of the student is Harry, his marks are 72 and phone number is 99999888"

print("=== PROBLEM 2: Student Details Format ===")

# Simulated inputs (or use input() for interactive terminal use)
name = "Harry"
marks = 72
phone = "99999888"

# Using str.format() with placeholders
output_template = "The name of the student is {}, his marks are {} and phone number is {}"
formatted_student = output_template.format(name, marks, phone)

print(formatted_student)
print()


# ===============================================================================================================================
# PROBLEM 3: Vertical String Conversion of Multiplication Table
# ===============================================================================================================================
# Question: A list contains the multiplication table of 7. Write a program to convert it to a vertical string of same numbers.

print("=== PROBLEM 3: Vertical String Multiplication Table ===")

# List containing the multiplication table of 7
table_of_seven = [7 * i for i in range(1, 11)]
print(f"Original list: {table_of_seven}")

# Convert each integer in the list to a string, then join them using a newline character (`\n`)
vertical_string = "\n".join(map(str, table_of_seven))

print("Vertical string output:")
print(vertical_string)
print()

