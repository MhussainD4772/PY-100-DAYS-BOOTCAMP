friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random

random_integer =  random.randint(1,5)

if random_integer == 1:
    print("Alice")
elif random_integer == 2:
    print("Bob")
elif random_integer == 3:
    print("Charlie")
elif random_integer == 4:
    print("David")
else:
    print("Emanuel")

# print(random.choice(friends))
