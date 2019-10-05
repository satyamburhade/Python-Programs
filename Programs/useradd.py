def add(userName, pasword):
	import os
	os.system("useradd -d /home/%s  -m -p %s %s"%(userName, pasword, userName))
