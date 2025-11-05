import re

# You can use the pipe symbol for logical or operator in reg ex
search_result = re.search(r'cat|dog|pet', 'The dog is here')
print(search_result.group())

# wildcard operators(.) it will match any one character if you want to keep your reg ex more relax use it other wise use character identifiers which we discussed earlier
print(re.findall(r'...at', 'The cat in the hat went splat.'))   # wil display ['e cat', 'e hat', 'splat']

# starts with 
# print("first")
# we ger result as 2 because we are using starts with symbol and the string starts with a digit calld 2 if the first char won't be a digit we wouldn't get a character back
print( re.search(r'^\d', '2 is a factor of 4 as well as 8').group())  # 2          
# same here we are again using start with so we are getting the starting char which is a digin the only value in our resultant list
print(re.findall(r'^\d', '2 is a factor of 4 as well as 8')) # ['2']            

# ends with uses $ sign and it indicate that just after whatever we wrote before it the string ends so here we will get the char 8 in our list because it's a digit just before string ends
print(re.findall(r'\d$', '2 is a factor of 4 as well as 8')) # ['8']            

# matching a single char from set of characters [], whatever characters we will use inside these brackets one of them will be matched with the string
# And remember inside the set ^ indicates negation of whatever written character are their inside the square brackers for ex r'[^.,/] means anything which is not a .,or/ ', it's often used to get rid of punctuations
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
list_of_words = re.findall(r'[^!.,? ]+', test_phrase)
print(list_of_words)
# we can join all the elements of an iterable with a string between every two elements of the iterable by calling join on a string and passing the iterable. But always remember you can never call it on iterable you want to join always call  it on string you want to use as a connector
print(' '.join(list_of_words))
# + means one or more occurences 
pattern = r'[^\d]+'
# * means zero or more occurences 

text = "a lot of bul-ish text where theres no sen-se of what they are dis-playing"
pattern = r'[\w]+'
print(re.findall(text, pattern))