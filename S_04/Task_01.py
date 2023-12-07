from functools import reduce
import math


def PearsonСorrelation(array1, array2):
    if len(array1) != len(array2) or len(array1) == 0 or len(array2) == 0:
        return None

    sredneeX = sum(array1) / len(array1)
    sredneeY = sum(array2) / len(array2)

    numerator = reduce(
        lambda x, y: x + y,
        map(lambda x: (x[0] - sredneeX) * (x[1] - sredneeY),
            zip(array1, array2)))

    sumX = reduce(lambda x, y: x + y,
                   map(lambda x: (x - sredneeX)**2, array1))
    sumY = reduce(lambda x, y: x + y,
                   map(lambda y: (y - sredneeY)**2, array2))

    denominator = math.sqrt(sumX * sumY)
    if denominator == 0:
        return None
    return numerator / denominator


print(PearsonСorrelation([1, 2, 3], [4, 5, 6]))