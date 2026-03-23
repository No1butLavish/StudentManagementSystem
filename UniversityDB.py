import mysql.connector
import pandas as pd

#creating the connection
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "RaspberryPi8"
)

#creating our database
sqlDatabase = "CREATE DATABASE IF NOT EXISTS Uni"
cursor = db.cursor()
cursor.execute(sqlDatabase)

#connecting database
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "RaspberryPi8",
    database = "Uni"
)

#creating our first table
sqlTable = """ CREATE TABLE IF NOT EXISTS student(
                studentNumber INT PRIMARY KEY,
                name varchar(50),
                surname varchar(50)
                
                )
        """
cursor = db.cursor()
cursor.execute(sqlTable)

#lets see the tables we have in our database
cursor = db.cursor()
cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)

print()
#finding out the columns in the table
cursor = db.cursor()
cursor.execute("SHOW COLUMNS FROM student")

for x in cursor:
    print(x)

#add data into the tables
sqlInput = "INSERT INTO student(studentNumber,name,surname) VALUES (%s,%s,%s)"
sqlData = (225078721,"Unathi","Mthethwa")
cursor = db.cursor()
cursor.execute(sqlInput,sqlData)
db.commit()

#fetching the data in the table
cursor = db.cursor()
cursor.execute("SELECT * FROM student")
result = cursor.fetchall()

for row in result:
    print(row)

#lets delete the records in the table
sqlDelete = "DELETE FROM student"
cursor = db.cursor()
cursor.execute(sqlDelete)
db.commit()

#now lets see if it worked
cursor = db.cursor()
cursor.execute("SELECT * FROM student")
result = cursor.fetchall()

for row in result:
    print(row)

#lets insert a new record
sqlData = (225011262,"Methuli","Dlamini")
cursor = db.cursor()
cursor.execute(sqlInput,sqlData)
db.commit()

#lets output the data
cursor = db.cursor()
cursor.execute("SELECT * FROM student")
result = cursor.fetchall()
print()
print("display  data")
for row in result:
    print(row)

#creating our second table
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS qualification(
               degreeID INT PRIMARY KEY,
               college varchar(100),
               school varchar(50),
               degree varchar(50),
               major1 varchar(50),
               major2 varchar(50),
               year INT,
               FOREIGN KEY (studentNumber) REFERENCES student(studentNumber),
               FOREIGN KEY (courseID) REFERENCES courseInfo(courseID)
               
               )
               """)

#lets find out the tables in our database
cursor = db.cursor()
cursor.execute("SHOW TABLES")
print()
for x in cursor:
    print(x)

#lets delete unwanted table 
cursor = db.cursor()
#cursor.execute("DROP TABLE degree")

#lets find out the tables in our database
cursor = db.cursor()
cursor.execute("SHOW TABLES")
print()
for x in cursor:
    print(x)

#lets delete unwanted table 
#cursor = db.cursor()
#cursor.execute("DROP TABLE qualificaion")

#lets find out the tables in our database
cursor = db.cursor()
cursor.execute("SHOW TABLES")
print()
for x in cursor:
    print(x)

#lets delete unwanted table 
cursor = db.cursor()
##cursor.execute("DROP TABLE qualificaion")

#lets find out the tables in our database
cursor = db.cursor()
cursor.execute("SHOW TABLES")
print()
for x in cursor:
    print(x)

print()
#lets find out if second table has columns
sqlShow = "SHOW COLUMNS FROM qualification"
cursor = db.cursor()
cursor.execute(sqlShow)

for x in cursor:
    print(x)
#inserting data into our second table
print()
print("the data from the table")

#validation to decrease error




#method to prevent duplication error when insertiong
degreeID = "225011262"
check = "SELECT * FROM qualification WHERE degreeID = 225011262"
cursor = db.cursor()
cursor.execute(check)

result = cursor.fetchone()

if result:
    print("primary key already exists")
else:
        sqlInput = "INSERT INTO qualification(degreeID,college,school,degree,major1,major2,year) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        sqlData = (225011262,
           "Health Science",
           "Health",
           "B Pharm Pharmacy",
           "Pharmaseutical science",
           "none",
           4
           )
        cursor = db.cursor()
        cursor.execute(sqlInput,sqlData)
        db.commit()


#Display data in second table
cursor = db.cursor()
cursor.execute("SELECT * FROM qualification")
result = cursor.fetchall()

for row in result :
    print(row)

#deleting the duplicate data
sqlDelete = "DELETE FROM qualification where degreeID = 225078721"
cursor = db.cursor()
cursor.execute(sqlDelete)

#displaying the data
print()
cursor = db.cursor()
cursor.execute("SELECT * FROM qualification")
result = cursor.fetchall()
for row in result:
    print(row)

#creating our third table 
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS courseInfo(
               courseID INT PRIMARY KEY,
               coreModule1 varchar(100),
               coreModule2 varchar(100),
               electiveModule1 varchar(100),
               electiveModule2 varchar(100),
               electiveModule3 varchar(100),
               electiveModule4 varchar(100),
               extraModule varchar(100),
               FOREIGN KEY (studentNumber) REFERENCES student(StudentNumber),
               FOREIGN KEY (degreeID) REFERENCES qualification(degreeID)
               )
               """)

