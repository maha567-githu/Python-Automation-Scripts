import os
files=os.listdir("file_organizer/downloads")
print(os.getcwd())
for file in files:
# type check
  if file.endswith(".png") or file.endswith(".jpg"):
    print(file,"Images")
  elif file.endswith(".txt"):
    print(file,"Text")
  elif file.endswith(".pdf"):
    print(file,"PDF")
  elif file.endswith(".csv"):
    print(file,"CSV")  
# file avaialbe or not    
if not os.path.exists("file_organizer/downloads/Images")   : 
    os.mkdir("file_organizer/downloads/Images")             
if not os.path.exists("file_organizer/downloads/Text"):
  os.mkdir("file_organizer/downloads/Text")
if not os.path.exists("file_organizer/downloads/PDF") :
  os.mkdir("file_organizer/downloads/PDF")
if not os.path.exists("file_organizer/downloads/CSV"):
  os.mkdir("file_organizer/downloads/CSV")
 # MOVE
import shutil
for file in files:
  old_path="file_organizer/downloads/" + file
  if os.path.isdir(old_path):
    continue
  if file.endswith(".png") or file.endswith(".jpg"):
   new_path="file_organizer/downloads/Images/"+ file
  elif file.endswith(".txt"):
    new_path="file_organizer/downloads/Text/" + file
  elif file.endswith(".csv"):
    new_path="file_organizer/downloads/CSV/"+ file
  elif file.endswith(".pdf"):
    new_path="file_organizer/downloads/PDF/" + file  
  shutil.move(old_path,new_path)