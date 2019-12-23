import requests
from bs4 import BeautifulSoup
import pandas

# @ ACCESING ZOMATO SITES
#Used headers/agent because the request was timed out and asking for an agent. 
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.zomato.com/bangalore/top-restaurants",headers=headers)

#@ Establish the connection
content = response.content
soup = BeautifulSoup(content,"html.parser")

#@ Find all HTML div tags (containg class)
top_rest = soup.find_all("div",attrs={"class": "bb0 collections-grid col-l-16"})
# print(top_rest)
list_tr = top_rest[0].find_all("div",attrs={"class": "col-s-8 col-l-1by3"})
# print(list_tr)

# @Extract the further intofoirmations
list_rest =[]
for tr in list_tr:
    dataframe ={}
    dataframe["rest_name"] = (tr.find("div",attrs={"class": "res_title zblack bold nowrap"})).text.replace('\n', ' ')
    dataframe["rest_address"] = (tr.find("div",attrs={"class": "nowrap grey-text fontsize5 ttupper"})).text.replace('\n', ' ')
    dataframe["cuisine_type"] = (tr.find("div",attrs={"class":"nowrap grey-text"})).text.replace('\n', ' ')
    list_rest.append(dataframe)
print(list_rest)

# @Save data into readable file (CSV file)
df = pandas.DataFrame(list_rest)
df.to_csv("zomato_res.csv",index=False)  # first create "data" folder in directory then run this"