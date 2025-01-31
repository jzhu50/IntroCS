#Michelle Zhu
#The People Who Can't See the Board +1
#IntroCS pd03 sec04
#HW27 -- Pig Latin Translation Engine v0
#2023-04-25t

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
* what if there are more than one "y"'s

DEVELOPMENT LOG:
2023-04-25 1 hour
Michelle Zhu: figured out how to translate single word into pig latin equivalent
'''

'''
def descriptive_name_of_piglatin_helper_fxn(arg0,arg1,...):
    """Return ."""
    return

# comment out
# your test cases
# after verifying each fxn works
'''

def translate(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_index = 0
    if word[0].lower() in vowels:
        return word + 'way'
    else:
        for i in range(len(word)):
            if word[i].lower() in vowels:
                vowel_index = i
                break #stop checking at the first vowel
        return word[vowel_index:] + word[:vowel_index] + 'ay'

print(translate("aha"))
print(translate("Goodnight"))
print(translate("pry")) #-> ypray

'''def translate(phrase):
    
    return phrase'''

#print(translate("What are the rules of Pig Latin?"))
# -> "Atwhay areway ethay ulesray ofway Igpay Atinlay?"
#print(translate("the pope rocks red kicks"))
# -> "ethay opepay ocksray edray ickskay"