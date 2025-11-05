import re

text = "The agent's phone number is 408-555-1234. Call soon!"
# Checking a substring with using reg ex will return true or false
print('phone' in text)


pattern = "phone"

# But using search of re module will give you so much more info
# True
# <re.Match object; span=(12, 17), match='phone'>
print(re.search(pattern, text))

match = re.search(pattern, text)

print(match.span())
# (12, 17)
print(match.start())
# 12
print(match.end())
# 17

repeat_text = "hey borther, hey how, how hey hey"
# if you want to find multiple matches instead of getting the first occurence only use finditer or matches instead it will return a list of match type objects
matches = re.findall("hey", repeat_text)
for it in matches:
    print(it)
    # hey

# But always keep in mind that findall only returns the value so you could use it nothing more than to know how many times match in the text. If you want to get objects the way search returns then we could use finditer
matches = re.finditer("hey", repeat_text)
for it in matches:
    print(it)
    print(it.start())
    print(it.end())
    print(it.span())
    print(it.group())

