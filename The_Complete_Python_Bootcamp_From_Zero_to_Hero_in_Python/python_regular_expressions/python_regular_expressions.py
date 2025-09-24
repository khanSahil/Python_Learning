# Regular expressions helps us to search for
# general pattern in text data.
# The re (regular expressions) library allows us to create specialized
# pattern strings and then search for matches with text
#
# The primary skill set for regex is understanding the 
# special syntax for these pattern strings
# Don't need to memorize these special patterns, instead
# focus on understanding how to look up the information.
# example:
# (555)-555-5555
# regex => r"(\d\d\d)-\d\d\d-\d\d\d\d"
# \d are individual identifiers, basically a placeholders,
# just like a wildcard. here \d means digit.
# regex => r"(\d{3})-\d{3}-\d{4}"

# ==========================
# REGULAR EXPRESSION PART 1
# ==========================

print("dog" in "my dog is great") # simple example without re library

text = "The agent's phone number is 123-456-7890 phone. Call soon!"
print("phone" in text)

import re
pattern = 'phone'
print(re.search(pattern, text))
pattern = "NOT IN TEXT"
print(re.search(pattern, text))
pattern = "phone"
match = re.search(pattern, text)
print(match.span())
print(match.end())
print(match.start())
matches = re.findall(pattern, text)
print(matches)

for match in re.finditer('phone', text):
    print(match)
    print(match.span())
    print(match.group())
    
# ==========================    
# REGULAR EXPRESSION PART 2
# ==========================

# Character Identifiers Table:

# \d digit                  file_\d\d       file_25
# \w alphanumeric           \w-\w\w\w       A-b_1
# \s white spaces           a\sb\sc         a b c
# \D A non-digit            \D\D\D          ABC
# \W Non-Alphanumeric       \W\W\W\W\W      *-+=)
# \S Non-whitespaces        \S\S\S\S        Yoyo

text = "The agent's phone number is 123-456-7890 phone. Call soon!"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone.group())


# Quantifiers Table:
# +     Occurs one or more time
# {3}   Occurs exactly 3 times
# {2,4} Occurs 2 to 4 times
# {3,}  Occurs 3 or more times
# *     Occurs 0 or more times
# ?     One or none

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone.group())

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print(re.search(phone_pattern, text).group(1))
print(re.search(phone_pattern, text).group(3))


# ==========================    
# REGULAR EXPRESSION PART 3
# ==========================

# Additional Regex Syntax

print(re.search(r'cat|dog', 'the dog is found'))
print(re.search(r'cat|dog', 'the cat is found'))

print(re.findall(r'.at', 'The cat in th hat sat there')) # . is wildcard
print(re.findall(r'...at', 'The cat in th hat went splat')) # . is wildcard


print(re.findall(r'^\d', '1 is a number')) # ^ startswith
print(re.findall(r'^\d', 'then 1 is a number'))

print(re.findall(r'\d$', '1 is a number')) # $ endswith
print(re.findall(r'\d$', 'then number is 2'))

phrase = "there are 3 numbers 24, inside 5 this sentence"
pattern = r'[^\d]+'
print(re.findall(pattern, phrase))

test_phrase = "This is a string !. but it has punctuation mark, how can we remove it?"
print(re.findall(r'[^!.?]+', test_phrase))

text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'
print(re.findall(pattern, text))