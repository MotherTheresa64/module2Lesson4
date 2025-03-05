#Engage & Apply (Mid-Lesson Exercise) -------------------------------------------------------------> Mid-Lesson Exercise
#Task: You're given a list of random tweets. Your job is to extract all hashtags using a regex pattern.

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


# Final Challenge (End of Lesson Exercise) -------------------------------------------------------------> Final Exercise
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

