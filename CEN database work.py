import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="elizabeth",
    database="cen434_database",
)

mycursor = db.cursor()

#create a database
mycursor.execute("CREATE DATABASE cen434_database")

#create a table
mycursor.execute("CREATE TABLE students (studentName VARCHAR(50), matricNumber VARCHAR(10), studentHall VARCHAR(20), studentProgram VARCHAR(50))")

#creating a sample data
sqlform = "INSERT INTO students (studentName, matricNumber, studentHall, studentProgram) VALUES (%s, %s, %s, %s)"
studentInfo = [("David", "20CJ027411", "Daniel", "Computer Engineering"), ("Wisdom", "20AA025746", "John", "Architecture"), ("Sophie", "20BB023465", "Dorcas", "Mass Communication"), ]

mycursor.executemany(sqlform, studentInfo)
db.commit()

#read the data
mycursor.execute("SELECT * FROM students")

for x in mycursor:
    print(x)

#write the data
mycursor.execute("INSERT INTO students (studentName, matricNumber, studentHall, studentProgram) VALUES (%s, %s, %s, %s)", ("Joshua", "20CM027885", "Daniel", "Mechanical Engineering"))
db.commit()

#update data in the table
mycursor.execute("UPDATE students SET studentProgram = 'Building Technology' WHERE studentName = 'Wisdom'")
db.commit()

#delete data from the table
mycursor.execute("DELETE FROM students WHERE studentName = 'Sophie'")
db.commit()

#close connection
db.close()