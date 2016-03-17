import MySQLdb

db = MySQLdb.connect(host="10.19.251.50",    # your host, usually localhost
                     user="root",         # your username
                     passwd="sxcloud",  # your password
                     db="test")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM heat_map limit 10")

# print all the first cell of all the rows
#for row in cur.fetchall():
#    print row[0],row[1],int(row[2])
entries = cur.fetchall()
if entries:
	print "it's not empty"
	for row in entries:
	    print row[0],row[1],int(row[2])
else:
	print "empty"

db.close()