from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = https://openlibrary.org/works/OL5798986W/PHP?edition=phpbeginnersguid00vasw
bookid=[] 
author=[] 
title=[] 
driver.get("<a href="https://openlibrary.org/works/OL5798986W/PHP?edition=phpbeginnersguid00vasw")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
bookid =a.find('div', attrs={'class':'_3wU53n'})
author=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
title =a.find('div', attrs={'class':'hGSR34 _2beYZw'})
bookid.append(name.text)
author.append(price.text)
title.append(rating.text)

driver =https://openlibrary.org/works/OL2649267W/C_programming?edition=
bookid=[] 
author=[] 
title=[] 
driver.get("<a href="https://openlibrary.org/works/OL2649267W/C_programming?edition=")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
bookid =a.find('div', attrs={'class':'_3wU53n'})
author=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
title =a.find('div', attrs={'class':'hGSR34 _2beYZw'})
bookid.append(name.text)
author.append(price.text)
title.append(rating.text)

driver = https://openlibrary.org/works/OL13756190W/Data_structures?edition=
bookid=[] 
author=[] 
title=[] 
driver.get("<a href="https://openlibrary.org/works/OL13756190W/Data_structures?edition=")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
bookid =a.find('div', attrs={'class':'_3wU53n'})
author=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
title =a.find('div', attrs={'class':'hGSR34 _2beYZw'})
bookid.append(name.text)
author.append(price.text)
title.append(rating.text)

driver = https://openlibrary.org/works/OL5798986W/PHP?edition=phpbeginnersguid00vasw
bookid=[] 
author=[] 
title=[] 
driver.get("<a href="https://openlibrary.org/works/OL5798986W/PHP?edition=phpbeginnersguid00vasw")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
bookid =a.find('div', attrs={'class':'_3wU53n'})
author=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
title =a.find('div', attrs={'class':'hGSR34 _2beYZw'})
bookid.append(name.text)
author.append(price.text)
title.append(rating.text)

driver =https://openlibrary.org/works/OL7008149W/Operating_systems?edition=
bookid=[] 
author=[] 
title=[] 
driver.get("<a href="https://openlibrary.org/works/OL7008149W/Operating_systems?edition=")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
bookid =a.find('div', attrs={'class':'_3wU53n'})
author=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
title =a.find('div', attrs={'class':'hGSR34 _2beYZw'})
bookid.append(name.text)
author.append(price.text)
title.append(rating.text)