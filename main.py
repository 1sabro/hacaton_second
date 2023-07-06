import requests
from bs4 import BeautifulSoup
import csv


with open('data.csv', 'w') as file:
    write_ = csv.writer(file)
    write_.writerow(['name', 'price_doll', 'price', 'url_img', 'inf'])


def write_to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'], data['price_doll'], data['price'], data['url_img'], data['inf']])

url = "https://www.mashina.kg/search/all/"
resposne = requests.get(url)
soup = BeautifulSoup(resposne.text, 'lxml')
all = soup.find('ul',class_="pagination").find_all('li')[-1]
result = all.find('a',class_ = 'page-link').get('href').split('=')[-1]


for count in range(int(result)):
    url = f"https://www.mashina.kg/search/all/?page={count}"

    resposne = requests.get(url)
    soup = BeautifulSoup(resposne.text, 'lxml')

    cars = soup.find_all("div", class_ = "list-item list-label")
    for i in cars:
        name = i.find("div", class_ = "block title").text.replace("\n","").strip()
        price = i.find("p").text.split()
        price = ''.join(price[3:])
        price_doll = i.find('p').find('strong').text.split()
        price_doll = ''.join(price_doll)
        inf = i.find("div", class_ = "block info-wrapper item-info-wrapper").text.split()
        inf = ''.join(inf)
        
        url_img = i.find("img").attrs.get('data-src')
        product_dict = {'name' : name, 
                        'price_doll' : price_doll, 
                        'price' : price, 
                        'url_img' : url_img, 
                        'inf' : inf
                        }
        write_to_csv(product_dict)

        


        




































# name = cars.find_all("span", class_ = "white font-big")
# print(name)


  
# data = soup.find("div", class_ = "col-lg-4 col-md-6 mb-4")

# name = data.find("h4", class_ = "card-title")

# price = data.find("h5")

# print(price.text)


# import requests
# from bs4 import BeautifulSoup

# url = "https://www.mashina.kg/search/all/"

# resposne = requests.get(url)
# soup = BeautifulSoup(resposne.text, 'lxml')

# cars = soup.find_all("div", class_ = "list-item list-label")
# for i in cars:
#     name = i.find("div", class_ = "block title").text.replace("\n","").strip()
#     price = i.find("strong").text.strip()
#     url_img = i.find("img").attrs.get('data-src').strip()


#     print(name + "\n" + price + "\n" + url_img + "\n\n")
