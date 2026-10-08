import os

# select the directory whone content you want to list
directory_path = '/'

# use the os module to read the contents of the directory
content = os.listdir(directory_path)

# print the contents
print(content)