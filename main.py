import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

print("""
	Welcome to the safe and secure,
	CubePasswordManager
	Type 'add' to add a new password
	Type 'passwords' to see all stored passwords
	""")
user_input = input()

cursor.execute("""CREATE TABLE IF NOT EXISTS passwordvault(
		ID text(30),
		website text(30),
		password text(30)
	)""")

conn.commit()

if user_input==('add'):
	username = input("Enter the username\n")
	website = input("Enter the website name\n")
	password = input("Enter the password")

	query = "INSERT INTO passwordvault (ID,website,password) VALUES (?,?,?)"
	query_values = (username,website,password)
	cursor.execute(query,query_values)
	conn.commit()
	conn.close()
else:
	cursor.execute("SELECT * FROM passwordvault")
	output = cursor.fetchall()
	for row in output:
		print(row)
	conn.commit()
	conn.close()
