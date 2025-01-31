#Michelle Zhu
#IntroCS pd03 sec04
#HW25 -- List Algos
#2023-04-04
#time cost: 1
#consulted: chatgpt

def min_val(liszt):
    #accepts a list and returns its least value. E.g.,
    min = liszt[0] #initialze min to the first element in the list
    i = 1 #initialize i to the second element in the list
    while i < len(liszt):
        if min > liszt[i]:
            min = liszt[i]
        i += 1
    return min

'''def min_val(liszt):
    ret_val = liszt[0]
    for val in liszt:
        if(val<ret_val):
            ret_val=val
    return ret_val'''

'''for loop visits and checks every value in the list, which makes it better than a while loop in this case'''

print(min_val( [3] )) #-> 3
print(min_val( [5,4,3,2,1] )) #-> 1
print(min_val( ["free", "fee","phi","pho","phum","Free", "Fee","Phi","Pho","Phum",] )) #-> Fee
#related to the ascii value

def list_find(liszt, q):
    #takes a list liszt and a query q as inputs, and returns the first index where the query occurs in the list. Returns -1 if query not found. E.g.,
    i = 0
    while i < len(liszt):
        if liszt[i] == q:
            return i
        i += 1
    return -1 #we want to return -1 b/c it keeps the output a number

'''def list_find(liszt, q):
    ret_pos = -1
    for i in range(len(liszt)):
        if (liszt[i]==1):
            return i
    return ret_pos'''

print(list_find( [5,4,3,2,1], 2 )) #-> 3
print(list_find( [5,4,3,2,1], 6 )) #-> -1
print(list_find( [5,4,'cat','dog','cat'], 'cat' )) #-> 2

'''the rightmost index is len(liszt)-1'''

def min_pos(liszt):
    #takes a list containing only numeric elements and returns the position (index) of the least value. E.g.,
    return list_find(liszt, min_val(liszt))

'''def min_pos(liszt):
    if ( len(liszt) < 1 ):
        return -1
    minpos = 0
    for i in range(len(liszt)):
        if ( liszt[i] < liszt[minpos] ):
            minpos = i
    return minpos'''
    
print(min_pos( [3] )) #-> 0
print(min_pos( [5,4,3,2,1] )) #-> 4
print(min_pos( [2,1,3] )) #-> 1
