"""import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempreture = []
    for row in data:
        if row[1] != "temp":
            tempreture.append(row[1])
    print(tempreture)"""

import pandas as p
data = p.read_csv("weather_data.csv")
#print(type(data))
#print(type(data["temp"]))

#data_dict = data["temp"].max()
#print(data_dict)
#print(sum(data_dict)/len((data_dict)))
#print(data_dict)
#print(data["condition"])
#data.Condition
#print(data[data.temp == max(data["temp"])])
data_temp= data[data.day == "Monday"]
monday_temp = data_temp.temp[0]
farahniet= monday_temp * 1.8 + 32

print(farahniet)