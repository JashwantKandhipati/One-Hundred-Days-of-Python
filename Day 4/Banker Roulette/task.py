import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
print(random.choice(friends))

# option 2
random_friends = random.randint(0,4)
print(friends[random_friends])