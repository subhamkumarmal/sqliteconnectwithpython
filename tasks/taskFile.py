
from mainSqlite.main import Connection as conClass

def createTask():

    e = conClass()
    tableName = input("Enter the table that you want create table : ")
    size = int(input("Enter the size of the column : "))
    lst = []
    for i in range(size):
        strs = input("Enter the column name : ")
        lst.append(strs)

    e.createTable(tableName, lst)


def readTask():
    e = conClass()
    exitTableName = input("Enter the table name that you want details : ")
    e.readData(exitTableName)

def insertTask():
    e = conClass()
    reference = e.dbConn()
    table = input("Enter the table where you want into insert the data : ")
    size = int(input("How many data do you want to insert : "))
    lst = conClass().dataDescription(table)

    for i in range(size):
        l = []
        for j in lst.description:
            value = input(f"Enter the {j[0]} : ", )
            l.append(value)

        e.insertData(table, l)

def deleteTask():
    e = conClass()
    tname = input("Enter the table name from where you want to delete the element : ")
    columnsname = input("Enter the column name by deleting : ")
    id = int(input("Enter the id that you want to del the row : "))
    e.deleteData(tname, columnsname, id)

