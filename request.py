import requests
y = 1
while y == 1:
    u = str(input('Enter Your URL:- '))
    d = str(input('Enter Your File Name:- '))
    t = '.txt'
    a = d+t
    r = requests.post(u)
    file = open(a, "w+")
    r.text
    file.write(r.text)
    file.close()
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('''
Enter to New URL    = 1
Open to File Enter  = 2
''')
    y = int(input('Enter Your Number:- '))
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
if y == 2:
    print(r.text)



