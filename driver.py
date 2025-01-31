#Clyde 'Thluffy' Sinclair
#IntroCS pd00/s00
#HW20 -- Driver/Tester for Pig Latin Translation Engine
#2023-04-24m

import sys                               #facilitate reading CLI args

import oink                             #load translation engine


'''
USAGE:
Save this file to same dir as oink.py.

 ~ thonny ~
modify FILENAME assignment below, then run this file.
see output in bottom pane (shell).

 ~ terminal ~
run this command to see output flushed to terminal ("standard out"):
$ python3 THIS_FILE_NAME PATH/TO/INPUT_FILE

run this command to redirect output to a file:
$ python3 THIS_FILE_NAME PATH/TO/INPUT_FILE > PATH/TO/OUTPUT_FILE

'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#use exactly one (1) of the FILENAME assignment options shown below

#if running from Thonny, use this:
#FILENAME = PATH/TO/INPUT_FILE

#if running from terminal, use this instead:
FILENAME = sys.argv[1]                  #store command line arg
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


INPUT_STREAM = ""

with open(FILENAME, 'r') as infile:      #open file in read-only mode
    INPUT_STREAM = infile.read()         #store contents in var

print(oink.translate(INPUT_STREAM))
