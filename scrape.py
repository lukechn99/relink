from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd
# Find the URL that you want to scrape
# Inspecting the Page
# Find the data you want to extract
# Write the code
# Run the code and extract the data
# Store the data in the required format

# this configures the web driver to work with Chrome, but eventually 
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

#driver.get() # get(URL)
links = []

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

#def getLinks (url):
#    driver.get(url)