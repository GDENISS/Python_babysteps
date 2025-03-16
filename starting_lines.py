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
    text = my_file ('This is really interesting 😁')
    print (my_file.readlines())