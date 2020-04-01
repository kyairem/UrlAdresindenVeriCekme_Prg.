#! /bin/python3 

import requests 
from bs4 import BeautifulSoup

#url="https://www.imdb.com/title/tt0111161/?ref_=adv_li_tt"
url="http://www.imdb.com/chart/top"
r=requests.get(url)
soup = BeautifulSoup(r.content,"html.parser") 
gelen_veri=soup.find_all("table",{"class":"chart full-width"}) 
#tablo=(gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
#tablo=tablo.find_all("tr")
#for i in tablo:
#	print(i)

print(len(gelen_veri))

tablo=(gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
tablo=tablo.find_all("tr")
for i in tablo:
	baslikler=i.find_all("td",{"class":"titleColumn"})
	film_ismi=baslikler[0].text
	film_ismi=film_ismi.replace("\n","")
	print(film_ismi)
	print("*********************************")
