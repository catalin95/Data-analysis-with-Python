# Simple connection to a MySQL database, define some simple methods for manipulating the database

import mysql.connector

mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'password',
	database = 'database'	# optional, to tell python which database to initialize 
	)



def execute_sql(object, query):

	try:
		object = mydb.cursor()

	except:
		print ("Coudn't create a connection using cursor %r" %object)

	try:
		object.execute(query)

	except:
		print ("Coudn't execute the query, please make sure you entered a string or a valid SQL command")

	finally:
		
		for line in object:
			print (line)
		
		mydb.close()




