# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close() #python uses resources of my laptop until I close this file

#Sometimes we forget to add file.close so we can use
with open("my_file.txt",mode='r') as file:#mode is read only('r') by default(if we write mode in parenthesis )
    contents = file.read()
    print(contents)                         # mode - 'r' read only
                                            # mode - 'w' write only (replaces the previous text)
                                            #mode - 'a' append , writes just after the text inside the file
with open("my_file.txt",mode='a') as file: # in write mode if you dont have a file named inside the parenthesis
    file.write("NEW TEXT")                 # the interpretor will create one with that name and write into it .
