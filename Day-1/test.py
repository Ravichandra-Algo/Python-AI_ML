# Simple Python program to test functionality

# Print a welcome message
print("Hello, World!")  # Outputs: Hello, World!

# Perform a simple calculation and print the result
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")  # Outputs the sum of 5 and 10

# Define a string variable and print its value using an f-string
name = "ravi"
print(f"{name=}")  # Outputs the variable name and its value (e.g., "name='ravi'")

# Define a floating-point number and format it to 2 decimal places
salary = 100.55050
print(f"{salary=:.2f}")  # Outputs: salary=100.55 (formatted to 2 decimal places)

# Import the datetime module and get the current date and time
from datetime import datetime
now = datetime.now()  # Retrieves the current date and time
print(now)  # Outputs the full datetime object (e.g., 2024-12-07 15:30:45.123456)

# Format the current time and print it
print(f"Current time: {now:%H:%M:%S}")  # Outputs the time in HH:MM:SS format
print(f": {now:%H:%M:%S}")  # Another example of formatted time output

# Combine strings using f-strings
fileName = "data"
ext = "csv"
print(f"{fileName}.{ext}")  # Outputs: data.csv

# Format strings with padding and alignment
print(f"name with star:{name:*>10}")  # Outputs the name right-aligned, padded with '*' (e.g., "******ravi")
print(f"name:{name:*<10}")  # Outputs the name left-aligned, padded with '*' (e.g., "ravi******")

# Define another floating-point number and format it to 2 decimal places
profit = 44533333232.55050
print(f"profit:${profit:,.2f}")  # Outputs: profit=445.55 (formatted to 2 decimal places)


# ----------------------------------------------------------------
fName= 'Ravi'
lName= 'Patil'
age=26
isTrue = True
favoriteLanguage= 'Javascript'

print(f"{fName} {lName} {age} {favoriteLanguage} {isTrue}")
print(f"My name is {fName} {lName} I am {age} years old. My favorite programming language is {favoriteLanguage} and all these things are {isTrue}")
print(f"My name is "+fName+" "+lName+" I am "+str(age)+" years old.") # string concatenated using +

bill = 2022.554544
print(f"Bill without decimal is {bill:.2f}")
print(f"Bill without decimal is {int(bill)}") # The int() function truncates the decimal part and keeps only the integer part of the number, effectively extracting 2022 from 2022.554544

nameWithStar = 'Hey'
print(f"{nameWithStar:*>10}")
print(f"{nameWithStar:&<10}")

from datetime import datetime as date
todaysDate = date.now()
print(f"{todaysDate:%Y-%m-%d %H:%M:%S}") # Y= year, m = month, d = day (m, d are in small case)

print("Python".center(10))
print("Python".ljust(10))
print("Python".rjust(10))
print('Python'.rjust(15,'*'))
print('Python'.ljust(15,'-'))

fruits = ['mango', 'apple', 'orange', 'banana', 'grapes']
mixedDataTypes = ['mango', True, 20, 5.001]

print(fruits[0]) # first fruit
print(fruits[-1]) # last fruit using -1
print(fruits[:3])
print(mixedDataTypes)

# del lName
# print(lName) this will throw error because lName is already deleted

print(type(lName)) #type checking

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print(f"{numbers=}")

numbers.insert(2, 99)
print(f"{numbers=}")

numbers.pop()
print(f"{numbers=}")

numbers.remove(3) # remove first occurrence
print(f"{numbers=}")

numbers.insert(1, "Python")
print(f"{numbers=}")

toBeSort = [10, 5, 8, 2, 7, 9]
print(f"{toBeSort=}")

toBeSort.sort()
print(f"{toBeSort=}") #sorted in ascending order

toBeSort.sort(reverse=True) # descending order
print(f"{toBeSort=}")

toBeSort.append('Hello')
print(f"{toBeSort=}")

toBeSort.sort(key=str)
print(f"{toBeSort=}")

generatedList1 = [n for n in range(0, 10)]
print(f"{generatedList1=}")

generatedList2 = [n*n for n in range(0, 10)] # n**2
print(f"{generatedList2=}")

generatedList3 = [n for n in range(0, 10) if n%2==0]
print(f"{generatedList3=}")

generatedList4 = [n for n in range(0, 30) if n%2==0 and n%3==0]
print(f"{generatedList4=}")

nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for subList in nestedList:
    print(subList)
    
flattenArray = [item for sublist in nestedList for item in sublist] # List Comprehension
print(f"{flattenArray=}")

print(f"Smallest number {min(flattenArray)}")
print(f"Largest number {max(flattenArray)}")
print(f"Sum of the numbers {sum(flattenArray)}")

duplicates = [1,2,5,5,3,3,4]

print(f"unique elements {list(set(duplicates))}")


#----------------------------------------------------------------

palidromeNumbers = 12321

def isNumberPalindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

print(f"is number palindrome: {isNumberPalindrome(palidromeNumbers)}")

# bytes data type
b2 = b'Hello'  
print(type(b2)) 

# bytearray data type (mutable)
b3 = bytearray([66, 55, 56, 70])
print(b3)

print(type({"one", 654, 5+6j,})) #set type

# tuple literal
T1=(1,"Ravi",75.50, True)
print (T1, type(T1))


a = 21
b = 10
if ( a == b ):
   print ("a is equal to b")
else:
   print ("a is not equal to b")
   
mark = 51
result = ""
if mark < 10:
    result = "Failed"
elif mark > 10 or mark < 50:
    result = "Passed"
else:
    result = 'Neither Passes nor failed'

print(result)

def weekday(n):
   match n:
      case 1: return "Monday"
      case 2: return "Tuesday"
      case 3: return "Wednesday"
      case 4: return "Thursday"
      case 5: return "Friday"
      case 6: return "Saturday"
      case 7: return "Sunday"
      case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(0))

def hasAccess(user):
   match user:
      case "admin" | "manager": return "Full access"
      case "Guest": return "Limited access"
      case _: return "No access"
print (hasAccess("manager"))
print (hasAccess("Guest"))
print (hasAccess("Ravi"))