# module2Lesson4

## Python Regex Exercises

This project contains exercises that demonstrate the use of Regular Expressions (regex) in Python. The main focus is on text extraction, pattern matching, and validation using the built-in `re` module. The two exercises provided showcase the power of regex for practical tasks.

## Exercises Overview

1. **Mid-Lesson Exercise: Extract Hashtags from Tweets**
   - **Task:** Given a list of tweets, the goal is to extract all hashtags using a regex pattern.
   - **Solution:** The script iterates through each tweet and uses the `re.findall()` function to find all words that start with a hashtag (`#`).

2. **Final Exercise: Email Validation Script**
   - **Task:** Create a simple script to validate email addresses. The script accepts a list of emails and checks whether they are valid according to a regex pattern.
   - **Solution:** The script uses a regex pattern that checks the structure of an email address and prints whether each email is valid or invalid.

## Code

### 1. Mid-Lesson Exercise: Extract Hashtags from Tweets

```python
# Sample tweets
tweets = [
    "Loving the #sunset! So peaceful #nature #blessed",
    "Had a great day! #happy #friends #goodvibes",
    "Can't wait for the #weekend! #fun #relax"
]

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
