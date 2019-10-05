#this is a Otp generation python program
import random
import time
string='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
random=random.sample(string,8)
otp=''
for i in random:
    otp=otp+str(i)
print "Your otp is :",otp
