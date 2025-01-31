#2Slays: Michelle Zhu, Prajusha Azeem
#IntroCS pd03/sec04
#HW40 -- dictionary
#2023-05-26
#time cost: 2
#consulted: Ben Goihman

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T1->T2
DISCOVERIES:
D: punctuations need to be removed
D: 

QUESTIONS/COMMENTS/CONCERNS:
Q:  
C:  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

#TASK:
#Write a loop that will add all of the words to the frequency tally.
#Words that do not exist will be added, while existing words will increase the count.

word_freq = {
        "Hello": 56,
        "at": 23,
        "test": 43,
        "this": 78
    }

words_to_add = ["test","Hello","fish","bacon","bacon","fish","at","bacon","bacon",
                "fish","kevin",'test',"Hello","fish","bacon","bacon","fish","at",
                "bacon","kevin","bacon","kevin","bacon"]

for item in words_to_add:
    if item in word_freq:
        word_freq[item] = word_freq[item]+1  #increments the value
    else:
        word_freq[item] = 1 #creates a new key and value pair
        
print(word_freq)


text = """
'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.

"Beware the Jabberwock, my son
The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
The frumious Bandersnatch!"

He took his vorpal sword in hand;
Long time the manxome foe he sought—
So rested he by the Tumtum tree,
And stood awhile in thought.

And, as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!

One, two! One, two! And through and through
The vorpal blade went snicker-snack!
He left it dead, and with its head
He went galumphing back.

"And hast thou slain the Jabberwock?
Come to my arms, my beamish boy!
O frabjous day! Callooh! Callay!"
He chortled in his joy.

'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.
"""

def tally_text(input_str):
    punctuations = [',', "'", ';', '!', ':', '"', '-',"."]
    add_words = input_str.strip().replace('\n',' ')
    add_words = add_words.split(' ')
    for i in range(len(add_words)):
        if add_words[i].isalpha() == False: #check if each sublist contains punctuations
            for j in add_words[i]:
                if j in punctuations:
                    add_words[i] = add_words[i].replace(j,"")
    for item in add_words:
        if item in word_freq:
            word_freq[item] = word_freq[item]+1  #increments the value
        else:
            word_freq[item] = 1
    return word_freq

print(tally_text(text))
