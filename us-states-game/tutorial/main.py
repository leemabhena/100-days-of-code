import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = [int(temp[1]) for temp in data if temp[1].isnumeric()]
#     print(temperature)

# data = pandas.read_csv("weather_data.csv")
# print(data[data.temp == data.temp.max()])
gray, red, black = 0, 0, 0
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
for item in data['Primary Fur Color']:
    if item == 'Gray':
        gray += 1
    elif item == 'Cinnamon':
        red += 1
    elif item == "Black":
        black += 1

new_data = pandas.DataFrame(
    {
        'Fur Color': ['gray', 'red', 'black'],
        'Count': [gray, red, black],
    }
)

new_data.to_csv('squirrel_count.csv')

