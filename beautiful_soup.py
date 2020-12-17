#web scraping

import requests 
from bs4 import BeautifulSoup 
  
URL = "https://d3c33hcgiwev3.cloudfront.net/_410e934e6553ac56409b2cb7096a44aa_SCC.txt?Expires=1607385600&Signature=A~RL4TbKaQ9JRR~f-R8l6G64yTHfporL2tQaqVNDJRhvE6JaR~Z4aX3VleQ7KZsuPzUkTJF0hTYf9ppCjlQ~pZLI2W5yXSo3vV~JP-FqBXEzD4vxBif~pO9pltFNPzIiIbdLKBHyBBn6YvpLplHOVgByxvs1RnUuGgyp7EAdM1A_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
a=str(soup.prettify())

string=a
string=string.replace('\n',',')[34:-17]

a=''
l=[]
for i in string:
    if(i==' '):
        l.append(int(a))
        a=''
    elif(i==','):
        pass
    else:
        a=a+i
l.append(int(a))

l1=[]
l2=[]
i=1
for j in l:
    if(i%2==1):
        l1.append(j)
    else:
        l2.append(j)
    i=i+1
    
import pandas as pd

dict_={'v1':l1,'v2':l2}
df = pd.DataFrame(dict_)
df.to_csv('scc.csv')