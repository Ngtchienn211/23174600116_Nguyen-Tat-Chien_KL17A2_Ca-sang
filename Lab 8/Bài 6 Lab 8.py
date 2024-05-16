def filter_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))

def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

def cube_numbers(numbers):
    return list(map(lambda x: x ** 3, numbers))

def cube_even_numbers(numbers):
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    return list(map(lambda x: x ** 3, even_numbers))

def square_odd_numbers(numbers):
    odd_numbers = filter(lambda x: x % 2 != 0, numbers)
    return list(map(lambda x: x ** 2, odd_numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("Danh sách ban đầu là: ", numbers)
print("Các số lẻ trong danh sách:", filter_odd_numbers(numbers))
print("Các số chẵn trong danh sách:", filter_even_numbers(numbers))
print("Danh sách các lập phương của các phần tử:", cube_numbers(numbers))
print("Danh sách lập phương của các số chẵn:", cube_even_numbers(numbers))
print("Danh sách bình phương của các số lẻ:", square_odd_numbers(numbers))
