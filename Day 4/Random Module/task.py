import random
#
# random_integer = random.randint(1,10)
# print(random_integer)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

# Generate a random intefer : 1 for Heads, 2 for Tails
random_integer =  random.randint(1,2)

#Map it to Heads and Tails
if random_integer == 1:
    print("Heads")
else:
    print("Tails")