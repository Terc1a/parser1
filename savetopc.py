import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}
for count in range(1, 8):
    response = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_="card mt-4 my-4")
    for i in data:
        card_url = "https://scrapingclub.com" + i.find("a").get("href")
    
    
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")



            #name = i.find("h4", class_="card-title").text.replace("\n","")
            #price = i.find("h5").text
            #url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
            
        #print(name + "\n" + price + "\n" + url_img + "\n\n")

    



url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
img_data = requests.get(url_img).content
with open('images/'+ input() +'.jpg', 'wb') as handler:

       handler.write(img_data)