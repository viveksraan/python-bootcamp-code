'''
- Always remember PascalCase for classes was introduced starting from PEP 8(the style guide) but defaultdict came in 2.5 version before this styling implemented and was a drop in replacement for dict the built-in container so although it's written in lowercase only but it's not some method but a full fledged class built upon dict class similar to Counter which is another sub class of dict
- Another useful insight python still not replaces dict with Dict, list with List so and so on because the programs already using small case would crash and would require changes to be made so developers decided to keep it as it 
'''
from collections import defaultdict

d = defaultdict(lambda: "default value")

d['correct'] = 100
print(d['correct'])
#although there's no key named 'wrong' but still we are getting default value as response becaue we are using defaultdict instead of dict 
print(d['wrong'])

# now for this defauntdict you will get default value as 24.3 as lambda is set to 24.3
d2 = defaultdict(lambda: 24.3)
# And since we haven't defined any key value pair so whatever key you would try to access you will get the same response 24.3 the default value basically
print(d2['key1'])
print(d2['key2'])
print(d2['wrong'])




