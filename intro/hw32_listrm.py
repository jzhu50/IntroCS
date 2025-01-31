#Apples: Michelle Zhu, Aeneas Merchant
#IntroCS pd03 sec04
#HW32 -- pop, remove, del
#2023-05-02t
#time cost: 0.75

def sorted_list(nums):
    #returns a sorted list
    for i in range(len(nums)):
        min_num = i
        for n in range(i+1, len(nums)):
            if nums[n] < nums[min_num]:
                min_num = n
        nums[i], nums[min_num] = nums[min_num], nums[i]
    return nums

def med_list(nums):
    #returns the median of the numeric elements in list nums. Challenge: Write med_list() without using the Python function sorted(). E.g.,
    nums=sorted_list(nums)
    if len(nums)%2 == 0:
        first=nums[(len(nums)//2)-1]
        second=nums[len(nums)//2]
        med=(first+second)/2
    else:
        med=nums[(len(nums)//2)-1]
    return med

#"//" returns the quotient  

print(sorted_list([2,3,1,0]))
print(med_list([2,3,1,0,5]))
print(med_list([2,3,0,5]))


'''
def rm_negatives(L):
    #removes the negative numbers from list L, assumed to contain only numeric elements. Restrictions: Modifies L; does not create a new list. Does NOT use pop, remove, or del. E.g.,
    new_list=[]
    for i in L:
        if i >= 0:
            new_list.append(i)
    return new_list
'''

def rm_negatives(L):
    for i in L:
        if i <= 0:
            del L[i]
    return L
    
print(rm_negatives( [5,4,3,2,1] )) #→ [5,4,3,2,1]
print(rm_negatives( [5,-4,3,-2,1] )) #→ [5,3,1]

'''
As a duo, rewrite rm_negatives(L) using the built-in Python tools pop(), remove(), or del. Create block comment like this preceding definition:

POP
syntax:

# create a list of numbers
numbers = [1, 2, 3, 4, 5]

# remove and return the last element of the list
last_number = numbers.pop()

# print the last element and the modified list
print(last_number)  # 5
print(numbers)      # [1, 2, 3, 4]

# remove and return the element at index 1
second_number = numbers.pop(1)

# print the second element and the modified list
print(second_number)  # 2
print(numbers)        # [1, 3, 4]

behavior:
removes and returns the last element from a list
OR
removes and returns an element from a specific position (by index) in the list

REMOVE
syntax:

# create a list of colors
colors = ['red', 'green', 'blue', 'yellow', 'green']

# remove the first occurrence of 'green'
colors.remove('green')

# print the modified list
print(colors)  # ['red', 'blue', 'yellow', 'green']

# try to remove 'purple', which is not in the list
colors.remove('purple')  # raises a ValueError

behavior:
removes the first occurrence of a specified element from a list
AND
modifies the list in place so that the specified element is no longer in the list

DEL
syntax:

# create a list of numbers
numbers = [1, 2, 3, 4, 5]

# remove the element at index 2
del numbers[2]

# print the modified list
print(numbers)  # [1, 2, 4, 5]

# remove a slice of elements
del numbers[1:3]

# print the modified list
print(numbers)  # [1, 5]

# delete the entire list
del numbers

# try to print the list (raises a NameError)
print(numbers)

behavior:
removes an element
OR
slice from a list
OR
any mutable sequence object (e.g. tuple)

Apples prefers DEL for use in rm_negatives() because compared to DEL, the built-in functions REMOVE and POP have more restrictions. For example, POP removes and returns a specific element from the list by identifying its index, but it would take unnecessary steps to find the index. REMOVE only removes the first occurrence of a certain element from the list, which would be insufficient for removing more than one negative number in this case.
'''