# Lesson 4: Python Regex - Engage & Apply + Final Challenge

# ===========================
# engage and apply ---------> Exercise 1 pre-provided
# ===========================

# Task: You're given a list of random tweets. Your job is to extract all hashtags using a regex pattern.

# Sample tweets
tweets = [
    "Loving the #sunset! So peaceful #nature #blessed",
    "Had a great day! #happy #friends #goodvibes",
    "Can't wait for the #weekend! #fun #relax"
]

# Solution:
# Importing the 're' module for regex matching
import re

# Extract hashtags using regex
hashtags = []
for tweet in tweets:
    hashtags.extend(re.findall(r'#\w+', tweet))

# Print the extracted hashtags
print(hashtags)

# Expected Output:
# ['#sunset', '#nature', '#blessed', '#happy', '#friends', '#goodvibes', '#weekend', '#fun', '#relax']

# ===========================
# engage and apply ---------> Exercise 1 My Version Created
# ===========================

# Task: Extract all hashtags from a list of tweets using a regex pattern. 

# Sample tweets
tweets = [
    "Exploring the #mountains today! #adventure #explore #outdoors",
    "Had the best time at the #beach! #sun #fun #vacation",
    "Coffee and #coding! #developer #workfromhome #productivity"
]

# Solution:
# Importing the 're' module for regex matching
import re

# Extract hashtags using regex
hashtags = []
for tweet in tweets:
    hashtags.extend(re.findall(r'#\w+', tweet))

# Print the extracted hashtags
print("Extracted Hashtags:", hashtags)

# Expected Output:
# ['#mountains', '#adventure', '#explore', '#outdoors', '#beach', '#sun', '#fun', '#vacation', '#coding', '#developer', '#workfromhome', '#productivity']

# ===========================
# final challenge ---------> pre-provided
# ===========================

# Task: You are tasked with creating a simple email validation script 
# that accepts a list of emails and checks if they are valid based on a regex pattern.

# Sample emails
emails = [
    "correct.email@example.com",
    "incorrect-email-at-example.com",
    "another.correct.email@example.org"
]

# Solution:
# Importing the 're' module for regex matching
import re

# Define the regex pattern for a valid email
email_pattern = r'[\w.-]+@[\w-]+\.[a-z]{2,3}'

# Check each email and validate using regex
for email in emails:
    if re.search(email_pattern, email):  # Use re.search to check for matches
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")

# Expected Output:
# correct.email@example.com is valid
# incorrect-email-at-example.com is invalid
# another.correct.email@example.org is valid

# ===========================
# final challenge ---------> My Version Created
# ===========================

# Task: Write a script to validate a list of email addresses based on a regex pattern.

# Sample emails
emails = [
    "hello.world@example.com",
    "invalid-email@domain",
    "user.name@company.org",
    "missing-at-symbol.com"
]

# Solution:
# Importing the 're' module for regex matching
import re

# Define the regex pattern for a valid email
email_pattern = r'[\w.-]+@[\w-]+\.[a-z]{2,3}'

# Check each email and validate using regex
for email in emails:
    if re.search(email_pattern, email):  # Use re.search to check for matches
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")

# Expected Output:
# hello.world@example.com is valid
# invalid-email@domain is invalid
# user.name@company.org is valid
# missing-at-symbol.com is invalid
