#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
    
# Declaring Placeholder as constant
PLACE_HOLDER = "[name]"

invited_guests = []

# Reading Invited People txt file
with open("./Input/Names/invited_names.txt", "r") as invited_guests_file:
    invited_people = invited_guests_file.readlines()

# Performing necessary cleaning of Invited People Names
for name in invited_people:
    invited_guests.append(name.strip())
    
# Reading Letter and replacing the place holder for every guest and saving it to ReadyToSend Folder
for name in invited_guests:
    letter = open("./Input/Letters/starting_letter.txt", "r")
    letter_context = letter.read() # Fetching Letter content
    guest_letter = letter_context.replace(PLACE_HOLDER, name) # Replace Placeholder with name
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as invitation_letter: # Create customised letter
        invitation_letter.write(guest_letter)