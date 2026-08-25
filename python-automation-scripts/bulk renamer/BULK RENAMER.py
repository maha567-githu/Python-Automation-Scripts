print("__________BULK FILE RENMAER___________")
import os
print(os.getcwd())
files=os.listdir("photos")
print(files)
for file in files:
    print(file)

count=1
for file in files:
    old_name="photos/" + file
    new_name="photos/image" + str(count) + ".jpg"
    os.rename(old_name,new_name)
    count+=1
print("ALL FILES RENAMED SUCCESSFULLY")