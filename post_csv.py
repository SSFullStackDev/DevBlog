# take in csv file as command line arguemnt convert to json and post to webapp
import sys
import csv
import json
import requests


def csv_to_json(file):
    diclist = []
    with open(file) as f:
        reader = csv.DictReader(f)
        for line in reader:
            diclist.append(line)
            print(diclist)
            jlist = json.dumps(diclist)
    return jlist


def post_data(jdata):
    post = requests.post(
        "http://10.0.0.131:8000/admin/trackerapp/price_history/add/", json=jdata
    )
    print(post.ok)
    print(post.status_code)


if __name__ == "__main__":
    jlist2 = csv_to_json("./xm4-eBay.csv")
    post_data(jlist2)
