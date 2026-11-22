#TODO: How many Gray squirrels , how many black? How many cinnamon
import pandas as pd
# Squirrels = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261121.csv")
# sq_color = Squirrels["Primary Fur Color"]
# data = pd.Series(sq_color)
# counts = data.value_counts() #Gets count of every element . as we need all we directly can use counts
# # if we need to exclude some type of count then we can use:
# #for ex we need count of an element that is greater than 1 , ie repeated = counts[counts>1] , this will get us every single object with more than 1 count along with count number
# print(counts)
#
# final_data = pd.DataFrame(counts)
# final_data.to_csv("Final_Data.csv")

#Tr sol
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261121.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray" , "Red", "Black"],
    "Count" : ["gray_squirrels_count" ,"red_squirrels_count" , "black_squirrels_count" ]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")