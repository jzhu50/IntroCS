#3Slays: Michelle Zhu, Linda Zheng, Krystal Khine
#IntroCS pd03/sec04
#LAB14
#2025-05-05f
#time cost: 1
#Consulted: Ben Goihman

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DISCOVERIES:
D: .split() separates a string into given parameter, or if left default, extra spaces
D: 
...

QUESTIONS/COMMENTS/CONCERNS:
Q:
C:
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

#==================================================
# Problem 0

# We can open and read text files in python like so:
#    f = open("file_name")
#    s = f.read()
# Notice that the file name should be a string.
# In order to make opening the file easy, make sure the file
# is in the same directory as your python program file.
#
# It is a good idea to close a file when you're done with
# it, which you can do like so:
#    f.close()
# 
# There is a file called 'nyc_pop.csv' that you can find in
# the same places as this lab file. Download it and put it
# in the same directory as this file.
#
# Write code that will open 'nyc_pop.csv' and the read its
# contents into a string called text.
#
# YOUR CODE HERE
f  = open("nyc_pop.csv")
text = f.read()
print(text)

# You may notice an extra newline after the file, this can
# happen if there are any blank lines after the file. There
# is a python method called strip that will return a copy of
# with extra whitespace (space, newlines, tabs) removedfrom the
# beginning and end of a string. The code below uses strip to
# get rid of any extra whitespace on the ends of text.
text = text.strip()
print(text)


print('==================================================')
# End Problem 0
#==================================================

#==================================================
# Problem 1
#
# You should notice that the file contains population data for
# The boroughs of NYC from 1790 - 2010. It is formatted such that
# Each line represents one year, and contains a series of numbers
# separated by ','. This is a common way of representing data in
# plain text, since it is easily accessible in programming. The
# file type is called 'comma separated value' or 'csv'.
#
# Often, the first line of a .csv file will contain the headers
# that describe what each value represents.
#
# Write a function that will take a string representing the text
# of a file that looks similar to 'nyc_pop.csv' and returns a list
# that contains only the headers.

def get_headers(s):
    
    #Splits the text where a new line starts. Values are assigned into the list: lstv
    lstv = s.split('\n')
    
    #Splits the first line of a given text by commas. Values are assigned to the list: g
    g = lstv[0].split(',')
    
    return g
            
# Should print
# ['Year', 'Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']
pop_headers = get_headers(text)
print(pop_headers)

print('==================================================')
# End Problem 1
#==================================================

#==================================================
# Problem 2
#
# Write a function that will take a string representing the text
# of file that looks similar to 'nyc_pop.csv' and returns a list of
# lists.
# Each sublist should represent a line from the file.
# Each element in a sublist should represent one value.

def get_data(s):
    ret_list = s.split('\n')
    
    #For each index in ret_list, a new list is made that separates values in the index by commas
    for i in range(len(ret_list)):
        ret_list[i] = ret_list[i].split(',')
        
    #Returns list without heading
    return ret_list[1:]

# Should print:
# [['1790', '33131', '4549', '6159', '1781', '3827'], ['1800', '60515', '5740', '6642', '1755', '4563'],
# There will be more sublists after that.
pop_data = get_data(text)
print(pop_data)

print('==================================================')
# End Problem 2
#==================================================

#==================================================
# Problem 3
#
# Write a function that will take a list of lists similar to pop_data,
# where every element is a string, and change each element in each
# sublist to a number.
#
# Note that this function modifies the parameter list, it does not
# return a new list.
#
# You can assume that the parameter only contains lists of number strings.

def number_convert(data):
    #Iterates through every list of values
    for j in range(len(data)):
        
        #Iterates through every value within each list
        for i in range(len(data[j])):
            
            #Sets each value in the list as an integer
            (data[j])[i] = int((data[j])[i])
            
# Should print
# [[1790.0, 33131.0, 4549.0, 6159.0, 1781.0, 3827.0 ], [1800.0, 60515.0, 5740.0, 6642.0, 1755.0, 4563.0],
# There will be more sublists after that.
number_convert(pop_data)
print (pop_data)

print('==================================================')
# End Problem 3s
#==================================================

#==================================================
# Problem 4
#
# Now that we have the data from our csv file in number form,
# We can actually do something with it!
#
# Write a function that takes a list similar to pop_data, and
# returns the total of the values in a given row. For pop_data,
# it would return the total population for a given year.

def row_total(row_key, data):
    total = 0
    
    #Iterates through each element in "data." Each element is assigned as variable "row."
    for row in data:
        
        #Determines if data corresponds to correct row_key
        if row[0] == row_key:
            
            #Subtracts row_key from total
            total =- row_key
            
            #Iterates through each value in correct row, and adds them to the total
            for num in row:
                total += num
                
            return total
        
    #Returns 0 if row_key is invalid
    return 0


    
    
# Should print 49447.0
print( row_total(1790, pop_data) )

# How many people lived in NYC in 1880?
print( row_total(1880, pop_data) )


print('==================================================')
# End Problem 4
#==================================================

#==================================================
# Problem 5
#
# Write a function that takes a list similar to pop_data, and
# returns a list containing the values in a given column. For pop_data,
# it would return a list where each element is the population of
# a specific borough.
#
# The function should take the list of headers, as well as a string
# for the specific header being looked at.

def get_column(key, headers, data):
    index = 0
    ret_list=[]
    
    #Iterates through list of headers to find index of "key"
    for i in range(len(headers)):
        if headers[i] == key:
            index = i
            
    #Appends values from column of the key to a list
    for i in data:
        ret_list.append(i[index])
        
    return ret_list

# Should print
# [1781.0, 1755.0, 2267.0, 2782.0, 3023.0, 5346.0, 8032.0, 23593.0, 37393.0, 51980.0,
# With more data after that
bronx_pops = get_column('Bronx', pop_headers, pop_data)
print(bronx_pops)


# Write code that would get the list of years that we have population data for.
# print to check
pop_years=[]

#Appends first value of each element in pop_data to pop_years
for data in pop_data:
    pop_years.append((data[0]))
    
print(pop_years)
print('==================================================')
# End Problem 5
#==================================================

#==================================================
# Problem 6
#
# Use code to answer the following questions. Your code
# should print out the answer.
#
#a) How many people lived in NYC in 2010?
print( row_total(2010, pop_data) )

#b) How many people lived in Brooklyn in 1970?

print( get_column('Brooklyn', pop_headers, pop_data) )

#c) What was the change in total population from 1900 to 2000?
print( row_total(2000, pop_data) - row_total(1900, pop_data ))

#d) What percentage of the total NYC population did Queens account for in 2010?
print(str(( get_column('Queens', pop_headers, pop_data)[22]/row_total(2010, pop_data))*100)+'%' )
#Because we have no function for a specific year and column by indexing into the year need

#e) Come up with your own question that can be answered using the population data.
#How many people lived in Manhattan in 1970?

#   What is the answer? (also the code to find your answer)
print( row_total(1970, pop_data) )

# End Problem 6
#==================================================
