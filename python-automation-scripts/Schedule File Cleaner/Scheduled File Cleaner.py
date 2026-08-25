import schedule
import time
from pathlib import Path
def clean_folder():
    print("checking folder....")
    Temp=Path("Schedule File Cleaner/temp")
    if Temp.exists():
     for i in Temp.iterdir():
          print(i)
          if i.suffix==".tmp":
                print(f"found : {i.name}")
                i.unlink()
                print(f"deleted : {i.name}")
          
schedule.every(5).seconds.do(clean_folder)
while True:
        schedule.run_pending()
        time.sleep(1)
        
