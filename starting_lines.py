#Day one practice
# conditional statements if else elif

is_magician = False
is_expert = True

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician and not is_expert:
    print('atleast you are getting there')
elif not is_magician:
    print('you need magic powers')
#conditional statements if else elif all are used to check the conditions and break the loop if the condition is met
# if the condition is not met then the loop will continue to the next condition

#Day two practice
#adding various numbers
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for i in my_list:
    counter += i
print(counter)
#the above is a simple example of adding numbers in a list using a for loop
#the for loop will iterate through the list and add the numbers to the counter

#Day three practice
# finding duplicates in a list
some_list = ['a','b','c','b','d','e','c','c']

Duplicates = []

for i in some_list:
    if some_list.count(i) > 1:
        if i not in Duplicates:
            Duplicates.append(i)

print(Duplicates)

#Another method 😂2.0 list damn comprehensions.
Duplicates = [i for i in some_list if  some_list.count(i)>1]

print(list(set(Duplicates)))
# The second method is a quick way to find duplicates in a list using list comprehensions
#list comprehensions are unique mordern way of qenerating list.

#Day four practice
#finding the highest even number in a list using a function

def highest_even(li):
    evens = []
    for i in li:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)
print(highest_even([10,2,86,4,6,8,24]))

#Day five practice
#Creating a class

class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

player1 = PlayerCharacter('Cindy', 44)

print(player1.name)
print(player1.age)

#the above is a simple example of creating a class in python
#the class has two attributes name and age  
#the class also has a method run that prints 'run'
#an object player1 is created using the class PlayerCharacter


class car:
    def __init__(self, make,model):
        self.make = make
        self.model = model

print (car('Range Rover', 'Vogue'))
car1 = car('Range Rover', 'Vogue')
car2 = car('Toyota', 'Corolla')

print(car1.model)

#the above class shows a simpe example of a class with two attributes make and model
#two objects car1 and car2 are created using the class car
#the object car1 is printed to show the model attribute

#Day six practice
# Define a base class 'User'
class User():
    # Method to simulate signing in
    def sign_in(self):
        print('logged in')

# Define a derived class 'Wizard' that inherits from 'User'
class Wizard(User):
    # Constructor method to initialize Wizard objects
    def __init__(self, name, power):
        # Instance variables to store the name and power of the wizard
        self.name = name
        self.power = power

    # Method to simulate an attack
    def attack(self):
        print(f'attacking with power of {self.power}')

# Define another derived class 'Archer' that inherits from 'User'
class Archer(User):
    # Constructor method to initialize Archer objects
    def __init__(self, name, num_arrows):
        # Instance variables to store the name and number of arrows
        self.name = name
        self.num_arrows = num_arrows

    # Method to simulate an attack
    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')

#Day 7 Practice!
# Reading files in python

#file I/O
#To ensure this part works create a file in your working directory and reaad it.
with open('whoops.txt') as my_file:
    # Open the text.txt we made earlier
    # We can now read the file
    print(my_file.read())
    # But what happens if we try to read it again?
    my_file.seek(0)
    # Seek to the start of file (index 0)
    my_file.seek(0)
    # Now read again
    print(my_file.read())
    # Readlines returns a list of the lines in the file
    my_file.seek(0)
    print(my_file.readlines())

#Day 8 Practice
# Writing to files in python
with open('whoops.txt', mode='r+') as my_file:
    # the part of mode = 'r+' allows one to read and write into a file. 
    my_file.write('This is really interesting 😁')
    print (my_file.readlines())

#first I apologise I worked on day nine and failed to commit ):
#this is new coctent for day nine
#difference between append() and extend() in Python
#append() increases the list length by 1, while extend() increases it by the length of the iterable

my_list1 = [1,2,3,4,5,6,7,8,9]

my_list1.append(10)

print (my_list1)

# extend

my_list2 = [2,4,6,8,10]
my_list3 = [1,3,5,7,9]

my_list2.extend(my_list3)

print(my_list2)

#I decided to add a sorted method to ensure the list is logical.
print(sorted(my_list2))


#Day 10

def is_palindrome(s):
    cleaned = ' '.join(char.lower()for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))

