import pandas as pan

data = pan.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirrel_count)
print(black_squirrel_count)
print(red_squirrel_count)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count":[gray_squirrel_count,red_squirrel_count,black_squirrel_count]
}

df = pan.DataFrame(data_dict)

df.to_csv("Squirrel_data.csv")