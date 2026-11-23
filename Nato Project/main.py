#List Comprehension
import random
numbers = [1,2,3]
new_numbers = [item + 1 for item in numbers]
print(new_numbers)

new_list = [num*2 for num in range(1,5)]
print(new_list)

names = ["Alex", "Beth" , "Caroline" ,"Dave", "Mike", "Eleanor","Freddie"]
new_name = [name for name in names if len(name)==4]
print(new_name)

capital_names = [name.upper() for name in names if len(name)>4]
print(capital_names)

#Dicitonary Ccomprehension
'''
syntax 1 : new_dict = {new_key:new_value for item in list}
syntax 2 : new_dict = {new_key:new_value for (key,value) in dict.items()} - creating a dict from another dict
'''
#Create a dictionary using names and giving them random marks

student_score = { name:random.randint(1,100) for name in names}
print(student_score)

#create passed students dictonary using previous dictonary
passed_students = { name:random_marks for (name , random_marks) in student_score.items() if random_marks>45}
print(passed_students)