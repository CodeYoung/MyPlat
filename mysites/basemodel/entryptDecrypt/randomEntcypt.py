from Crypto.Random import random

print('random.randint: ', random.randint(10, 20))
print('random.randrange: ', random.randrange(10, 20, 2))
print('random.randint: ', random.getrandbits(3))
print('random.choice: ', random.choice([1, 2, 3, 4, 5]))
print('random.sample: ', random.sample([1, 2, 3, 4, 5], 3))
list = [1, 2, 3, 4, 5]
random.shuffle(list)
print('random.shuffle: ', list)