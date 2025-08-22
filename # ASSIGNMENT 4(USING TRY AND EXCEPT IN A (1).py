# ASSIGNMENT 4(USING TRY AND EXCEPT IN ASSSIGNMENT 1 AND 2)
# Task 1
ama = 344
kwame = 56.78
john = 'affum'
baidoo = True
print(ama, type(ama))
print(kwame, type(kwame))
print(john, type(john))
print(baidoo, type(baidoo))

# Task 2
s = int(19.99)
t = str(50)
u = float('50')
print(s,type(s))
print(t,type(t))
print(u,type(u))

# Task 3
first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
print('Hello '+first_name, last_name+'!')

# Task 4
age = 20

# Fixed version (convert int to str before concatenation)
print("You are " + str(age) + " years old.")

# Task 5
word = input("Enter your favourite word: ")
count = int(input("How many times to repeat it? "))

# Repeat with spaces
print((word + " ") * count)
# Task 6
try:
    eval('print("Hello')   # SyntaxError
except SyntaxError:
    print("Caught a SyntaxError")

try:
    int("abc")            # ValueError
except ValueError:
    print("Caught a ValueError")

try:
    result = "age" + 10   # TypeError
except TypeError:
    print("Caught a TypeError")

try:
    print('unknown_var')    # NameError
except NameError:
    print("Caught a NameError")
    
    
    #FOR ASSIGNMENT 2
    # Task 1
try:
    s = "Hello"
    result = s.lower()
    print("Task 1 Output:", result)
except Exception as e:
    print("Error in Task 1:", e)


# Task 2
try:
    s = "HeLLo WoRLd"
    result = s.swapcase()
    print("Task 2 Output:", result)
except Exception as e:
    print("Error in Task 2:", e)


# Task 3
try:
    s = "HelloWorld"
    result = "".join([ch for ch in s if not ch.isupper()])
    print("Task 3 Output:", result)
except Exception as e:
    print("Error in Task 3:", e)

# Task 4
try:
    s = "EngiNEEr"
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    print(f"Task 4 Output: Uppercase: {upper}, Lowercase: {lower}")
except Exception as e:
    print("Error in Task 4:", e)


# Task 5
import string

try:
    s = "Data-Driven@2025!"
    result = "".join([ch for ch in s if ch.isalpha()])
    print("Task 5 Output:", result)
except Exception as e:
    print("Error in Task 5:", e)


# Task 6
import math

try:
    a, b, c = 3, 4, 5
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Task 6 Output:", area)
except Exception as e:
    print("Error in Task 6:", e)


# Task 7
try:
    names = ["Alice", "Bob", "Catherine", "David"]
    print("Task 7 Output:\n")
    print("Name".ljust(15, " "))
    print("-" * 15)
    for name in names:
        print(name.ljust(15, " "))
except Exception as e:
    print("Error in Task 7:", e)
    
    
    # Task 8
try:
    import string
    s = " Hello, World! "

    # i. Strip leading/trailing spaces
    cleaned = s.strip()

    # ii. Remove punctuation
    cleaned = "".join(ch for ch in cleaned if ch not in string.punctuation)

    # iii. Remove all spaces
    cleaned = cleaned.replace(" ", "")

    print("Task 8 Output:", cleaned)
except Exception as e:
    print("Error in Task 8:", e)