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
