'''
SPECIAL CHARACTERS
We can use some special characters in reg ex to allow some categories of characters in our expression at a particular place
->  Character    Description            Example pattern code        Example match
->  \d             a digit                   file_\d\d                  file_25
->  \w            alphanumeric               \w-\w\w\w                  A-b_1
                  (digits, alphabets
                   and _ )
->  \s           White space                  a\sb\sc                   a b c
->  \D           non digit                      \D\D\D                   ABC
->  \W            non-alphanumeric           \W\W\W\W\W                 *-+=)
->  \s          Non-whitespace                \S\S\S\S\S                  Yoyo2           
'''               
import re

text = 'My phone number is 408-555-1234'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone.group())

'''
QUANTIFIERS
Character   Description                     Example Pattern Code         Example Match
    +       Occurs one or more time         Version \w-\w+              Vesrion A-b1_1
    {n}     Occurs exactly n times              \D{3}                         abc
    {n, m}  Occurs n to m times                 \d{2,4}                       123
    {n, }   Occurs n or more times              \w{4, }                 anycharacters
    {0, m}  Occurs m or less times             \w{0, 4}                      ab
      *     Occurs zero or more times           ABC*                         ABC
      ?     Once or none                        plurals?                    plural
'''

'''
-> re.compile() creates a compiled regular expression object.
-> The pattern is parsed and stored once.
-> You can reuse it efficiently many times without recompiling.
'''
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
phone2 = re.search(phone_pattern, text)
print(phone2.group())

'''
- Now there could be a case that you need area code(first three digit of the phone no.) separately from the rest of the code for these kind of situations you could use groups
- Particularly when the information you are extracting has various components which have their individual identity as well
'''
address_code = re.search(phone_pattern, text)

print(address_code.group()) # This will display the whole code
print(address_code.group(1)) # This will display the address code only(408)
print(address_code.group(2)) # This will display only (555)
print(address_code.group(3)) # This will display the address code only(1234)

