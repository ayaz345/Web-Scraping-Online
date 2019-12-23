{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "# @ ACCESING ZOMATO SITES\n",
    "#Used headers/agent because the request was timed out and asking for an agent. \n",
    "#Using following code we can fake the agent.\n",
    "headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}\n",
    "response = requests.get(\"https://www.zomato.com/bangalore/top-restaurants\",headers=headers)\n",
    "\n",
    "#@ Establish the connection\n",
    "content = response.content\n",
    "soup = BeautifulSoup(content,\"html.parser\")\n",
    "\n",
    "#@ Find all HTML div tags (containg class) \n",
    "top_rest = soup.find_all(\"div\",attrs={\"class\": \"bb0 collections-grid col-l-16\"})\n",
    "list_tr = top_rest[0].find_all(\"div\",attrs={\"class\": \"col-s-8 col-l-1by3\"})\n",
    "\n",
    "# @Extract the further intofoirmations\n",
    "list_rest =[]\n",
    "for tr in list_tr:\n",
    "    dataframe ={}\n",
    "    dataframe[\"rest_name\"] = (tr.find(\"div\",attrs={\"class\": \"res_title zblack bold nowrap\"})).text.replace('\\n', ' ')\n",
    "    dataframe[\"rest_address\"] = (tr.find(\"div\",attrs={\"class\": \"nowrap grey-text fontsize5 ttupper\"})).text.replace('\\n', ' ')\n",
    "    dataframe[\"cuisine_type\"] = (tr.find(\"div\",attrs={\"class\":\"nowrap grey-text\"})).text.replace('\\n', ' ')\n",
    "    list_rest.append(dataframe)\n",
    "print(list_rest)\n",
    "\n",
    "# Save data into readable file (CSV file)\n",
    "df = pandas.DataFrame(list_rest)\n",
    "df.to_csv(\"zomato_restaurant.csv\",index=False) df.to_csv("data/zomato_restaurant.csv",index=False) # first create "data" folder in directory thn run this"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
