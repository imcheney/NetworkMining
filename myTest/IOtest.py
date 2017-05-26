import csv
DATA_PATH = r'/Users/Chen/Desktop/计算社会学/largeDataset/data/edges10000.csv'

with open(DATA_PATH, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # row is a list-type
        print(row[0])
        print(row[1])

if __name__ == "__main__":
    print("hello")