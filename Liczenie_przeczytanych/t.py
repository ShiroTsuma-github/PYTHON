import re

text = "11.12.13.14.1556."
match = re.search(r"\d+(?=[^.\d]*[.]?$)", text)
if match:
    last_number = match.group()
    print(last_number)  # Output: 15
else:
    print("No match found")