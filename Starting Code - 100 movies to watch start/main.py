import requests
from bs4 import BeautifulSoup

# Write your code below this line 👇
response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com"
                      "/movies/features/""best-movies-2/")
web_html=response.text
soup=BeautifulSoup(web_html,"html.parser")
top_Gs=soup.find_all(name="h3",class_="title")
my_list=[movie.getText() for movie in top_Gs]
movie_list=my_list[::-1] # to reverse the list or
#or n in range(len(my_list)-1,-1,-1):# this comes from the cicle slice operator,slice(start:stop:step)
#   print(my_list[n])
with open("movie_list.txt",mode="w",encoding="utf8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
