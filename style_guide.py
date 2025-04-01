
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four) 

# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
     
# Wrong:
# operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)     

1. Naming Conventions
------------------------
# Use descriptive variable names in snake_case
correct_variable = 10  # Correct
IncorrectVariable = 20  # Wrong (Should be snake_case)

# Class names should be in PascalCase
class MyClass:  # Correct
    pass

class my_class:  # Wrong
    pass

# Constants should be in UPPERCASE
MAX_SIZE = 100  # Correct
maxSize = 100   # Wrong

2. Indentation
------------------------
# Use 4 spaces per indentation level
def my_function():
    print("Hello")  # Correct

def bad_function():
  print("Hello")  # Wrong (Uses 2 spaces instead of 4)

3. Line Length
------------------------
# Keep lines under 79 characters
message = "This is a very long message that exceeds 79 characters, which is not recommended."  # Wrong
message = (
    "This is a better way to split long lines so they remain readable."
)  # Correct

5. Whitespace
------------------------
# Use spaces around operators and after commas
x = 5 + 10  # Correct
x=5+10  # Wrong
 