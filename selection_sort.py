# def swap(x, i, j):
#     x[i], x[j] = x[j], x[i]

# def selection_sort(numbers):
#     print(numbers)
#     for laps in reversed(range(len(numbers))):
#         max_i = 0
#         for i in range(1, 1+laps):
#             if numbers[i] > numbers[max_i]:
#                 max_i = i
#             swap(numbers, max_i, laps)
#     print(numbers)

# numbers = [3, 7, 4, 5, 2, 6, 1]

# selection_sort(numbers)

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def selection_sort(numbers):
    for laps in reversed(range(len(numbers))):
        max_i = 0
        for i in range(1, 1+laps):
            if numbers[i] > numbers[max_i]:
                max_i = i
        swap(numbers, i, max_i)
