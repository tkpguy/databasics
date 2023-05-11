import os

def clear_screen():
    os.system('cls')

clear_screen()

# Different usability of list
str_list = ['Facebook', 'Twitter', 'Microsoft']
num_list = [0,1,2,3,4,5,6,7,8,9]
mixed_list = [1008, 'Zoho', True, False, 108, 'HSVJ']
inr_list = ['Jaguar', [1,3,5,7,9], [True, False]]

#Displaying list values
print(f'\n\n\t{str_list}')
print(f'\n\t{num_list}')
print(f'\n\t{mixed_list}')
print(f'\n\t{inr_list}\n\n')

# Appending list items
str_list.append('Adobe')
num_list.append(10)
inr_list.append([12,24])
    # Display appended lists
print(f'\n DISPLAYING APPEDNED LIST: \n\t{str_list}')
print(f'\n\t{num_list}')
print(f'\n\t{mixed_list}')
print(f'\n\t{inr_list}\n\n')

# Replacing list item
str_list[1] = 'Cognizant'
inr_list[1][4]=0
    # Displaying the altered lists
print(f'\n DISPLAYING ALTERED LIST: \n\t{str_list}')
print(f'\n\t{inr_list}\n\n')

# Delete / Remove list items
inr_list[1].remove(0)
print(f'\n LIST VALUE AFTER DELETEING / REMOVING AN ITEM : \t{inr_list}\n\n')

#

