import random

random_int_btw_1to100 = random.randint(0, 100)
# this random int will change every time you run the code because it's using some arbitrary seed
print(random_int_btw_1to100)
'''
- If you want to test a fixed batch of random number then you could seed, it allows us to start from a seeded random numbers 
 - Every time the code is executed the random number is computer on the fixed seedling given by you so it doesn't comes different in multiple executions
 - But never assume that after setting the seed you would call your randint as many times as you want and you will get the same exact value in every different call because seed sets a series of batches for the random number not a fixed number. for ex(74, 24, 69) now in every call to the method you are getting different value but the point as many times you run the same code you will get (74, 24, 69) the exact same batch
 '''
random.seed(101)
print(random.randint(0, 100) )  # 74
print(random.randint(0, 100) )  # 24
print(random.randint(0, 100) )  # 69

random.seed(101)
print(random.randint(0, 100) )  # 74
print(random.randint(0, 100) )  # 24
print(random.randint(0, 100) )  # 69

random.seed(10)
print(random.randint(0, 100) )  # 73
print(random.randint(0, 100) )  # 4
print(random.randint(0, 100) )  # 54

mylist = [1, 2, 3, 4, 5, 6]
# could be used to choose an item randomly from your own list
print(random.choice(mylist))

# could be used to choose multiple items randomly from the list
# SAMPLE WITH REPLACEMENT 
random.choices(population=mylist, k=10)
# SAMPLE WITHOUT REPLACEMENT 
random.sample(population=mylist, k=10)

# shuffling the list
random.shuffle(mylist)

# if you want to choose random float value between a range 
random.uniform(a=0, b=1)

# gauss method takes mean(mu) and standard deviation(sigma) and returns random floating-point sampled from a Gaussian (normal) distribution
random.gauss(mu=0, sigma=1)