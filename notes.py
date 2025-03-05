# Regular Expressions (Regex) in Python

# Regex is used for matching patterns in text. It's powerful for text processing and data extraction.
# Use cases include:
# - Validation (e.g., emails, phone numbers)
# - Data extraction (e.g., extracting hashtags, phone numbers)
# - Text replacement (e.g., anonymizing data)
# - String splitting (e.g., breaking text into parts)
# - Searching for patterns (e.g., finding specific text)

# Key Concepts in Regex:
# 1. **Literal Characters**: Characters that match exactly, like "a" matching 'a' in a string.
# 2. **Metacharacters**: Special characters with unique meanings in regex patterns.
#   - `.`: Matches any character except a newline.
#   - `^`: Matches the start of a string.
#   - `$`: Matches the end of a string.
#   - `[]`: Matches any one of the characters inside the brackets.
# 3. **Special Sequences**:
#   - `\d`: Matches any digit (0-9).
#   - `\w`: Matches any word character (letters, digits, underscores).
#   - `\s`: Matches any whitespace character (spaces, tabs, newlines).

# Python `re` module: Import this to work with regex in Python.
import re

# Common Regex Functions:

# 1. **re.findall()**: Finds all matches of a pattern in a string. Returns a list of all occurrences.
text = "Hi my name is Travis, and I like to go and do things and stuff"
ands = re.findall(r"and", text)  # Find all occurrences of "and"
print(ands)  # Output: ['and', 'and', 'and']
print(len(ands))  # Output: 3

# Example: Extracting hashtags
post = "I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Code"
tags = re.findall(r"#\w+", post)
print(tags)  # Output: ['#Python_is_lyfe', '#Regex', '#Code']

# Exercise: Extract hashtags from a list of tweets
tweets = [
    "Loving the #sunset! So peaceful #nature #blessed",
    "Had a great day! #happy #friends #goodvibes",
    "Can't wait for the #weekend! #fun #relax"
]
# Use re.findall() to extract hashtags from tweets
hashtags = [re.findall(r"#\w+", tweet) for tweet in tweets]
print(hashtags)

# 2. **re.search()**: Finds the first match of a pattern in a string. Returns a match object or None.
# Example: Validating an email address
email = "kareem33-34-28@gmail.com"
found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
if found:
    print(f"{found.group()} is a valid email!")  # Output: kareem33-34-28@gmail.com is valid

# 3. **re.match()**: Checks if a string starts with a pattern.
url = "https://example.com"
secure = re.match(r"https", url)
if secure:
    print("This link goes to a secure website!")  # Output: This link goes to a secure website!

# 4. **re.split()**: Splits a string into a list based on a regex pattern (delimiters).
text = 'Python,Regex;Splitting-Example. Fun, right?'
words = re.split(r"[,.;\s-]+", text)
print(words)  # Output: ['Python', 'Regex', 'Splitting', 'Example', 'Fun', 'right', '']

# 5. **re.sub()**: Substitutes all occurrences of a pattern with a replacement string.
number = "(770) 888-1180"
formatted_number = re.sub(r"\D", '', number)  # Remove non-digits
print(formatted_number)  # Output: 7708881180

# Example: Anonymizing usernames in chat messages
chat = '''
@Yve-bee123 : "I think I love Regex"
@Travis : "Aren't you married?"
@Yve_bee123 : "It's just not the same"
@Travis : "They better not see this!"
'''
anon_chat = re.sub(r"@[\w-]+", '@user-anon', chat)
print(anon_chat)
# Output:
# @user-anon : "I think I love Regex"
# @user-anon : "Aren't you married?"
# @user-anon : "It's just not the same"
# @user-anon : "They better not see this!"

# 6. **Grouping**: Capturing specific parts of a match using parentheses.
# Example: Capturing parts of a phone number
text = "123-456"
pattern = r"(\d+)-(\d+)"
thematch = re.search(pattern, text)
if thematch:
    print(f"Group 1: {thematch.group(1)}")  # Output: 123
    print(f"Group 2: {thematch.group(2)}")  # Output: 456

# Final Challenge (Email Validation): Create a script to validate emails from a list.
emails = [
    "correct.email@example.com",
    "incorrect-email-at-example.com",
    "another.correct.email@example.org"
]
for email in emails:
    if re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email):  # Use regex to check validity
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")