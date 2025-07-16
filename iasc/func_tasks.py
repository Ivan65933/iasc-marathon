def hello_world():
    print("Hello, world!")

hello_world()

def greet(name="Гість"):
    print(f"Привіт, {name}!")

greet("Anna")
greet()


def square(n):
    return n ** 2

print(square(5))  


def add(a, b):
    return a + b

print(add(3, 4))  


def factorial(n):
    if n < 0:
        return None  
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))  


def is_even(n):
    return n % 2 == 0

print(is_even(4))  
print(is_even(7))  


def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)


def find_name(name, name_list):
    return name in name_list

print(find_name("Anna", ["Oleh", "Anna", "Ivan"]))  
print(find_name("Marta", ["Oleh", "Anna", "Ivan"]))  


def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(3, 9, 5))  


def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  


def count_vowels(s):
    vowels = "aeiouAEIOUаеєиіїоуюяАЕЄИІЇОУЮЯ"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Привіт, світе!"))  


def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(average(1, 2, 3, 4))  
print(average())           


def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_user_info(name="Ivan", age=30, city="Lviv")

def outer():
    def inner():
        print("Я - вкладена функція!")
    inner()

outer()
