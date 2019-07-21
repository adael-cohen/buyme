import pymysql


# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='users')

# Getting a cursor from Database
cursor = conn.cursor()

# # Getting all data from table “users”
# cursor.execute("SELECT * FROM users.players;")
#
# # Iterating table and printing all users
# for row in cursor:
#     print(row)
#
# cursor.close()
# conn.close()
#

conn.autocommit(True)

# Getting a cursor from Database
# cursor = conn.cursor()

# Inserting data into table
# cursor.execute("INSERT into users.players (id, name) VALUES (7, 'Moshe')")

# cursor.execute("DELETE FROM users.players WHERE id = 7 ")
cursor.execute("UPDATE users.players SET name='David' WHERE id = 4 ")

cursor.close()
conn.close()