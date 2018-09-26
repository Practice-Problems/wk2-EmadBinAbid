# Complete the squares function below.

import math

def squares(a, b):
    number = a
    while (math.sqrt(number) - int(math.sqrt(number)) != 0):
        number += 1
    first = number

    number = b
    while (math.sqrt(number) - int(math.sqrt(number)) != 0):
        number += 1
    second = number

    if math.sqrt(b) - int(math.sqrt(b)) == 0:
        return 2 + int(math.sqrt(second) - math.sqrt(first)) - 1
    else:
        return int(math.sqrt(second) - math.sqrt(first))

# print(squares(3, 9))