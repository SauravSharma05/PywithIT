# string compare
main_string = "GfG is a good website"

substrings = ["GfG", "site", "CS", "Geeks", "Tutorial"]

matching_substrings = [sub for sub in substrings if sub in main_string]

print("Matching substrings:", matching_substrings)



# Initialize the string
main_string = "GfG is a good website"
substrings = ["GfG", "site", "CS", "Geeks", "Tutorial"]
matching_substrings = list(filter(lambda x: x in main_string, substrings))
print("Matching substrings:", matching_substrings)

# find method
main_string = "GfG is a good website"
substrings = ["GfG", "site", "CS", "Geeks", "Tutorial"]
matching_substrings = []
for sub in substrings:
    if main_string.find(sub) != -1:
        matching_substrings.append(sub)

print("Matching substrings:", matching_substrings) 



# re expression : regular expression

import re

main_string = "GfG is a good website"
substrings = ["GfG", "site", "CS", "Geeks", "Tutorial"]
matching_substrings = [sub for sub in substrings if re.search(re.escape(sub), main_string)]

print("Matching substrings:", matching_substrings)

# string functions 
text = "Hello, World"

first_character = text[0]  # 'H'
last_character = text[-1]   # '!'
length_of_text = len(text)  # 13

substring = text[7:12]  # 'World'

print(first_character, last_character, length_of_text, substring)