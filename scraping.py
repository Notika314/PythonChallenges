import requests
import csv
from bs4 import BeautifulSoup

response = requests.get('https://www.thriftbooks.com/w/effective-python-90-specific-ways-to-write-better-python_brett-slatkin/26566163/?resultid=3525a313-64d9-4294-8604-27958a00d283#edition=21451970&idiq=35394394')
soup = BeautifulSoup(response.text, 'html.parser')


price = soup.find("span",{"class": "price"}).text
condition = soup.find_all(lambda tag: tag.name == "p" and "Condition" in tag.text)[0].text.split(": ")[1]
details = soup.find_all("div", {"class": "WorkMeta-detailsRow"})
for detail in details:
    if ("ISBN13" in detail.text):
        isbn13=detail.text.split(":")[1]
    elif ("Publisher" in detail.text):
        publisher=detail.text.split(":")[1]
    elif ("Release Date" in detail.text):
        release_date=detail.text.split(":")[1]
    elif ("Length" in detail.text):
        pages=detail.text.split(":")[1].split(" ")[0]
    elif ("Dimensions" in detail.text):
        dims=detail.text.split(":")[1]        
depth,width,height=dims.split("x")

print(price,condition,isbn13,publisher,release_date)

"""Saving data to CSV file"""

header_row=["ISBN13","Publisher","Release Date","Price","Pages","Depth","Width","Height","Condition"]
data=[isbn13,publisher,release_date,price,pages,depth,width,height,condition]

with open('./data_scraping/bookinfo.csv', 'w', encoding='UTF8', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(header_row)
    writer.writerow(data)
    
    new_file.close()
    
print("Thank you for your time")