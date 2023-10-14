#----------------------------------------------------------------------------------
#reviewing recursion in Python
#if in interview, ask the interviewer WHERE they consider the Fibonnacci Sequence...
#...to start, as courtesy and to not make assumptions.(aka if 0 is included)
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
#Part 1: Factorials
#I need to divide n! into two cases:
#1. where n! = (n*(n-1)!) IF n >= 1
#2. and   n! = 1 (in every other case, aka n = 0)
#----------------------------------------------------------------------------------
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

#this function ^^ calls itself
#----------------------------------------------------------------------------------



# Part 2: Fibonnacci
# 1 1 2 3 5 8 13 21 34...
#----------------------------------
def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)
#          ^
result = fib(1000000)
print(result)
#----------------------------------
#---I START CODING WAY TOO SOON----
#THINK ABOUT THE PROBLEM MORE FIRST
#---------USE PSEUDOCODE-----------

#followup: how would i find the nth factorial number?
        
