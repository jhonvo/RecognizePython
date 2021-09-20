num1 = 42 #variable declaration - Numbers
num2 = 2.3 #variable declaration - Numbers
boolean = True #variable declaration - Boolean
string = 'Hello World' #variable declaration - Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List - initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #Dictionary - initialize
fruit = ('blueberry', 'strawberry', 'banana') #Tuples - initialize
print(type(fruit)) #log statement - type check
print(pizza_toppings[1]) #log statement - List access value 
pizza_toppings.append('Mushrooms') #List - add value
print(person['name']) #log statement - Dictionary - access value
person['name'] = 'George' #Dictionary - change value
person['eye_color'] = 'blue' #Dictionrary - NameError: name <variable name> is not defined
print(fruit[2]) #log statement - Tuples - access value

if num1 > 45: #Conditional if
    print("It's greater") #log statement
else: #Conditional else
    print("It's lower") #log statement

if len(string) < 5: #Conditional if
    print("It's a short word!") #log statement
elif len(string) > 15: #Conditional elseif
    print("It's a long word!") #log statement
else: #Conditional else
    print("Just right!") #log statement

for x in range(5): #for loop - start
    print(x) #log statement
for x in range(2,5): #for loop - stop
    print(x) #log statement
for x in range(2,10,3): #for loop - increment
    print(x) #log statement
x = 0 # variable declaration
while(x < 5): #while loop - start
    print(x) #log statement
    x += 1 #while loop - increment

pizza_toppings.pop() #list - remove value
pizza_toppings.pop(1) #list - ?

print(person) #log statement
person.pop('eye_color') #error
print(person) #log statement

for topping in pizza_toppings: #foor lop - start
    if topping == 'Pepperoni': #conditional if
        continue #foor loop - continue
    print('After 1st if statement') #log statement 
    if topping == 'Olives': #conditional if
        break #foor loop - break

def print_hello_ten_times(): #function - parameter
    for num in range(10): #function - argument
        print('Hello') #function #return

print_hello_ten_times() #function

def print_hello_x_times(x): #function - parameter
    for num in range(x): #function - argument
        print('Hello') #function #return

print_hello_x_times(4) #function

def print_hello_x_or_ten_times(x = 10): #function - parameter
    for num in range(x): #function - argument
        print('Hello') #function #return

print_hello_x_or_ten_times() #function
print_hello_x_or_ten_times(4) #function


""" #length check
Bonus section #length check
""" #length check

# print(num3) - comment
# num3 = 72 - comment 
# fruit[0] = 'cranberry'- comment error tuples chaneg value
# print(person['favorite_team'])- comment - KeyError: 'favorite_team'
# print(pizza_toppings[7])- comment  - IndexError: list index out of range
#   print(boolean)- comment 
# fruit.append('raspberry')- comment - error Tuples add value
# fruit.pop(1)- comment - error delete value