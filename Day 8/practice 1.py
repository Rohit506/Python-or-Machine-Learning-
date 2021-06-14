# random function : to generate random number
import random
print(random.randint(0,100))
print(random.randrange(0,101,5))

mylist = list(range(100))
(random.shuffle(mylist))
print(mylist)

print("choice :", random.choice(mylist))
print("choice :", random.choices(mylist, k=10))