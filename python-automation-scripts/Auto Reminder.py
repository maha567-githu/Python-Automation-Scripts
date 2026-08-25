import time
while True:
    print("1.DRINK WATER")
    print("2.STUDY")
    print("3.TAKE BREAK")
    print("4.EXIT")
    choice=int(input("enter choice"))
    if choice==1:
        while True:
           print("Remainder : DRINK WATER")
           time.sleep(5)
           stop=input("PRESS Q TO STOP AND ENTER TO CONTINUE THE REMAINDER")
           if stop.upper()=="Q":
             break
    elif choice==2:
        while True:
          print("Remainder : STUDY") 
          time.sleep(5)
          exit=input("ente Q to stop and enter to continue")
          if exit.upper():
             break
          
    elif choice==3:
        while True:
          print("Remainder : TAKE BREAK")
          time.sleep(5)
          dur=input("enter h to continue and r to stop")
          if dur.lower()=="r":
             break
          elif dur.lower()=="h":
             continue
    elif choice==4:
        print("NICE TO MEET") 
        break 
    else:
        print("enter a valid choice")