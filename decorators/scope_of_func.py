'''def hello(name="Jose"):
    print('The hello() function has been executed!')
    def greet():
        return '\t This is the greet() func inside hello!'
    def welcome():
        return '\t This is welcome() inside hello'
    print(greet())
    print(welcome())
    print('This is the end of the hello function')

hello()'''

# Since the scope of welcome is limited inside the hello function so you will get following error for trying this
# "welcome" is not defined
# But we can use welcome and greet functions like this if we pass the reference to these functions from hello function
# welcome()

# Let's try it other way
def hello(name="Jose"):
    print('The hello() function has been executed!')
    def greet():
        return '\t This is the greet() func inside hello!'
    def welcome():
        return '\t This is welcome() inside hello'
    print("I am going to return a function!!")
    if name == 'Jose':
        return greet
    else:
        return welcome
        
# now depending on we pass an argument to the hello function or not the function will return one the greet and welcome and we would be able to use it even outside the hello also but not the other one
greet = hello()
welcome = hello("Sam")
print(greet())
print(welcome())