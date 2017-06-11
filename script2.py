import requests
uname=input("enter username")
pword=input("enter password")
payload={'username':uname,'password':pword}
url='http://localhost/link-php/form1.php'
s=requests.session()
p=s.post(url,data=payload)

print(p.cookies)
print(p.text)
b=p.text
c=b.split()
d=c[len(c)-1]
if (d!="invalid"):
 
 link=input("link:")
 ck={'input1':link}
 sk={'username':uname}
 q=s.post('http://localhost/link-php/form2.php',data=ck)
# r=s.session('http://localhost/link-php/form2.php',data=sk)
 print(q.text)
 print(q.cookies)

