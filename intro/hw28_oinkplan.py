#Michelle Zhu, Shaw Edwards, Zachary Liu
#The People Who Can't See the Board +1
#IntroCS pd03 sec04
#HW28 -- Pig Latin Translation Engine v0
#2023-04-26w

'''OINK OINK TAKEOVER BY 
Team 3 Oats: Leonna Wang, Eli Lifton, Kerick Espino
2023-04-26
time cost: 0.5

ALIGNMENT OF OUTLINE WITH CODE: 5/5
They clearly created and labeled the helper functions
Clear solution to operating punctuations

WOO-WOO:
* they used the built-in function .isalpha() to check for punctuations

HUH-WHA:
* how do we treat double "y" situations

MODS by us:
* we created new helper functions to check & add punctuations
'''

'''
PIG LATIN RULES:
1. If first letter is consonant, move all consonants before first vowel to the end and add "ay"
2. If first letter is vowel, add "way" to end of word
3. Retain the same capitalization and punctuation
4. Compound words have the same rules applied to each individual word
5. If there is only one "y" in the input, we treat "y" as a vowel; otherwise, we treat "y" as a consonant

SUMMARY OF APPROACH:
Make a list that contains vowels and a list that contains consonants
Check if the string input contains spaces, 1) if true: split the strings at the spaces & apply rules
2) if false:
Using a while loop, check if first letter is a vowel, if true: apply rule 2
Else go on checking the remaining letters and stop at the first vowel then apply rule 3

MODULARITY:
* KNOWN:
- slicing
- for loop
- if cascading
* UNKNOWN:

DISCOVERIES:
* punctuations should go at the end of output
* "y" is a vowel sound if there are no other vowels in the word

UNRESOLVED MYSTERIES:
* what if there are more than one "y"
* how to maintain the same capitalization
* how to avoid space before a punctuation

DEVELOPMENT LOG:
2023-04-26 1 hr
Michelle: marked up and commented on another team's code & revised our own code
Michelle: revised & added on
'''


def piglatin_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_index = 0
    if word[0].lower() in vowels:
        return word + 'way' + ' '
    else:
        for i in range(len(word)):
            if word[i].lower() in vowels:
                vowel_index = i
                break #stops checking at first vowel
        return word[vowel_index:] + word[:vowel_index] + 'ay' + ' '

def translate(phrase):
    piglatin_phrase=''
    word_list=phrase.split() #splits the phrase at space
    for word in word_list:
        punctuation=''
        if not word[-1].isalpha(): #checks if last index is an alphabetical letter
            punctuation=word[-1]
            word=word[:-1]
        piglatin_w = piglatin_word(word)
        piglatin_phrase += piglatin_w + punctuation + ''
        phrase = piglatin_phrase
    return phrase

print(translate("What are the rules of Pig Latin?"))
# -> "Atwhay areway ethay ulesray ofway Igpay Atinlay?"
print(translate("the pope rocks red kicks"))
# -> "ethay opepay ocksray edray ickskay"
