# 1:

# def is_prime(n, i=2):
#     if n <= 2:
#         return True if n == 2 else False
#     if n % i == 0:
#         return False
#     if i * i > n:
#         return True
#     return is_prime(n, i + 1)

# def pr(n, current=0):
#     if current > n:
#         return
#     if is_prime(current):
#         print(current)
#     pr(n, current + 1)

# n = int(input("Son kiriting: "))
# pr(n)

# 2:

# import math

# numbers = [1.2, 2.3, 3.5, 4.1]
# rounded_numbers = list(map(math.ceil, numbers))
# print(rounded_numbers)


# 3:


# numbers = [1.2, 2.3, 3.5, 4.1]
# integer_parts = list(map(int, numbers))
# print(integer_parts)

# 4:

# numbers = [1, -2, 3, -4, 5]
# transformed_numbers = list(map(lambda x: -x if x > 0 else x * 2, numbers))
# print(transformed_numbers)


# 5:

# N = int(input("N sonini kiriting: "))
# numbers = [1, 2, 8, 27, 64, 125]
# filtered_numbers = list(filter(lambda x: x > N ** 3, numbers))
# print(filtered_numbers)


# 6:

# numbers = [1.2, 2, 3.5, 4, 5.1]
# integer_numbers = list(filter(lambda x: isinstance(x, int), numbers))
# print(integer_numbers)

# 7:

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime_numbers = list(filter(is_prime, numbers))
# print(prime_numbers)


# 8:

# elements = [1, 'hello', 2.5, 'world', True, 'python']
# strings = list(filter(lambda x: isinstance(x, str), elements))
# print(strings)


# 9:

# numbers = [-1, 2, -3, 4, -5, 6]
# positive_numbers = list(filter(lambda x: x > 0, numbers))
# print(positive_numbers)

# 10:

# numbers = [1, 2.5, 3, 4.8]
# converted_numbers = list(map(lambda x: float(x) if isinstance(x, int) else int(x), numbers))
# print(converted_numbers)

# 11:

# binary_values = [1, 0, 1, 0, 1]
# boolean_values = list(map(lambda x: True if x == 1 else False, binary_values))
# print(boolean_values)
