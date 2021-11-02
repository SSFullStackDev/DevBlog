# Price Tracker Web App

This project started as a simple web scraper and has evloved into a price tracking webapp that will create and display an historical price history for a desired item. The webapp portion of this project is being built using the Python Django lib. Thes supporting scripts and files are present in the `price_tracker` dir. Within this dir there is an app named "trackerapp". This is where the database, files, and scripts for the webapp are.  

Once complete the webapp will allow you to enter the url of an item you would like to track, and return todays average, along with any price history that may be present. 


## Usage

### ebayscraper.py

The main script `ebayscraper.py` takes in an ebay item search url as a command line argument. It then calculates the average item price that day.  Results are saved or amended (if exists) to a CSV file.

```
$ python ebayscraper.py https://www.ebay.com/<search_url>
```

### pricechartgenerator.py

The `pricechartgenerator.py` script takes in the info from the csv file and creates a simple line graph to show the change in price over time.

```
$ python pricechartgenerator.py <csv_file>
```

### post_data.py

**TODO**

The post_data.py script reads the info in the csv and then posts the data to the webapp. This script is not yet working correctly

### test_file.py

The Test_File.py file will test each module in each of the scripts for future troubleshooting and debugging.
