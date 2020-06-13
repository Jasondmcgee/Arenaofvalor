from random import randint
def rng(parameter_low, parameter_high):
    random_number = randint(parameter_low,parameter_high)
    print(str(random_number))
    return random_number

print('Generate a random number between two values')
print('input min value')
x = input()
print('input max value')
y = input()

rng(x,y)
