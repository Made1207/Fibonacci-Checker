import sys
print('The fibonacci sequence is a sequence of numbers in which each number is the sum of the two numbers before it.')
print('This program checks if a given number is in the fibonacci sequence.')
number = input('What number do you want to check? ')

list1 = []
fibonacci = [0, 1, 1]

for i in range(1, int(number) + 1):
    list1.append(i)

for i in range(1, int(number) - 3):
    fibonacci.append(fibonacci [i] + fibonacci [i+1])
    for i in fibonacci:
        if i == int(number):
            print(fibonacci)
            print('Yes.', number, 'is in the fibonacci sequence')
            sys.exit()
        elif i > int(number):
            print(fibonacci)
            print('No', number, 'is not in the fibonacci sequence')
            sys.exit()