# The above is a simple function that checks a palindrome
#Day 11
# finding second largest number in a list

def second_largest(numbers):
    new_num = sorted(numbers)
    ascend = new_num[::-1]
    print(ascend[1])

second_largest([5, 2, 9, 1, 7, 6, 3])
#this is a hypothetical idea
# The real way of finding the second largest number using O(n)
def second_largest(numbers):
    
    largest = float('-inf')
    second = float('-inf')
    
    for num in numbers:
        if num > largest :
            second = largest
            largest = num
        elif num > second and num != largest :
            second = num

    return second

print (second_largest([5, 2, 9, 1, 7, 6, 3]))

#This is a more logical way of finding the second largest value in alist.
#Day eleven is already here 

def merged_sorted(List1,List2):
    for i in List1:
        List2.append(i)
    return sorted(List2)

print(merged_sorted([1, 3, 5],[2, 4, 6]))

#merging two list and ensuring they are well sorted
#infact it is already day twelve

def merged_sorted(List_1,List_2):
    combined = List_1 + List_2
    return sorted(combined)

print(merged_sorted([1, 3, 5],[2, 4, 6]))

#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

def sets_data():
    set_a = input('Please enter numbers separated by space: ')
    set_b = input('Please enter numbers separated by space: ')

    integer_set_a = [x for x in set_a.split()]
    integer_set_b = [i for i in set_b.split()]

    new_set = []

    for x in integer_set_a:
        for i in integer_set_b:
            if x == i:
                new_set.append(x)
    return set(new_set)



print(sets_data())
#this is how we get to week 13 in style.

# Time for a second week  wrap up
# We create a partner to help us in preparing for the new dream

def ignite_future():
    start = time.time()
    while True:
        elapsed = time.time() - start
        print(f"Rendering Vision: {elapsed:.1f}s elapsed | Stand by for the shift...")
        time.sleep(1)  # Simulates the build-up to something big

ignite_future()

#Thankyou for the company.
#As we start another week lets reflect on whhat we have been doing 
#The basic of python starts with the syntax the elememts of good code starts with
#Clean; ensure the code is up to standard, by ensuring we have the correct method for this
#readerbillity; let your code be as simpe as posible.achieved through commenting.
#Predicability; let the code be easy to understand and predictable.
#DRY; Do not repeat your self,avoid redundant code and meethods
#Understand the data structures
#ok that said and done lets do something fun:

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
] #we created a matrix representing an image of a tree

for row in picture: #looping through the matrix to identify pixels and non pixels.
    for pixel in row:
        if pixel == 1:
            print('*',end='')
        else:
            print(' ',end='')
    print('')

# ther we go we created a christmas tree.


# simple if statements:
def calculate_discount(price,discount):
    
    if discount >= 20:
        discount = discount/100
        discout_price = price * discount
        new_price = price - discout_price
        return new_price
    else:
        return price
   

#practical applications

price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage (e.g., 20 for 20%): "))


final_price = calculate_discount(price, discount)

if discount >= 20:
    print(f"Final price after {discount}% discount: {final_price: }")
else:
    print(f"No discount applied. Original price: {price: }")

# I thought maybe we could revisit the files and how to work with them

input_text = """
This is the first line of the text file.
Here is another line to add more content.
Python programming is fun and versatile.
We can process text files easily with Python.
Let's count words and convert text to uppercase.
"""
with open("input.txt", mode = 'r+') as my_file:
    my_file.write(input_text)
    

with open('input.txt', mode='r') as my_file:
    content = my_file.read()

print(content)
num_words = len(content.split())
print(num_words)

upper_case = content.upper()

with open('Output.txt', mode='r+') as New_file:
    New_file.write(f"Processed Text:\n{upper_case}\n\nWord Count: {num_words}")

#We need to create two files input.txt and Output.txt

#Recursive function
def tricky_function(x):
    if x > 0:
        return x + tricky_function(x - 1)
    else:
        return 0 

result = tricky_function(5)
#the output of the function is 15

x = 0
while x < 20:
    x += 1
    if x % 2 != 0:
        print(x)

# finding the odd numbers between 0 and 20
