""" Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве. """

from typing import List


def binarySearch(arr: List[int], number: int) -> int:
  
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]

    print(f"Массив: {arr}")
    number = int(input("Элемент поиска: "))
    result = binarySearch(arr, number)

    if result == -1:
        print("-1")
    else:
        print(f"Индекс: {result}")


if __name__ == "__main__":
    main()