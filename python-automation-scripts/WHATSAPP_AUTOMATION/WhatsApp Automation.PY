import pandas as pd
import pywhatkit
import pyautogui
import time
contacts=pd.read_excel("WHATSAPP_AUTOMATION/CONTACTS.XLSX")
print(contacts)
for index,row in contacts.iterrows():
    name=row["Name"]
    number=str(row["Number"])
    if not number .startswith("+"):
        number ="+"+ number
    
    message=row["Message"]
    print("MESSAGE SENDING....")
pywhatkit.sendwhatmsg_instantly(number ,
                      message,
                      wait_time=20)
time.sleep(3)
pyautogui.press("enter")
print("message sent")    