#lets show the tables we have in our database
print()
cursor = db.cursor()
cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)

#now lets see the columns in our table
print()
cursor = db.cursor()
cursor.execute("SHOW COLUMNS FROM courseInfo")

for x in cursor:
    print(x)

#this is to see our tables
print()
cursor = db.cursor()
cursor.execute("""
SELECT table_name FROM information_schema.tables
WHERE table_schema = 'Uni'
                """)

for x in cursor:
    print(x)

print()

cursor = db.cursor()
cursor.execute("DESCRIBE courseInfo")

for x in cursor:
    print(x)

#making changes to my table since columns are
#cursor.execute("ALTER TABLE users ADD COLUMN age INT")
# forgot this:
#db.commit()

#cursor = db.cursor()
#cursor.execute("ALTER TABLE courseInfo ADD COLUMN electiveModule1 varchar(100)")
#cursor.execute("ALTER TABLE courseInfo ADD COLUMN electiveModule2 varchar(100)")
#cursor.execute("ALTER TABLE courseInfo ADD COLUMN electiveModule3 varchar(100) ")
#cursor.execute("ALTER TABLE courseInfo ADD COLUMN electiveModule4 varchar(100)")
#cursor.execute("ALTER TABLE courseInfo ADD COLUMN electiveModule4 varchar(100)")
#cursor.execute("ALTER TABLE courseInfo ADD COLUMN Year INT")


#lets keep track of our columns here
cursor = db.cursor()
cursor.execute("DESCRIBE courseInfo")
print()
for x in cursor:
    print(x)


#all tables are created and connected in the table we can start manipulating,adding and removing data
#inserting more students in the student table
#first lets look at the data inside
cursor = db.cursor()
cursor.execute("SELECT * FROM student")
print()
for x in cursor:
    print(x)

#inserting data again
sqlInput = "INSERT INTO student(studentNumber,name,surname) VALUES (%s,%s,%s)"
sqlData = (225078721,"Unathi","Mthethwa")
cursor = db.cursor()
cursor.execute(sqlInput,sqlData)
db.commit()

#displaying the data we have inserted along with other ones
db.cursor()
cursor.execute("SELECT * FROM student")
result = cursor.fetchall()

print()
for row in result:
    print(row)

#inserting more data to work with 
sqlInput = "INSERT INTO student(studentnumber,name,surname) VALUES (%s,%s,%s)"
sqlData = (225017210,"Ithandile","Mahlamvu")
cursor = db.cursor()
cursor.execute(sqlInput,sqlData)
db.commit()

sqlData = (223015212,"Avela","Cele")
cursor = db.cursor()
cursor.execute(sqlInput,sqlData)
db.commit()

sqlData = (225054879,"Mosa","Ntshangase")
cursor = db.cursor()
cursor.execute(sqlInput,sqlData)
db.commit()

sqlData = (225052822,"Khwatsi","Mkansi")
cursor = db.cursor()
cursor.execute(sqlInput,sqlData)
db.commit()

#displaying our current data from student without pandas
cursor = db.cursor()
cursor.execute("SELECT * FROM student")
result = cursor.fetchall()

for row in result:
    print(row)

#inputting data into our second table
sqlInput = "INSERT INTO qualification (degreeID,college,school,degree,major1,major2,year) VALUES (%s,%s,%s,%s,%s,%s,%s)"
sqlData = (225078721, 
           "Agriculture,Engineering and Science",
           "Math,Stats and Comp",
           "Bsc Stream M",
           "Computer Science",
           "Statistics",
           3)
cursor = db.cursor()
cursor.execute(sqlInput,sqlData)
db.commit()

#displaying it alone 
cursor = db.cursor()
cursor.execute("SELECT * FROM qualification")

