import pandas as pd

leadername = ['Stanisław', 'Jan', 'Jan', 'Grzegorz', 'Jan']
leadersurname = ['Żółkiewski', 'Chodkiewicz', 'Sobieski', 'Chodkiewicz', 'Chodkiewicz']
battle = ['Kłuszyn 4.VII.1610', 'Kircholm 27.IX.1605', 'Wiedeń 12.IX.1683 | Chocim 11.XI.1673','Czaśniki 26.I.1564','Biały Kamień 25.IX.1604']
btype = ['land battle']*5
no = ['old slavic','hebrew','hebrew','greek','hebrew']
title = ['hetman wielki koronny','hetman wielki litewski','król','hetman wielki litewski','hetman wielki litewski']

ln = pd.Series(leadername)
ls = pd.Series(leadersurname)
b = pd.Series(battle)
bt = pd.Series(btype)
o = pd.Series(no)
t = pd.Series(title)

data = pd.DataFrame({'Leader Name': ln, 'Leader Surname': ls, 'Battle': b, 'Battle type': bt,
                     'Name origin': o, 'Title':t})

#część 1 - dzielimy wiersz z dwoma bitwami na dwa
data['Battle'] = data['Battle'].str.split('|')
data = (data
 .set_index(['Leader Name','Leader Surname','Battle type','Name origin','Title'])['Battle']
 .apply(pd.Series)
 .stack()
 .reset_index()
 .drop('level_5', axis=1)
 .rename(columns={0:'Battle'}))

#część 2 - robimy z wyjściowej tabeli dwie, leaders i battle
leaders = data[['Leader Name', 'Leader Surname', 'Name origin', 'Title']]
leaders = leaders.drop_duplicates()
battle = data[['Battle type', 'Battle', 'Leader Name', 'Leader Surname']]

#część 3 - z tabeli leaders robimy dwie: leaders_2 i names
names = leaders[['Leader Name', 'Name origin']]
names = names.drop_duplicates()
leaders_2 = leaders[['Leader Name', 'Leader Surname', 'Title']]
print(battle)
print(leaders)
print(names)

#łączymy nowe tabele leaders_2 i names, otrzymując wcześniejszą tabelę leaders
new_leaders = pd.merge(leaders_2, names, on='Leader Name')
print(new_leaders)
