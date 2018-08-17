import csv

def getData(file):
    data = []
    with open(file + ".csv", 'rt') as data_file:
        reader = csv.reader(data_file, delimiter=',')
        for row in reader:
            data.append(row)
    print("Success")
    return data

def setData(path, data):
    with open(path + ".csv", "w", newline='') as data_file:
        writer = csv.writer(data_file, delimiter=',')
        for item in data:
            writer.writerow(item)
    print("Success")


