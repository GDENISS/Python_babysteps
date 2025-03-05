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