print()
result = cursor.fetchall()
for x in result:
    print(x)

#now display using join and some form of manipulation
cursor = db.cursor()
cursor.execute("""SELECT student.name AS name, 
               qualification.major1 AS major 
               FROM student
               INNER JOIN qualification ON 
               student.studentnumber = qualification.degreeID

               """)

print()
print("manipulated table")
result = cursor.fetchall()
for x in result:
    print(x)


#using pandas series 

cursor = db.cursor()
cursor.execute("SELECT * FROM student")

table = pd.DataFrame(cursor)
print(table)

sqlInput = "INSERT INTO student(studentnumber,name,surname) VALUES (%s,%s,%s)"
sqlData = (225038390,"Andile","Zuma")
cursor = db.cursor()
cursor.execute(sqlInput,sqlData)
db.commit()
print()
print("data inserted successfully")

check = "SELECT * FROM qualification WHERE degreeID = 225038390"
cursor = db.cursor()
cursor.execute(check)
result =  cursor.fetchone()

if result:
    print("data already exists")
else:

    sqlInput = "INSERT INTO qualification(degreeID,college,school,degree,major1,major2,year) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    sqlData = (225038390,
               "Agriculture,Engineering and Science",
               "Math,Stats and Comp",
               "Bsc Comp and IT",
               "Computer Science",
               "Information Technology",
               3
               )
    cursor = db.cursor()
    cursor.execute(sqlInput,sqlData)
    db.commit()
    print()
    print("data inserted into qualification table")

check = "SELECT * FROM courseInfo WHERE courseID = 225078721"
cursor = db.cursor()
cursor.execute(check)
result =  cursor.fetchone()
if result:
    print("data already exists")
else:

    sqlInput = "INSERT INTO courseInfo(courseID,coreModule1,corModule2,electiveModule1,electiveModule2,electiveModule3,electiveModule4,Year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    sqlData = (225078721,
               "comp100",
               "math130",
               "none",
               "none",
               "none",
               "none",
               1
               )
    cursor = db.cursor()
    cursor.execute(sqlInput,sqlData)
    print()
    print("data inserted into third table")

check = "SELECT * FROM student WHERE studentnumber = 225045289"
cursor = db.cursor()
cursor.execute(check)
result = cursor.fetchone()

if result:
    print("student already exists")

else:
    sqlInput = "INSERT INTO student(studentnumber,name,surname) VALUES (%s,%s,%s)"
    sqlData = (225045289,
               "Unathi",
               "Zulu")
    cursor = db.cursor()
    cursor.execute(sqlInput,sqlData)
    db.commit()

cursor  = db.cursor()
cursor.execute("SELECT * FROM student")

result = cursor.fetchall()
tabulate = pd.DataFrame(result)
print()
print(tabulate)

check = "SELECT * FROM qualification WHERE degreeID = 225045289"
cursor = db.cursor()
cursor.execute(check)
result = cursor.fetchone()

if result:
    print("student already exists")
else:
    sqlInsert = "INSERT INTO qualification(degreeID,college,school,degree,major1,major2,year) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    sqlData = (225045289,
               "Agriculture,Engineering and Science",
               "Life Sciences",
               "Bsc Stream LES",
               "Chemistry",
               "Biochemistry",
               3)
    cursor = db.cursor()
    cursor.execute(sqlInsert,sqlData)
    db.commit()
    print("data inserted")

#outputting data in our table
cursor = db.cursor()
cursor.execute("SELECT * FROM qualification")
result = cursor.fetchall()

#printing in tuple format 
print()
for row in result:
    print(row)
print()

#printing in 2 dimensional format 
tablulate = pd.DataFrame(result)
print(tablulate)

check = "SELECT * FROM student WHERE studentnumber = 224086779"
cursor = db.cursor()
cursor.execute(check)
result = cursor.fetchone()

if result:
    print("student already exist")
else:
    sqlInsert = "INSERT INTO student(studentnumber,name,surname) VALUES (%s,%s,%s)"
    sqlData = (224086779,
               "Thando",
               "Ngcobo")
    cursor = db.cursor()
    cursor.execute(sqlInsert,sqlData)
    db.commit()

cursor = db.cursor()
cursor.execute("SELECT * FROM student")

print()
tabulate = pd.DataFrame(cursor)
print(tabulate)

check = "SELECT * FROM qualification where degreeID = 224086779"
cursor = db.cursor()

cursor.execute(check)
result = cursor.fetchone()

