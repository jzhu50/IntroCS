#The People Who can't See the Board +1: Michelle Zhu, Shaw Edwards, Zachary Liu
#IntroCS pd03/s04
#HW28 -- Pig Latin Translation Engine v3
#2023-04-27r

'''CODE REVIEW SUMMARY
some of our rules are redundant
capitalization needs to be considered case by case
'''

'''
PIG LATIN RULES:
1. Any word that begins with a vowel then add 'way' to
       the end.

       eg. apple  becomes appleway
           orange becomes orangeway

    2. Otherwise, move the leading letters up to the first
       vowel to the end of the word then add 'ay'.

       eg. strong becomes ongstray
           program becomes ogrampray

    3. If there are no vowels in the word then add 'ay' to the end.

       eg. zzz becomes zzzay

    4. y is a vowel unless it begins a word.

       eg.  you becomes ouyay
            fly becomes yflay

    5. u is a vowel unless it is part of a qu combination.

       eg.  unique becomes uniqueway
            quiet  becomes ietquay

    6. Each word in a hyphenated word should be translated
       individually.

       eg.  semi-perimeter becomes emisay-erimeterpay

SUMMARY OF APPROACH:
Create helper functions is_partially_cap(word) & is_cap(letter)
Make a list that contains vowels
Split the phrase at space & apply piglatin_word(word)

MODULARITY:
* KNOWN ::
- slicing
- for loop
- if cascading
* UNKNOWN ::
- built-in function for capitalizing a letter

DISCOVERIES:
* we need more helper functions to check for vowels & caps

UNRESOLVED MYSTERIES:
* how does capitalization work?
* how to deal with the "y" situations?
* how to remove space before punctuation?

DEVELOPMENT LOG:
2023-04-27 1.5 hours
Michelle Zhu: created all helper functions & got the correct capitalizations
'''
    
def is_partially_cap(word):
    if word.isupper(): #checks if all letters are capitalized
        return False
    elif word.islower(): #checks if all letters are lower case
        return False
    else:
        return True
        
def is_cap(letter):
    if letter.isupper():
        return True
    else:
        return False
    
def has_punctuation(text):
    for char in text:
        if not char.isalpha(): #checks if text contains non-alphabetical letters
            return True
    return False
        
def piglatin_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_index = 0
    w = ''
    lower_case = ''
    if word[0].lower() in vowels:
        w += word + 'way' + ' '
        return w
    else:
        for i in range(len(word)):
            if word[i].lower() in vowels:
                vowel_index = i
                w += word[vowel_index:] + word[:vowel_index] + 'ay' + ' '
                break #stops checking at first vowel
        if is_partially_cap(w):
            w = w[0].upper() + w[1:]
        for letter in range(len(w)):
            if is_cap(w[0]):
                if is_cap(w[letter+1]):
                    lower_case += w[letter+1].lower()
                    w = w[:letter+1] + lower_case + w[letter+2:]
                    break #breaks the loop so that str does not go out of index
        return w

def translate(phrase):
    piglatin_phrase=''
    word_list=phrase.split() #splits the phrase at space
    for word in word_list:
        punctuation=''
        if not word[-1].isalpha(): #checks if last index is an alphabetical letter
            punctuation = word[-1]
            word = word[:-1]
        piglatin_phrase += piglatin_word(word) + punctuation
        phrase = piglatin_phrase
    return phrase

print(translate("What are the rules of Pig Latin?"))
# -> "Atwhay areway ethay ulesray ofway Igpay Atinlay?"
print(translate("the pope rocks red kicks"))
# -> "ethay opepay ocksray edray ickskay"