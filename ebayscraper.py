from bs4 import BeautifulSoup as bs
import requests
import os
import csv
import datetime

path = os.getcwd()
source = requests.get(
    "https://www.ebay.com/sch/i.html?_from=R40&_nkw=xm4&_sacat=0&_sop=1&LH_ItemCondition=1500%7C2000%7C2500%7C3000%7C1000&rt=nc&LH_BO=1"
)
"""source.text and html.parser instead of source and html need to look at bs docs"""
soup = bs(source.text, "html.parser")
priceList = []
total = 0

for item in soup.find_all("div", class_="s-item__info clearfix"):
    price = item.find("span", class_="s-item__price")
    try:
        price = float(price.text[1:])
        priceList.append(price)

    except AttributeError:
        continue
# Calculate the average price for the item
for x in priceList:
    total += x
average = total / len(priceList)

# Create header and data entry for csv file
csv_header = ["date", "price"]
csv_entry = [str(datetime.date.today()), average]

# Parse title from soup for file name
a = soup.title.text.find(" | ")
b = soup.title.text[:a] + "-" + soup.title.text[a + 3 :]

# check if filename exists and create one if not, then write data to file
if not os.path.exists(path + "/" + b + ".csv"):
    with open(path + "/" + b + ".csv", "w") as history:
        writer = csv.writer(history)
        print(writer.writerow(csv_header))
        print(writer.writerow(csv_entry))

# Check if data entry is already in CSV, write entry if not
else:
    with open(path + "/" + b + ".csv", "r+") as history:
        reader = csv.reader(history)
        writer = csv.writer(history)
        present = False
        print(csv_entry[0])
        for line in reader:
            if csv_entry[0] in line:
                print("DATA ALREADY ENTERED")
                present = True
        if present != True:
            writer.writerow(csv_entry)

"""DONE Get average price/day save to a csv 
        create graph from csv
        use functions
        Testing file    
        Set email alerts for price drops 
        create functions with ability to imput parameters for search 
        Build Gui for parameter input and graphs 
        Android App
    """
