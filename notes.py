# Lesson 4: Python Regular Expressions (Regex) - Summary Notes

# Brief Overview:
# This lesson introduces Regular Expressions (Regex) in Python, which is a powerful tool 
# for pattern matching in strings. You'll learn how to search for patterns, extract 
# data, and replace content within strings using Regex.

# Key Concepts Covered:

# 1. Metacharacters:
# - Dot (.) - Matches any character except newline.
# - Caret (^) - Anchors the pattern to the start of the string.
# - Dollar ($) - Anchors the pattern to the end of the string.
# - Asterisk (*) - Matches zero or more of the preceding element.
# - Plus (+) - Matches one or more of the preceding element.
# - Question Mark (?) - Matches zero or one of the preceding element.
# - Square Brackets ([]) - Defines a character set.
# - Pipe (|) - Acts as an OR operator.
# - Parentheses (()) - Used for grouping.
# - Backslash (\) - Escapes special characters or specifies special sequences.

# Example of matching patterns:
import re

# 2. Special Sequences:
# - \d - Matches any digit (0-9).
# - \w - Matches any alphanumeric character and underscore.
# - \s - Matches any whitespace character.
# - \b - Matches a word boundary.

# Example code for using Regex to match digits in a string:
pattern = r"\d+"  # Matches one or more digits
text = "There are 123 apples and 45 bananas."
result = re.findall(pattern, text)
print(result)  # Output: ['123', '45']

# 3. Using Anchors to match the start and end of the string:
pattern_start = r"^Hello"  # Matches "Hello" at the start
pattern_end = r"world!$"  # Matches "world!" at the end

text = "Hello, world!"
start_match = re.search(pattern_start, text)
end_match = re.search(pattern_end, text)

if start_match:
    print("Found at the start")
if end_match:
    print("Found at the end")

# 4. Using Groups and Parentheses for capturing:
# You can use parentheses to capture parts of a match:
pattern = r"(\w+) (\w+)"
text = "John Doe"
match = re.search(pattern, text)
if match:
    first_name = match.group(1)
    last_name = match.group(2)
    print(f"First Name: {first_name}, Last Name: {last_name}")

# Example output:
# First Name: John, Last Name: Doe

# 5. Modifying Strings Using Regex:
# Regex can be used to substitute parts of strings:
pattern_replace = r"(\d{3})-(\d{2})-(\d{4})"
replacement = r"XXX-XX-\3"  # Replace with masked SSN
text = "My SSN is 123-45-6789"
modified_text = re.sub(pattern_replace, replacement, text)
print(modified_text)  # Output: "My SSN is XXX-XX-6789"