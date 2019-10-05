import pymysql
con=pymysql.connect('localhost','root','fedora'.'testing')
if (not con == None):
    print("Success in connection to DB")
con.close()
