import requests
import json
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
laughs_coconut = 'https://scrape-sm1.github.io/site1/COCA%2COLA0market1super.html'
glomark_coconut = 'https://glomark.lk/coca-cola-pet-2l/p/9613'



def compare_prices(product_laughs,product_glomark):
    
    result = requests.get(product_laughs)
    doc = BeautifulSoup(result.text,"html.parser")
    product_name_laughs = doc.find("div",{"class":"product-title"})
    print(product_name_laughs.text)
    price_laughs_text = doc.find("div",{"class":"price"})
    print(price_laughs_text)
    price_laughs=int(price_laughs_text.text)

    result2 = requests.get(product_glomark)
    doc2 = BeautifulSoup(result2.text,"html.parser")
    product_name_glomark = doc.find("div",{"class":"product-title"})
    print(product_name_glomark.text)
    price_glomark_text = doc.find("div",{"class":"price"})
    print(price_glomark_text)
    price_glomark=int(price_glomark_text.text)
    

    
    #print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    #print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    #if(price_laughs>price_glomark):
     #   print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    #elif(price_laughs<price_glomark):
     #   print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    #else:
     #   print('Price is the same')