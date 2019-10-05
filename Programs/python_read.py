test=open("/etc/crontab",'r')
var=test.read()
print var
test.close()
