# import os
# file_path=r'C:\Users\sabri\OneDrive\Desktop\AIML\Day-8\ourfiles\sample.txt'
# file=open(file_path,'w')
# content=input('Enter text to write in file \t')
# file.write(content)
# file.close()

#UNTUK CREATE FILES DALAM FOLDER
# import os
# # file_path=r'C:\Users\sabri\OneDrive\Desktop\AIML\Day-8\ourfiles\sample.txt'
# filepath='C:\\Users\\sabri\\OneDrive\\Desktop\\AIML\\Day-8\\ourfiles'
# filename=input('Enter File Name to Create File:\t')
# fullpath=os.path.join(filepath,filename)
# file=open(fullpath,'w')
# content=input('Enter text to write in file \t')
# file.write(content)
# print(f'File{filename} create at{fullpath} and content saved in file')
# file.close()

#UNTUK CREATE FILES OUTSIDE FOLDER
import os
# file_path=r'C:\Users\sabri\OneDrive\Desktop\AIML\Day-8\ourfiles\sample.txt'
filepath=os.getcwd()
filename=input('Enter File Name to Create File:\t')
fullpath=os.path.join(filepath,filename)
file=open(fullpath,'w')
content=input('Enter text to write in file \t')
file.write(content)
print(f'File{filename} create at{fullpath} and content saved in file')
file.close()