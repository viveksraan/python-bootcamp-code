'''
We will be using decorators which works as an on/off switch for the addon functionality which we adding over the basic functionality of the decorator function. We will be using passing functions as argument and returning functions for the decorators
'''

def new_decorator(original_fun):
    
    def wrap_func():
        '''Wrap function represents the extra functionality which you want to addon upon the basic functionality. Think of it like we are giving the base/original function to some decorator, than this decorator creates a wrap up function in which it wraps some additional functionality before as well as after the original function depending upon the requirement and returns the wrapped up function. Now what we can do is if we want to use the function with original as well as extra functionality then we can call this wrapped function returned by decorator otherwise if we only want to use basic functionality then we can use the original function '''
        print('Some extra code, before the original function')
        original_fun()
        print('Some extra code, after the original function')
    return wrap_func

# def original_func():
#     '''This is the base func'''
#     print("I want to be decorated!!")

# This is the basic way of using decorator
# decorated_func = new_decorator(original_func)
# decorated_func()

# Or else can use @ operator as well which is a better and more used approach, and now whenever you want to use decorator call the original_func it will automatically be applied and if you don't want simply turn off the deocrator by commenting @new_decorator(or whatever your decorator's name is)
@new_decorator
def original_func():
    '''This is the base func'''
    print("I want to be decorated!!")

'''now when you will be using your original_func function even normally if will use the wrap_up functionality inside the decorator function''' 
original_func()