#The People Who can't See the Board +1: Michelle Zhu, Shaw Edwards, Zachary Liu
#IntroCS pd03/s04
#Lab13 -- Pig Latin Translation Engine
#2023-05-01m

'''
PIG LATIN RULES:
1. Any word that begins with a vowel then add 'way' to the end.

       eg. apple  becomes appleway
           orange becomes orangeway

2. Otherwise, move the leading letters up to the first vowel to the end of the word then add 'ay'.

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
'''

def is_vowel(char):
    vowels = 'aeiouAEIOU'
    for i in char:
        if i in vowels:
            return True
    return False

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
    vowel_index = 0
    w = ''
    lower_case = ''
    if not is_vowel(word):
        w += word + 'ay' + ' '
        return w
    elif is_vowel(word[0]):
        w += word + 'way' + ' '
        return w
    else:
        for i in range(len(word)):
            if is_vowel(word[i]):
                vowel_index = i
                w += word[vowel_index:] + word[:vowel_index] + 'ay' + ' '
                if is_partially_cap(w):
                    w = w[0].upper() + w[1:len(w)]
                break #stops checking at first vowel
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
        if has_punctuation(word):
            punctuation = word[-1]
            word = piglatin_word(word) #-> "Atin?lay "
            word = word.replace(punctuation, "")
            word = word.replace(" ", punctuation)
        else:
            word = piglatin_word(word)
        piglatin_phrase += word
        phrase = piglatin_phrase
    return phrase

print(translate("What are the rules of Pig Latin?"))
# -> "Atwhay areway ethay ulesray ofway Igpay Atinlay?"
print(translate("the pope rocks red kicks"))
# -> "ethay opepay ocksray edray ickskay"
print(translate("zzz"))
# -> "zzzay"