# take in csv file as command line arguemnt convert to json and post to webapp
import sys
import csv
import json
import requests
import socket


ip_add = socket.gethostbyname(socket.gethostname())

def csv_to_json(file):
    diclist = []
    with open(file) as f:
        reader = csv.DictReader(f)
        for line in reader:
            diclist.append(line)
#            print(diclist)
            jlist = json.dumps(diclist)
    return jlist

def post_data(jlist):
    post = requests.post(
        "http://" + ip_add + ":8000/track_item/", data={'title' : 'ScriptAgain', 'data' : jlist}
        #'http://127.0.0.1'
    )
    print(post.ok)
    print(post.status_code)


if __name__ == "__main__":
    jlist = csv_to_json("./xm4-eBay.csv")
    print(jlist)
    post_data(jlist)
