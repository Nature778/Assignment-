    #ASSIGNMENT 5(USING FUNCTIONS FOR ASSIGNMENT 1 AND 2)
# Task 1
def task1():
    print("\n--- Task 1 ---")
    ama = 344
    kwame = 56.78
    john = 'affum'
    baidoo = True
    print(ama, type(ama))
    print(kwame, type(kwame))
    print(john, type(john))
    print(baidoo, type(baidoo))

# Task 2
def task2():
    print("\n--- Task 2 ---")
    s = int(19.99)
    t = str(50)
    u = float('50')
    print(s,type(s))
    print(t,type(t))
    print(u,type(u))

# Task 3
def task3():
    print("\n--- Task 3 ---")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print("Hello, " + first_name + " " + last_name + "!")


# Task 4
def task4():
    print("\n--- Task 4 ---")
    age = 20
    # Corrected version
    print("You are " + str(age) + " years old.")
    print("Explanation: Cannot concatenate 'str' with 'int' without converting the int to string.")


# Task 5
def task5():
    print("\n--- Task 5 ---")
    word = input("Enter your favourite word: ")
    count = int(input("How many times to repeat it? "))
    print((word + " ") * count)


# Task 6
def task6():
    print("\n--- Task 6 ---")

    # Matching error codes with types inside functions
    def syntax_error_demo():
        try:
            eval('print("Hello')   # incomplete string literal = SyntaxError
        except SyntaxError:
            print("Caught a SyntaxError")

    def value_error_demo():
        try:
            int("abc")          # Cannot convert "abc" to int
        except ValueError:
            print("Caught a ValueError")

    def type_error_demo():
        try:
            result = "age" + 10  # Cannot add str + int
        except TypeError:
            print("Caught a TypeError")

    def name_error_demo():
        try:
            print('not_defined_var')  # Variable not defined
        except NameError:
            print("Caught a NameError")

    # Run all
    syntax_error_demo()
    value_error_demo()
    type_error_demo()
    name_error_demo()

# Main function to run everything
def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()


# Run program
if name == "_main_":
    main()
    
    #FOR ASSIGNMENT 2
    import math
import string

# Task 1: Convert all uppercase to lowercase
def task1(s):
    return s.lower()

# Task 2: Swap uppercase <-> lowercase
def task2(s):
    return s.swapcase()

# Task 3: Remove uppercase letters
def task3(s):
    return "".join([ch for ch in s if not ch.isupper()])
                   
# Task 4: Count uppercase and lowercase
def task4(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return f"Uppercase: {upper}, Lowercase: {lower}"

# Task 5: Remove non-English letters
def task5(s):
    return "".join([ch for ch in s if ch.isalpha()])

# Task 6: Heron’s Formula for triangle area
def task6(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Task 7: Format names neatly in a table
def task7(names):
    output = "Name".ljust(15) + "\n" + "-"*15 + "\n"
    for name in names:
        output += name.ljust(15) + "\n"
    return output

# Task 8: Clean string → strip, remove punctuations, remove spaces
def task8(s):
    s = s.strip()
    s = "".join(ch for ch in s if ch not in string.punctuation)
    s = s.replace(" ", "")
    return s


    
