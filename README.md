# Price Tracker Web App

This project started as a simple web scraper and has evloved into a price tracking webapp that will create and display an historical price history for a desired item. The webapp portion of this project is being built using the Python Django lib. Thes supporting scripts and files are present in the `price_tracker` dir. Within this dir there is an app named "trackerapp". This is where the database, files, and scripts for the webapp are.  

Once complete the webapp will allow you to enter the url of an item you would like to track, and return todays average, along with any price history that may be present. 

## Requirements and Installation Instructions

This project is built in python 3.8.3 using the Django 3.2.7 lib. The install instructions are written for a Linux based OS such as Ubuntu. 

### Installation: 

Ensure that the latest Python and Django versions are installed.

Clone repository to desired location, which will create a folder named `Price-Tracker-Web-App`. In this folder are the main python scripts that parse the data as well as the folders created by Django.

Open terminal, move to the `price_tracker` dir and run the following:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

These commands will allow the forms and database to be used. Next you will need to create a superuser

```
python3 manage.py createsuperuser
```
Follow the prompt to finish creating your superuser. You will need this info to access the admin page 

Finally all you need to do is start the server. Run the following:
```
python3 manage.py runserver 0.0.0.0:8000
```

The server and webapp are now up and running and can be accessed by entering the host computers IP address adding :8000 to the end. 



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

### test_file.py

The Test_File.py file will test each module in each of the scripts for future troubleshooting and debugging.
### test_file.py

The Test_File.py file will test each module in each of the scripts for future troubleshooting and debugging.
