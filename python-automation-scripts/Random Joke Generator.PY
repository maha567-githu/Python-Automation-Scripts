import requests
 
while  True:
     print("1.GET RANDOM JOKE  ?")
     print("2.EXIT")
     Choice=int(input("enter choice"))
     if Choice==1:
         
         joke=requests.get("https://official-joke-api.appspot.com/random_joke")
         data=(joke.json())
         if joke.status_code==200:
          
          print(data['setup'])
          print(data['punchline'])
         else:
             print("FAILED TO FETCH JOKE")  
     elif  Choice==2:
         print("Enjoy")  
         break
     else:
         print("enter a valid choice")    
 

 
  