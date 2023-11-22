import csv

with open("test.csv", 'r') as csv_file:
    data = list(csv.reader(csv_file))

print(data)

city_input = input("Please enter a city: ")
for row in data:
    if row[0].lower() == city_input.lower():
        print(f'the temperature in {row[0]} is {row[1]}')