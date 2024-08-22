lower = int(input('enter lower range number: '))
upper = int(input('enter upper range number: '))

for num in range (lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % 2 == 0:
                break
        else:
          print(num)