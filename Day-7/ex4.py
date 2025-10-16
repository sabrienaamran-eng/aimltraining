# import os
# # import inspect
# print ('Current Directory',os.getcwd())

# functions=inspect.getmembers(os,inspect.isbuiltin)

# print('All Function in math module')
# for n, func in functions:
#     print(n)

# create a folder inside current directory using python

# import os
# cdir=os.getcwd()
# folder_name=input('Enter Folder Name to Create:\t')
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print('Folder Already Exist')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f'{folder_name} created at {folder_path}')

# Rename a folder
# os.rename(folder_name, "renamed_folder")
# write code to rename a folder
# you will take folderName from user
# if it is exist, you will ask new name and rename it

import os
cdir=os.getcwd()
folder_name=input('Enter Folder Name to Create:\t')
folder_path=os.path.join(cdir,folder_name)
os.makedirs(folder_path,exist_ok=True)
print(f'{folder_name} created at {folder_path}')

renamed_folder=input('Enter New Folder Name:\t')
new_folder_path=os.path.join(cdir,renamed_folder)
os.rename(folder_path,new_folder_path)
print(f'Folder renamed to "{renamed_folder}" at {new_folder_path}')

