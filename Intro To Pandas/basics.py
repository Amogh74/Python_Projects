# with open("./weather_data.csv") as file:
#     data = file.readlines()
#     clean_data = [datas.rstrip("\n") for datas in data]
#
# print(clean_data)

#inbuilt library for csv
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)
# Look How much lines of code it took to extract 1 coloumn , hence pandas are used
import pandas as pd
# data = pd.read_csv("weather_data.csv")
#print(data)
#print(data["temp"])
#print(type(data))
# data_dict = data.to_dict()
# temperature = data["temp"].to_list()
# # Avg_temp = sum(temperature)/len(temperature)
# Avg_temp = data["temp"].mean()  # 2nd method
# Max_temp = data["temp"].max()
# # print(Max_temp)
# print(Avg_temp)


#Get Data in columns
# print(data["condition"])
# or
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Monday"])
# #challenge: print the row containing max temp
# print(data[data.temp == Max_temp])

#Accessing single data from the table
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]#this only fives the temp absolute value and other data is not shown
# monday_temp_Farenheit = monday_temp*9/5 + 32
# print(monday_temp_Farenheit)


#Create DataFrame From Scratch
data_dict = {
    "students" : ["Amy", "James" , "Angela"],
     "scores" : [76,56,65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
