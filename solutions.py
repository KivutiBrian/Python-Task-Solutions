# PRACTICE QUESTIONS: PART A

"""""QN1.We should create a function that ‘findsgrade’ by taking in marks of each subject as parameters
calculating total from the parameters(subjects) passed
calculating the average from the total"""


""""
GRADING SYSTEM
A 80-100
B 70 -79
C 60-69
D 50 -59
E 0-49
"""

def findsgrade(math,eng,kisw,sci,sst,):
    totalScore = math+eng+kisw+sci+sst
    average = totalScore/5
    grade = None
    if average >=80 and average <=100:
        grade = 'A'
    elif average >= 70 and average <=79:
        grade = 'B'
    elif average >=60 and average <= 69:
        grade = 'C'
    elif average >= 50 and average <= 59:
        grade = 'D'
    elif average >= 0 and average <=49:
        grade = 'E'
    else:
        grade = 'NULL (AVERAGE SCORE CANNOT BE GREATER THAN 100)'

    print("MATHS:",math, "ENG:",eng, "KISW:",kisw, "SCI:",sci, "SST:",sst )
    print("TOTAL SCORE:", totalScore)
    print("AVERAGE SCORE:", average)
    print("GRADE:", grade)

# findsgrade(40,50,60,20,40)


"""""QN2.Write a function called sum_digits that is given an integer num and returns the sum of the digits of num"""
def sum_digits(num):
    tostr = str(num) #convert the num passed in to a string
    sum = 0 #initialize the sum to zero
    for i in tostr: #going over every digit usinf a for loop
        sum += int(i)

    print(sum)

    return sum

# sum_digits(1255464336)




#######################################################################################################################
#######################################################################################################################

# PRACTICE QUESTIONS: PART B

""""TASK 1:Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", 
otherwise print "No". 
Hint: Use input () to get the persons input
"""""

# userInput = input("Provide a string!:")
#
# if userInput == 'yes' or userInput == "YES" or userInput== 'Yes':
#     print(userInput.title())
# else:
#     print('No')


"""""TASK 2: Implement a function that takes as input three variables, and returns the largest of the three."""""
def findTheLargest(a,b,c):
    if a > b and a > c:
        print(a,'is the largest')
    elif b > a and b > c:
        print(b, 'is the largest')
    elif c >a and c>b:
        print(c,"is the largest")

# findTheLargest(100,200,5)





""""TASK 3:Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list 
of only the first and last elements of the given list. For practice, write this code inside a function
 """""

def generateNewList(alist):
    newList = []
    firstElement = alist[0]
    lastElement = alist[-1]
    newList.append(firstElement)
    newList.append(lastElement)
    print(newList)
    return  newList

# generateNewList([5,10,15,20,25])



"""""TASK 4:Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
 to the user.
 """

# # Ask the user for any number
# anyNumber = input("Enter a number:")
# # evalute the number and print out appropriate messages.
# if int(anyNumber)%2 == 0:
#     print("{} is an even number".format(anyNumber))
#     if int(anyNumber)%4 == 0:
#         print("{} is a multiple of 4".format(anyNumber))
# else:
#     print("{} is an odd number".format(anyNumber))



"""TASK 5: With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
write a program to print the first half values in one line and the last half values in one line.
"""
def split_the_tuple(atuple):


    # find the midpoint
    half = int(len(atuple)/2)

    # get the first half and other half of the tuple
    first_half = atuple[:half]
    last_half = atuple[half:]

    #convert the halfs into strings
    first_half_toString = str(first_half)
    last_half_toString = str(last_half)

    #use the strip function in python that returns a copy of the string with both leading and trailing characters removed
    first_half_values = first_half_toString.strip('()')
    last_half_values = last_half_toString.strip('()')

    print(first_half_values)
    print(last_half_values)

# split_the_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


#######################################################################################################################
#######################################################################################################################
                                    # Practice questions: PART C

"""a)Create a function that takes a name and returns a greeting."""
def hello_name(name):
    return 'Hello {}!'.format(name)

# print(hello_name('Gerald'))


"""b)Write a function that takes the base and height of a triangle and return its area."""
def tri_area(base,height):
    return int((0.5) * base * height)

# print(tri_area(3,2))
# print(tri_area(7,4))
# print(tri_area(10,10))

"""c)Create a function that finds the maximum range of a triangles third edge."""
def next_edge(side1, side2):
    max_range_third_edge = (side1 + side2) - 1
    return max_range_third_edge

# print(next_edge(8,10))
# print(next_edge(5,7))
# print(next_edge(9,2))

"""d)Create a function that takes a list and returns the first element."""
def get_first_value(alist):
    first_element = alist[0]
    return first_element

