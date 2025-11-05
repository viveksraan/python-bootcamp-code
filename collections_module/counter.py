'''
    - Collection modules are buit-in in python to implement specialised containers that are great alternative to python's built in containers(such as list, tuple, sets , dictionaries)
    - If let's say you have a list of any type of objects and you want to get the frequency of every unique value in the list you can use Counter class of collections module instead of doing it hard way by writing the loop and keeping the track using dictionary 
    - We are discussing example for list but in exact same way it works with strings and tuples as well
    - You can use methods like pop, popitem, setdefault, get, fromkeys with Counter objects according to the requirement, mostly all the methods available for a dictionary but some additional methods also such as most_common(to get key items sorted according to the most common to least common) 
'''
from collections import Counter 
mylist1 = [1,1,1,1,2,2,2,3,3,3,3,3,1,2]
mylist2 = [1,1, "car", "car", 4.5, 6.7, 4.5, "bike"]
count1 = Counter(mylist1)
# The result you get from Counter class is a dictionary type of object like this Counter({1: 2, 'car': 2, 4.5: 2, 6.7: 1, 'bike': 1}), always remember counters are a dictionary subclass only so that's why we get a dictionary object in return from the Counter class
count2 = Counter(mylist2)
print(count1)
print(count2)