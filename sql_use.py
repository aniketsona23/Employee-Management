import mysql.connector as msc

mydb = msc.connect(host="localhost", user="root", password="aniket", database="employee")
cur = mydb.cursor()


def fetch_data(table, column="*", condition="True"):
    # print(f"SELECT {column} FROM {table} WHERE {condition} ORDER BY SNO")
    cur.execute(f"SELECT {column} FROM {table} WHERE {condition}")
    data = cur.fetchall()
    if column == "*":
        pass
    else:
        for i in range(len(data)):
            data[i] = data[i][0]
    return data


def insert_data(table, values):
    try:
        cur.execute(f"INSERT INTO {table} VALUES ({values}) ")
        mydb.commit()
    except msc.Error as error:
        print(error)
        mydb.rollback()


def delete_data(table, condition="TRUE"):
    cur.execute(f"DELETE FROM {table} WHERE {condition}")
    mydb.commit()


def update_data(table, values, condition="TRUE"):
    try:
        cur.execute(f"UPDATE {table} SET {values} WHERE {condition}")
        mydb.commit()
    except msc.Error as error:
        print(error)
        mydb.rollback()