if result:
    print("data already exists")
else:
    sqlInsert = "INSERT INTO qualification(degreeID,college,school,degree,major1,major2,year) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    sqlData = (224086779,
               "Agriculture,Engineering and Science",
               "School of Life Science",
               "Bsc Stream LES",
               "Microbiology",
               "Genetics",
               3
               )
    cursor = db.cursor()
    cursor.execute(sqlInsert,sqlData)
    db.commit()

cursor = db.cursor()
cursor.execute("SELECT * FROM qualification")

tabulate = pd.DataFrame(cursor)
print()
print(tabulate)

cursor = db.cursor()
cursor.execute("""SELECT student.name as Name,
                qualification.degree as Degree, 
               qualification.major1 as Major
               FROM
               student INNER JOIN qualification
               ON student.studentnumber = qualification.degreeID
               """)
print()
tabulate = pd.DataFrame(cursor)
print(tabulate)

check = "SELECT * FROM courseInfo WHERE courseID = 225011262"
cursor = db.cursor()
cursor.execute(check)
result = cursor.fetchone()

if result:
    print("data already exists")
else:
    sqlInsert = "INSERT INTO courseInfo(courseID,coreModule1,corModule2,electiveModule1,electiveModule2,electiveModule3,electiveModule4,Year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    sqlData = (225011262,
               "Bio103",
               "Phys131",
               "none",
               "none",
               "none",
               "none",
               1
               )
    cursor = db.cursor()
    cursor.execute(sqlInsert,sqlData)
    db.commit()

cursor = db.cursor()
cursor.execute("SELECT * FROM courseInfo")

tabulate = pd.DataFrame(cursor)
print()
print(tabulate)

check = "SELECT * FROM courseInfo WHERE courseID = 225045289 "
cursor = db.cursor()
cursor.execute(check)

result = cursor.fetchone()

if result :
    print("student data already exists")
else:
    sqlInsert = "INSERT INTO courseInfo(courseID,coreModule1,corModule2,electiveModule1,electiveModule2,electiveModule3,electiveModule4,Year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    sqlData = (225045289,
               "Chem210",
               "Chem220",
               "Biochem200",
               "Math150",
               "none",
               "none",
               2
               )
    cursor = db.cursor()
    cursor.execute(sqlInsert,sqlData)
    db.commit()
    print("data inserted")

cursor = db.cursor()
cursor.execute("SELECT * FROM courseInfo")

tabulate = pd.DataFrame(cursor)
print()
print(tabulate)

check = "SELECT * FROM courseInfo WHERE courseID = 225038390 "
cursor = db.cursor()
cursor.execute(check)

result = cursor.fetchone()

if result :
    print("student data already exists")
else:
    sqlInsert = sqlInsert = "INSERT INTO courseInfo(courseID,coreModule1,corModule2,electiveModule1,electiveModule2,electiveModule3,electiveModule4,Year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    sqlData = (225038390,
           "comp200",
           "istn212",
           "math140",
           "managemant130",
           "none",
           "none",
           2)
    cursor = db.cursor()
    cursor.execute(sqlInsert,sqlData)
    db.commit()

sqlInsert = "INSERT INTO student(studentnumber,name,surname) VALUES (%s,%s,%s)"
sqlData = (224050732,
           "Sthabile",
           "Zubane")
cursor = db.cursor()
cursor.execute(sqlInsert,sqlData)
db.commit()

sqlInsert = "INSERT INTO student(studentnumber,name,surname) VALUES (%s,%s,%s)"
sqlData= (225105371,
         "Xihlenge xa vulombe",
         "Majola")

cursor = db.cursor()
cursor.execute(sqlInsert,sqlData)
db.commit()

check = "SELECT * FROM qualification WHERE degreeID = 225105371"
cursor = db.cursor()
cursor.execute(check)
result= cursor.fetchone()

if result:
    print("data already inserted")
else:
    sqlInsert = "INSERT INTO qualification(degreeID,college,school,degree,major1,major2,year) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    sqlData = (225105371,
              "Law and Management Studies",
              "Commerce",
              "Bcom General in Information Systems and Technology",
              "Information Systems and Technology",
              "Information Systems in Computing",
              4

              )
    cursor = db.cursor()
    cursor.execute(sqlInsert,sqlData)
    db.commit()

cursor = db.cursor()
cursor.execute("SELECT * FROM qualification")

tabulate = pd.DataFrame(cursor)
print()
print(tabulate)


