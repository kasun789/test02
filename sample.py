from bs4 import BeautifulSoup
import requests

url1 = "https://glomark.lk/my-lemon-1000ml/p/99457"
url2 = "https://www.newegg.ca/eclipse-gray-asus-rog-zephyrus-g15-ga503qm-bs94q-gaming/p/1TS-001A-05M75"
result = requests.get(url1)
doc = BeautifulSoup(result.text,"html.parser")

#prices = doc.find_all(text="$")
#parent = prices[0].parent
#strong = parent.find("strong")
#pri1 = int(str(strong.string))
doc = (doc.find_all('span',attrs={'class':'price'}))
print(doc)


result2 = requests.get(url2)
doc2 = BeautifulSoup(result2.text,"html.parser")

prices2 = doc2.find_all(text="$")
parent2 = prices2[0].parent
strong2 = parent2.find("strong")
pri2 = int(str(strong2.string))

if pri1==pri2:
    print("same")


