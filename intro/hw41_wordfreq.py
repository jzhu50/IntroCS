#Child Passenger: Michelle Zhu, Han Xiao
#IntroCS pd03/sec04
#HW41 -- punctuations
#2023-05-30
#time cost: .5

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T2 -> T3
DISCOVERIES:
D: double (or multiple consecutive) punctuation issues can be fixed in the beginning by .replace() with a space
D: 

QUESTIONS/COMMENTS/CONCERNS:
Q:  
C:  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


text = '''
Call me Ishmael. Some years ago--never mind how long precisely--having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off--then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.
'''

word_freq = {}

def tally_text(input_str):
    punctuations = [',', "'", ';', '!', ':', '"', '-',"."]
    add_words = input_str.strip().replace('\n',' ')
    add_words = add_words.replace('--', ' ')
    add_words = add_words.split(' ')
    for i in range(len(add_words)):
        if add_words[i].isalpha() == False: #checks if each sublist contains punctuations
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