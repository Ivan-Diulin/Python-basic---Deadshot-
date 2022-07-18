import csv

with open('sample.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for l in reader:
        print(l)

with open('sample.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['4', '5', '6'])

