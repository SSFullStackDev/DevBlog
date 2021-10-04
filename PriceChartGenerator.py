from matplotlib import pyplot as plt
import csv
import os


plt.set_loglevel("WARNING")


def create_graph(csv_file):
    xaxis = []
    yaxis = []
    path = os.getcwd()
    with open(os.path.join(path, csv_file + ".csv")) as f:
        reader = csv.DictReader(f)
        for row in reader:
            xaxis.append(row["date"])
            yaxis.append(float(row["price"]))
    # print(xaxis)
    # print(yaxis)
    plt.plot(xaxis, yaxis)
    plt.show()
