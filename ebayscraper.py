#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
import requests
import os
import csv
import datetime
import sys

path = os.getcwd()


def scrapeWebsite(
    search_url="""https://www.ebay.com/sch/i.html?_from=R40&_nkw=xm4&_sacat=0&_sop=1&LH_
    ItemCondition=1500%7C2000%7C2500%7C3000%7C1000&rt=nc&LH_BO=1""",
):
    """Take in a URL and create a list of prices from search)"""

    source = requests.get(search_url)
    """source.text and html.parser instead of source and html need to look at bs docs"""
    soup = bs(source.text, "html.parser")
    priceList = []

    for item in soup.find_all("div", class_="s-item__info clearfix"):
        price = item.find("span", class_="s-item__price")

        try:
            price = float(price.text[1:].replace(",", ""))
            priceList.append(price)

        except AttributeError:
            pass
        except ValueError:
            print(price.text[1:])
    # print(priceList)
    # print(soup.title.text)

    return priceList, soup


def calculateAverage(priceList):
    # Calculate the average price for the item
    total = 0
    for x in priceList:
        total += x
        average = total / len(priceList)
    return average


def create_entry(average):
    # Create header and data entry for csv file
    csv_header = ["date", "price"]
    csv_entry = [str(datetime.date.today()), average]
    return csv_header, csv_entry


def writeData(soup, csv_header, csv_entry):
    # Parse title from soup for file name
    filename = soup.title.text.replace(" | ", "-")

    # check if filename exists and create one if not, then write data to file
    if not os.path.exists(path + "/" + filename + ".csv"):
        with open(path + "/" + filename + ".csv", "w") as history:
            writer = csv.writer(history)
            print(writer.writerow(csv_header))
            print(writer.writerow(csv_entry))

    # Check if data entry is already in CSV, write entry if not
    else:
        with open(path + "/" + filename + ".csv", "r+") as history:
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


def main():
    """
    Main Function takes command line argument and scrapes info
    """
    try:
        priceList, soup = scrapeWebsite(sys.argv[1])
    except IndexError:
        priceList, soup = scrapeWebsite()
    average = calculateAverage(priceList)
    csv_header, csv_entry = create_entry(average)
    writeData(soup, csv_header, csv_entry)


if __name__ == "__main__":
    main()


""" DONE Get average price/day save to a csv 
         create graph from csv
    DONE use functions
         Testing file    
         Set email alerts for price drops 
    DONE create functions with ability to input parameters for search 
         Build Gui for parameter input and graphs 
         Android App
    """
