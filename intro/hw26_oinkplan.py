#Michelle Zhu
#The People Who Can't See the Board +1
#IntroCS pd03 sec04
#HW26 -- Pig Latin Translation Engine Outline
#2023-04-24

'''
PIG LATIN RULES:
1. If first letter is consonant, move first letter to end and add "ay"
2. If first letter is vowel, add "way" to end of word
3. If word begins with multiple consonants, then move all consonants before first vowel to the end and add "ay"
4. Retain the same capitalization and punctuation
5. Compound words have the same rules applied to each individual word

SUMMARY OF APPROACH:
Make a list that contains vowels and a list that contains consonants
Check if the string input contains spaces, 1) if true: split the strings at the spaces & apply rules
2) if false:
Using a while loop, check if first letter is a vowel, if true: apply rule 2
Else go on checking the remaining letters and stop at the first vowel then apply rule 3

MODULARITY:
* KNOWN ::
- slicing
- while loop
- if cascading
- split built-in
* UNKNOWN ::

DEVELOPMENT LOG:
2023-04-24
Team: listed out the rules & figured out priority
2023-04-25

'''