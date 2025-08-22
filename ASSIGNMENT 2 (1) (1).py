# ASSIGNMENT 2 
# Task 1
mally = 'Hello'
shasha = 'here'
race = 'LOVELY'
print(mally.lower())

print(shasha.lower())

print(race.lower())

# Task 2(all upper case turns lower case and all lower case turns upper case)
basic='HeLLo WoRLd'
print(basic.swapcase())

# Task 3 (remmove all upper case leters)
def remove_uppercase(t):
    return ''.join(c for c in t if not c.isupper())
t='HelloWOrld'
print(remove_uppercase(t))

# Task 4
def count_case(v):
    upper = sum(1 for c in v if c.isupper())
    lower = sum(1 for c in v if c.islower())
    return f"Uppercase:{upper}, Lowercase: {lower}"
v = 'EngiNEEr'
print(count_case(v))

# Task 5
def remove_non_letters(u):
    return''.join(c for c in u if c.isalpha())
u = 'Data-Driven@2025!'
print(remove_non_letters(u))

# Task 6 (Heron's formula for calculating area or a triangle)
a,b,c = 3,4,5
s = (a+b+c)/2
z=(1/2)
A = ((s*(s-a)*(s-b)*(s-c))**z)
print(A)

# Task 7
names = ['Cynthia', 'Lord', 'Arnold', 'Reece', 'Fank'] 
width = 20

print('Name'.center(width, '-'))
print('\nLeft aligned:\n')
for name in names:
    print(name.ljust(width))
print('\nRight aligned:\n')
for name in names:
    print(name.rjust(width))
print('\nCentered:\n')
for name in names:
    print(name.center(width))    
    
    #Task 8
    import string

def clean_string(s: str) -> str:
    # Remove leading/trailing whitespace
    s = s.strip()
    
    # Replace punctuation with empty string
    s = s.translate(str.maketrans('', '', string.punctuation))
    
    # Remove all spaces
    s = s.replace(" ", "")
    
    return s

# Example usage
input_str = " Hello, World! "
output_str = clean_string(input_str)
print(output_str)  # Output: "HelloWorld"


# CLASS WORK.
# write a code that prompys a user the value is even or odd
name=input('Enter your name: ')
y=int(input('Please enter an integer: '))

if y %2 == 0:
    print(name +' your number is even')
elif y %2==1:
    print(name +' your number is odd')
else:
    print(name + ' your input is invalid')
