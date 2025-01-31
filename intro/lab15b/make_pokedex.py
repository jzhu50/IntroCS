#! /usr/bin/python3

site = '''
<!DOCTYPE html>\n

<!-- Michelle Zhu
     IntroCS pd03 sec04
     Lab15b -- webpub
     2023-05-25
--> 

<html lang="en">
  <head>
    <meta charset="utf-8"/>

    <title>
      Pokemon!!!
    </title>
    
    <style>
    
    nav li {
      display: inline-block;
      position: relative;
    }
    nav li ul {
      display: none;
      position: absolute;
      width: 100px;
      top: 100%;
      padding: 0;

    }
    nav li:hover > ul {
      display: block;
      background-color: #9370db;
    }
    nav li:hover li{
      background-color: #9370db;
    }
    nav li > ul a{
      text-decoration: none;
      font-size: 20px;
      color: lightblue;
      padding: 5px;
    }
    nav > ul > li > a {
    border: 2px solid black;
    color: #F0E6EF;
    font-size: 30px;
    text-align: center;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Cardo&family=Nothing+You+Could+Do&display=swap');
      
    h1 {
        font-size: 45px;
        font-family: 'Nothing You Could Do',sans-serif;
        padding: 30px;
        text-align: center;
    }

    tr:hover {background-color: #D0A5C0;}

    th, td {
        border-bottom: 1px solid #ddd;
        margin: 30px;
        text-align: center;
        font-family: 'Cardo',sans-serif;
    }

    table {
        margin-left: auto;
        margin-right: auto;
    }
    
    body {
        background-color: #F6C0D0;
    }
    
    </style>

  </head>

  <body>
  <nav>
  <ul>
    <li><a href="./index.html">Home</a></li>
    <li><a href="#">Types</a>
      <ul>
        ?TYPES?
      </ul>
    </li>
    <li><a href="./pokesite/all_pokemon.html">All Pokemon</a></li>
    <li><a href="./pokesite/top10.html">Top10</a></li>
  </ul>
    </nav>
    ?SPECINFO?
    REPLACE_TABLE
  </body>
  
</html>'''

f = open("pokemon.csv")
text = f.read().strip()
lstv = text.split('\n')
headers = lstv[0].split(',')
for i in range(len(lstv)):
    lstv[i] = lstv[i].split(',')
lstv.pop(0)
data = lstv #creates a list containing sublists separated by '\n'
table = "<table>"
table += "<tr>"
table += "<th>Front image</th>\n"
table += "<th>Back image</th>\n"
for item in headers:
    table += f"<th>{item}</th>\n"
table += "</tr>\n"
for row in data: #for each sublist in list
    table+="<tr>"
    table+=f'\n<td><img src="../img/front/{row[0]}.png"></td>'
    table+=f'\n<td><img src="../img/back/{row[0]}.png"></td>\n'
    for item in row: #for each item in sublist
      table+=f"<td>{item}</td>\n"
    table+="</tr>\n"
table+="</table>"

def table_type(typ, specific):
  table = "<table>"
  for row in data:
    if row[2] == typ or row[3] == typ or int(row[0]) in specific:
        table += "<tr>"
        table += f'\n<td><img src="../img/front/{row[0]}.png"></td>'
        table += f'\n<td><img src="../img/back/{row[0]}.png"></td>\n'
        for item in row:
            table += f"<td>{item}</td>\n"
        table += "</tr>\n"
  table += "</table>"
  return table
types = [
    "Normal",
    "Fire",
    "Water",
    "Grass",
    "Electric",
    "Ice",
    "Fighting",
    "Poison",
    "Ground",
    "Flying",
    "Psychic",
    "Bug",
    "Rock",
    "Ghost",
    "Dragon",
    "Steel",
    "Fairy",
]

def gen_list(typez):
    typez_list = ''''''
    for i in typez:
        typez_list += f'''<li><a href="{i.lower()}.html">'''
        typez_list += f'''{i}'''
        typez_list += '''</a></li>'''
    return typez_list

site = site.replace("?TYPES?", gen_list(types))
all_pkmon = site.replace("REPLACE_TABLE", table)

#Make all_pokemon.html file
f = open("./pokesite/all_pokemon.html","w")
all_pkmon = site.replace("?SPECINFO?", "<h1>All Pokemon</h1>")
all_pkmon = all_pkmon.replace("REPLACE_TABLE", table)
f.write(all_pkmon)
f.close()
#Make index.html file
f = open("./pokesite/index.html","w")
indx = site.replace("REPLACE_TABLE", table_type("N/A",[7]))
indx = indx.replace("?SPECINFO?", "<h1>NO ME GUSTA POKEMON</h1>\n<h1>I like squirtle the best because it is very cute</h1>")
f.write(indx)
f.close()
#Make top10.html
f = open("./pokesite/top10.html","w")
top10 = site.replace("REPLACE_TABLE", table_type("",[7,12,25,39,94,133,143,145,149,151]))
top10 = top10.replace("?SPECINFO?", "<h1>Top 10 Pokemon</h1>\n<h1>These are the top 10 pokemon in my opinion based off mainly how cute they are!</h1>")
f.write(top10)
f.close()
for typ in types:
  f = open(f"./pokesite/{typ.lower()}.html","w")
  temp = site.replace("REPLACE_TABLE", table_type(typ,[-1])) #-1 indicates that this input is not used
  temp = temp.replace("?SPECINFO?", f"<h1>{typ} Pokemon</h1>")
  f.write(temp)
  f.close
  
print(site)