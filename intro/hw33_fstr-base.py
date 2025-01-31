#3Slay: Linda Zheng, Krystal Khine, Michelle Zhu
#IntroCS pd03 sec04
#HW33 fstr-base
#2023-05-08
#time cost: 0.5

'''
DISCOVERIES:
* d tells python to format variable as an integer
* > forces the field to be right aligned
* < forces the field to be left aligned
* passing an integer after ':' causes field to be minimum # of character wide
* \t is used to line up column
* convert x to float(x) before using f
* f determines # of decimal points
* floating-point number is a type of numerical data in computing that represents a real number with a fractional part

UNRESOLVED MYSTERIES:
* what is the pattern of width?

FAVORITE FSTRING FEATURE:
* > width: aligns the columns
'''

def rgb_table(x):
    print(f'{"reg":>3}{"min[2]":>10}{"max[2]":>10}{"min[10]":>10}{"max[10]":>10}{"num[2]":>10}{"num[10]":>10}{"numRGB[10]":>12}') 
    for i in range(1, x+1):
        print(f'{i:>3}{i*"0":>10}{"1"*i:>10}{"0":>9}{2**i-1:>11}{10**i:>10}{2**i:>10}{8**i:>12}')
        
rgb_table(8)

'''

reg     min[2]    max[2]  min[10]    max[10]     num[2]  num[10]  numRGB[10]
  1          0         1        0          1         10        2           8
  2         00        11        0          3        100        4          64
  3        000       111        0          7       1000        8         512
  4       0000      1111        0         15      10000       16        4096
  5      00000     11111        0         31     100000       32       32768
  6     000000    111111        0         63    1000000       64      262144
  7    0000000   1111111        0        127   10000000      128     2097152
  8   00000000  11111111        0        255  100000000      256    16777216

'''