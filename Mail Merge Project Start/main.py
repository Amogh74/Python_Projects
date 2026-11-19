#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
 #---> The readlines() method returns a list containing each line in the file as a list item.
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    #----> The replace() method replaces a specified phrase with another specified phrase.
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        #---->The strip('e') method removes any leading, and trailing "e" char inside the string.

with open(r"./Input/Names/invited_names.txt") as file:
    invited_names = file.readlines()# returns list with every name in the line including the '\n'
    clean_names = [line.rstrip('\n') for line in invited_names] # this strips the '\n' leaving us with only names
#Now we have clean names , just need to make invited.txt inside output and replace [name]
with open("./Input/Letters/starting_letter.txt") as Main_File:
    Invite_letter = Main_File.read()

#now we have the invite file format , we just need to replace the [name] with an actual name
for names in clean_names:
    with open(f"./Output/ReadyToSend/{names}_Invited.txt", 'w') as new_file:
        updated_letter = Invite_letter.replace("[name]" , names )
        new_file.write(updated_letter)