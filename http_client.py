import urllib.request

v= urllib.request.urlopen('https://api.github.com/users/vivianchenane')
print(v.read())
