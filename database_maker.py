import mysql.connector as msq

mydb = msq.connect(user="root", password="aniket", host="localhost")
cur = mydb.cursor()

cur.execute("CREATE DATABASE EMPLOYEES")
cur.execute("USE EMPLOYEES")
print("1")
cur.execute(
    "CREATE TABLE EMP_DATA(NAME VARCHAR(50),EMP_ID VARCHAR(20) UNIQUE PRIMARY KEY,PHONE BIGINT,POST VARCHAR(30),ENTER_TIME VARCHAR(10),LEAVE_TIME VARCHAR(10))")
print("2")
cur.execute(
    "CREATE TABLE ADMIN_LOGIN(EMP_ID VARCHAR(20) UNIQUE,PHONE BIGINT,PASSWORD VARCHAR(20),FOREIGN KEY(EMP_ID) REFERENCES EMP_DATA(EMP_ID))")
print("3")
cur.execute(
    "CREATE TABLE EMP_SALARY(NAME VARCHAR(30),EMP_ID VARCHAR(20) UNIQUE,BASE BIGINT,MEDICAL INT,ADVANCE INT,BONUS INT,FOREIGN KEY(EMP_ID) REFERENCES EMP_DATA(EMP_ID))")
mydb.commit()
print('hello')
mydb.rollback()
