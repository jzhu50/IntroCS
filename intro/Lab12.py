#Michelle Zhu
#The People Who Can't See the Board +1
#IntroCS pd3 sec4
#LAB12 
#2023-04-20
#time cost: 3
#collaborated with: Andrew Choi
#consulted: Chatgpt

# This is a python library that we will use to generate random numbers
import random

#==================================================
# Problem 0

# random.randrange( limit ) is a python function that returns a
# random integer in the range [0, limit)

# Write a function that will create and return a list of size n that
# is filled with random integers in the range [0, limit)

def rand_list(n, limit):
    g = []
    for elements in range(n):
        g.append(random.randrange(limit))
    return g

# When printed, a and b should have different values.
print(('=' * 10) + "Problem 0" + ('=' * 10))
a = rand_list(10, 10)
b = rand_list(10, 10)
print(len(a), a)
print(len(b), b)

# End Problem 0
#==================================================


#==================================================
# Problem 1
# Write a function that takes a list of non-negative integer
# values and returns a string of a bar graph representation of the list.
# The length of each bar should be the same as the value at that index.
# That means if g[0] = 9, then the first bar should have a length of 9.

def bar_graph(g):
    s = ''
    for q in g: #it loops through every item in the list
        s += q * "=" + "\n"
    return s

# The code below should have this output:
# 0: =========
# 1: =====
# 2: =====
# 3: ===
# 4: =
# 5: =====
# 6: =========
# 7: =====
# 8: =======
# 9: ========
print(('=' * 10) + "Problem 1" + ('=' * 10))
test = [9, 5, 5, 3, 1, 5, 9, 5, 7, 8]
print(bar_graph(test))

# This should print out the bar graph for your random
# lists from Problem 0
print(bar_graph(a))
print(bar_graph(b))

# End Problem 1
#==================================================


#==================================================
# Problem 2

# Write a function that returns the average of the
# values in a list. You may assume that the argument
# provided is a list that only contains numbers.

def list_avg( g ):
    avg = sum(g) / len(g)
    return avg

print(('=' * 10) + "Problem 2" + ('=' * 10))
# This should print 5.7
print( list_avg(test) )

# This should print out the averages of your random
# lists from Problem 0
print( list_avg(a) )
print( list_avg(b) )

# End problem 2
#==================================================


#==================================================
# Problem 3

# Write a function that returns the number of times
# the value n appears in list g.
# Im so dumb

def count(n, g):
    c = 0
    for p in g:
        if p == n:
            c += 1
    return c

print(('=' * 10) + "Problem 3" + ('=' * 10))
# This should print 4
print( count(5, test) )

# End Problem 3
#==================================================


#==================================================
# Problem 4

# Write a function that returns the mode (most frequently
# appearing value) of a given list.
# It should only return a single value, even if there are
# multiple modes, just return one of them.


def find_mode(g):
    count_dict = {} # Create an empty dictionary to keep track of counts
    for i in g:
        if i in count_dict:
            count_dict[i] += 1 # If the element is already in the dictionary, increment the count
        else:
            count_dict[i] = 1 # Otherwise, add the element to the dictionary with a count of 1
    guess = 0
    mode = ''
    for i in count_dict:
        if count_dict[i] > guess:
            guess = count_dict[i] # Count[i] counts the occurrences of each value
            mode = i
    return mode

print(('=' * 10) + "Problem 4" + ('=' * 10))
# Should print 5
print( find_mode(test) )

print( find_mode(a) )
print( find_mode(b) )

#==================================================
# Problem 5

# Write a function that keeps track of the frequencies of values
# from a list containing only integers.
# For example, if the provided list only contained 0s and 1s,
# and there were 8 0s and 23 1s, then the fucntion should
# return this list: [8, 23]
# It is important to understand that each index in the new
# list represents a value from the parameter list. So the new
# list needs to be as large as the biggest value in the parameter.
def list_counts(g, max_value):
    #This will create a new list with a size of max_value filled with 0s
    counts = [0] * (max_value)
    for x in g:
        counts[x] += 1
    return counts

print(('=' * 10) + "Problem 5" + ('=' * 10))
# Should print
# [0, 1, 0, 1, 0, 4, 0, 1, 1, 2]
test_counts = list_counts( test, 10 )
print( test_counts )

print( list_counts(a, 10) )
print( list_counts(b, 10) )

# create a new list of 10 random values in the range [0, 5)
# print that list
# YOUR CODE HERE


# create a list that correctly counts all the values in
# the new list you just made.
# print that list
# YOUR CODE HERE

# End Problem 5
#==================================================

#==================================================
# Problem 6
# If you use bar_graph on a list with sufficiently large
# values, you'll have a problem with the bars taking up
# more than one line.

# Write a new bar_graph function that will draw a scaled bar
# graph. It should take an argument for the scale factor,
# such that 1 piece of a bar represents 1 quantity equal
# to the scale factor.

def bar_graph_scaled(g, scale_factor):
    s = ''
    for r in range(len(g)):
        s += '=' * int(g[r]/scale_factor) + '\n'
    return s

print(('=' * 10) + "Problem 6" + ('=' * 10))
# Should print:
# 0: =====
# 1: ======
# 2: =
scale_test = [500, 670, 125]
print(bar_graph_scaled(scale_test, 100))

# now let's try it on a list with very large values
big_list = rand_list(10, 1000)
print(bar_graph_scaled(big_list, 25))

# End Problem 6
#==================================================


#==================================================
# Problem 7

# random.randrange() distributes numbers evenly, meaning
# that every possible random value has an equal chance
# of being returned.

# How could you test how evenly random.randrange()
# distributes the results?
# print out your answer as a string
print(('=' * 10) + "Problem 7" + ('=' * 10))
answer = 'adds a random integer between 0 to 9 inclusive to an empty list 10k times then counts appear'
print(answer)
# Write code below that performs the test you described.
# YOUR ANSWER BELOW

rand_list=[]
for i in range(10000):
    rand_list.append(random.randrange(10))
print(list_counts(rand_list,10))

# End Problem 7
#==================================================
