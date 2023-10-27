import re
firstName = first_multiple_input[0]
valid = 
emailID = first_multiple_input[1]
pattern = r'@gmail.com$'
if re.search(pattern, emailID):
    valid.append(firstName)
    if valid:
        for name in list(valid.sort()):
            print(name)