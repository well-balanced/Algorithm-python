def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def buble_sort(numbers):
    print(numbers)
    for labs in reversed(range(len(numbers))):
        for i in range(labs):
            if numbers[i] > numbers[i+1]:
                swap(numbers, i, i+1)
    return numbers

numbers = [3, 7, 4, 5, 2, 6, 1]
numbers = buble_sort(numbers)
