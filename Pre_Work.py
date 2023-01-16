# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the
# function. The first line of the code has been defined as below. 
def hello_name(user_name):
    """Greeting for user"""
    print("Hello, " + user_name + "!")
hello_name('Brock Anderson')

# Question 2:
# Write a python function, first_odds that prints the odd numbers
# from 1-100 and returns nothing.
# I was unsure of the question being asked, so what is below returns
# nothing. If you add another line and call the function, it will 
# output all of the odd numbers from 1-100. 
def first_odds():
    """Displays odd numbers from 1-100"""
    for x in range(1, 100, 2):
        print(x)

# Question 3:
# Please write a Python function, max_num_in_list to return the max
# number of a given list. The first line of the code has been defined as
# below. 
def max_num_in_list(a_list):
    print(max(a_list))
number_list1 = [100,200,500,200]
number_list2 = [25,75,100,10]
max_num_in_list(number_list1)
max_num_in_list(number_list2)

# Question 4:
# Write a function to return if the given year is a leap year. A
# leap year is divisible by 4, but not divisible by 100, unless it
# is also divisible by 400. The return should be boolean Type
# (true/false). 
def is_leap_year(a_year):
    if a_year % 100 == 0:
        if a_year % 400 == 0:
            a_year = True
            print(bool(a_year))
        else:
            a_year = False
            print(bool(a_year))
    elif a_year % 4 == 0:
        a_year = True
        print(bool(a_year))
is_leap_year(400)
is_leap_year(100)
is_leap_year(1996)

# Question 5:
# Write a function to check to see if all numbers in list are
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive
# numbers, but [1,2,4,5] are not consecutive numbers. The return
# should be boolean Type. 
def is_consecutive(a_list):
    if a_list[0] + len(a_list) -1 == a_list[-1]:
        a_list=True
        print(bool(a_list))
    else:
        a_list = False
        print(bool(a_list))
a_list1 = [1,3,3,4,5,6,7,8,10]  #False
a_list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]  #True
is_consecutive(a_list1)
is_consecutive(a_list2)
