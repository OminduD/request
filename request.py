import requests

y = 0
u = str(input('Enter Your URL:- '))
r = requests.post(u)
file = open('vws.txt', "w+")
r.text
file.write(r.text)
file.close()
print('Open to File Enter = 1')
y = int(input('Enter Your Number:- '))
if y==1:
    print(r.text)





