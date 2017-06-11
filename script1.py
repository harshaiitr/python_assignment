import urllib.request
import os
import threading
#import _thread

content =open('links.txt').read().splitlines()
def func(url,q):

 
 #for i in content:
 response=urllib.request.urlopen(url)
 text=response.read().decode('utf-8')
 f=open("/home/harsha/harsha/download/"+str(q), "w+")
 f.write(text)
 f.close()
 f1=open("/home/harsha/harsha/download/"+str(q),"r")
 #print(f1.read())
 w=len(f1.read().split())
 
 print(w)
try:
 q=1
 for url in content:
  t=threading.Thread(target= func, args=(url,q,))
  q+=1 
  t.start()
  t.join()
except:
 print("Error:unable to start thread")












 

