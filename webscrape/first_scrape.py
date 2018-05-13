from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%204814%20601201888%20601203793%20601204369%20601296707%20601301599&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_1'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, 'w') #normal convention for file writter is f

header = "brand, product_name, shipping\n"

f.write("header")

for container in containers:
	brand = container.div.div.a.img["title"]
	
	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text
	
	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping_container: " + shipping)

	f.write(brand.replace(",", "|" ) + "," + product_name.replace(",", "|" ) + "," + shipping + "\n")

f.close()