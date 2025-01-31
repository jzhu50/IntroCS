#loop over list to generate dropdown...

for i in range(5):
    VARIABLE = "Monster"+str(i)
    print('''<li><a href="./'''+VARIABLE+'''.html">'''+VARIABLE+'''</a></li>''' )
    