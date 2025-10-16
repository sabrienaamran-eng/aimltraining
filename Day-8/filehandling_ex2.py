import os
# file_path=r'C:\Users\sabri\OneDrive\Desktop\AIML\Day-8\ourfiles\sample.txt'
filepath=os.getcwd()
filename=input('Enter File Name to Update File:\t')
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,'a')
    content=input('Enter text to write in file \t')
    file.write(content)
    print(f'File{filename} updated')
    file.close()
else:
    print(f'No such file{filename}exist')