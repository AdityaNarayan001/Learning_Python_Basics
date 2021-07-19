import random

for i in range(3):
    print(random.random())


for z in range(4):
    print(random.randint(10, 20))


members = ['John', 'Mosh', 'Sarah', 'Mary']
leader = random.choice(members)
print(leader)