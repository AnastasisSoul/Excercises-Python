x = int(input('Enter a number >=  10: '))
while (x > 9):
    x = 3*x + 1
    sum = 0
    while (x != 0):
        sum = sum + x%10
        x = x//10
    x = sum
    print(x)
