
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

# declare the page variable and store requests.get(url)
page=requests.get(url)
#craete the soup variable and put bs object in it => bs(page.text,'html.parser')
soup=bs(page.text,"html.parser")
#craete variable star_table and use soup.find_all to get all table
star_table=soup.find_all("table")
print(len(star_table))


temp_list= []
table_rows = star_table[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)


#Create empty lists for Star_names ,Distance ,Mass ,Radius 
Star_names=[]
Distance=[]
Mass=[]
Radius=[]

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)
# convert df2 to csv
df2.to_csv("dwarf_stars.csv")
