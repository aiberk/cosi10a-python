# So that it also finds the smallest number inputed by the user.

# Here is the original code
# '''
# L10 -- demos for Lesson 10
# '''

# def average_script():
#     ''' calculates the average (mean) and max from sequence of numbers inputed by user '''
#     print('Enter a sequence of numbers and we will find the average.')

#     n = float(input("Enter your first number: "))
#     sum = n   #this is the sum of the numbers so far
#     num_values=1 # this is the number of values so far
#     max_val=n  # this is maximum value so far

#     more = input("enter more numbers?  (y or n) ")
#     while more=='y':
#        n = float(input("Enter a number: "))
#        sum = sum+n  # add n to the sum
#        num_values = num_values+1 # add 1 to the number of values
#        if n>max_val:
#            max_val=n
#        more = input("enter more numbers?  (y or n) ")

#     mean = sum/num_values
#     print('the average of the',num_values,'numbers is',mean)
#     print('the largest value was',max_val)
#     print('goodbye')

    