import os

user=os.environ.get('USER')
passw=os.environ.get('PASSW')
fromaddr = os.environ.get('FROMADD')

print(user)
print(passw)
print(fromaddr)