# print(get_first_value([1, 2, 3]))
# print(get_first_value([80, 5, 100]))
# print(get_first_value([-500, 0, 50]))

"""e)You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm. 
Return the total number of legs on your farm. (CREATE A FUNCTION)"""

def animals(chickens,cows,pigs):
    total_legs = (chickens * 2) + (cows * 4) + (pigs * 4)
    return  total_legs

# print(animals(2,3,5))
# print(animals(1,2,3))
# print(animals(5,2,8))


"""f)Create a function that takes a list of numbers. Return the largest number in the list."""

# solution A
def findLargestNum(alist):
    maxnum = max(alist)
    return  maxnum

# print(findLargestNum([4, 5, 1, 3]))
# print(findLargestNum([300, 200, 600, 150]))
# print(findLargestNum([1000, 1001, 857, 1]))


# solution B
def largestNum(alist):
    largest = 0
    for i in alist:
        if i > largest:
            largest = i
    return largest

# print(largestNum([4, 5, 1, 3]))
# print(largestNum([300, 200, 600, 150]))
# print(largestNum([1000, 1001, 857, 1]))

"""g))Given a list of integers, return the difference between the largest and smallest integers in the list."""
# solution A
def difference(alist):
    maxnum = max(alist)
    minnum = min(alist)

    diff = maxnum - minnum

    return diff

# print(difference([10, 15, 20, 2, 10, 6]))
# print(difference([-3, 4, -9, -1, -2, 15]))


"""h)Create a function to concatenate two integer lists."""
def concat(ls1,ls2):
    fullList = ls1+ls2
    return fullList

# print(concat([1, 3, 5],[2, 6, 8]))
# print(concat([7, 8],[10, 9, 1, 1, 2]))
# print(concat([4, 5, 1],[3, 3, 3, 3, 3]))


"""i)Create a function that takes two strings as arguments and return either True or False depending on whether the total 
number of characters in the first string is equal to the total number of characters in the second string."""
def comp(stringa,stringb):
    lenStringA = len(stringa)
    lenStringB = len(stringb)

    if lenStringA == lenStringB:
        return True
    else:
        return False

# print(comp("AB", "CD"))
# print(comp("ABC", "DE"))
# print(comp("hello", "edabit"))

"""j)Write a function that converts a dictionary into a list, where each element represents a key-value pair."""

# when working with dictionaries, you work with both keys and value
# One of the most useful ways to iterate through a dictionary in Python is by using .items()
# which is a method that returns a new view of the dictionary’s items:

def convert_to_array(adictionary):
    newList = []
    for item in adictionary.items():
        # print(list(item))
        newList.append(list(item))
    return newList

# print(convert_to_array({ "a": 1, "b": 2 }))
# print(convert_to_array({ "shrimp": 15, "tots": 12 }))
# print(convert_to_array({}))

"""k)You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
 You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), 
 and the starting inventory. Return the total profit made, rounded to the nearest dollar. 
 Assume all of the inventory has been sold
 
 NOTE:Profit = Total Sales - Total Cost
 
 """

def profit(adictionary):
    profit = int((adictionary['sell_price'] - adictionary['cost_price']) * adictionary['inventory'])
    return profit

# print(profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }))
#
# print(profit({
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# }))
#
# print(profit({
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# }))

"""
Abigail and Benson are playing Rock, Paper, Scissors.
Each game is represented by an array of length 2, where the first element represents what Abigail played 
and the second element represents what Benson played.

Given a sequence of games, determine who wins the most number of matches. If they tie, output "Tie".

R stands for Rock
P stands for Paper
S stands for Scissors
"""

x = [["R", "P"], ["R", "S"], ["S", "P"]]


def calculate_score(alist):
    # print(alist)
    winList = []

    for i in alist:
        # print(i)
        # print(i[0])
        if i[0] == i[-1]:
            print('Draw')
            winList.append('Draw')
        elif (i[0] == 'R') and (i[-1] == 'P'):
            print("Paper beats Rock")
            winList.append('Right')
        elif (i[0] == 'R') and (i[-1] == 'S'):
            print("Rock beats Scissors")
            winList.append('Left')
        elif (i[0] == 'S') and (i[-1] == 'P'):
            print("Scissors beat Paper")
            winList.append('Left')
        elif (i[0] == 'S') and (i[-1] == 'R'):
            print("Rock beats Scissors")
            winList.append("Right")

    print('')
    abiwins = winList.count('Left')
    benwins = winList.count('Right')
    print(abiwins)
    print(benwins)

    print(winList)


# calculate_score([["R", "R"], ["S", "S"]])
# calculate_score([["R", "P"], ["R", "S"], ["S", "P"]])