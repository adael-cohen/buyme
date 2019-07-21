import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='LYRBBuhqUC', passwd='T2pT14VYOd', db='LYRBBuhqUC')

cursor = conn.cursor()

conn.autocommit(True)
# 2
cursor.execute("INSERT into LYRBBuhqUC.dogs (names, age, breed) VALUES ('Max', 3, 'Bulldog')")
cursor.execute("INSERT into LYRBBuhqUC.dogs (names, age, breed) VALUES ('Coco', 2, 'poodle')")
cursor.execute("INSERT into LYRBBuhqUC.dogs (names, age, breed) VALUES ('Rudy', 4, 'Labrador')")
# 3
cursor.execute("UPDATE LYRBBuhqUC.dogs SET age=6 WHERE names='Coco' ")
# 4
cursor.execute("DELETE from LYRBBuhqUC.dogs WHERE names='Rudy' ")
# 5
cursor.execute("SELECT * FROM LYRBBuhqUC.dogs;")
for row in cursor:
    print(row)

cursor.close()
conn.close()
