from pathlib import Path
import shutil
from datetime import datetime
import os
print(os.getcwd())
Source=Path("Daily Backup Script/source")
if Source.exists():
    print("folder found")
else:
    print("folder not found")    
today=datetime.now().strftime("%d-%m-%y")
backupfolder=Path("Daily Backup Script")/f"source_backup{today}"
print(backupfolder) 
backupfolder.mkdir(exist_ok=True)
for i in Source.iterdir():
    print(i)
    shutil.copy2(i,backupfolder/i.name)    