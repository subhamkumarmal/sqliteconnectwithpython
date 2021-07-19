import sqlite3

from cursor import cursors
from sqlite3 import connect



class Connection:

    def dbConn(self):
        curs,conn=cursors.cursor()
        print("Cursor has been successfully created..")
        return curs


    def createTable(self,tableName,*n):
        curs,conn = cursors.cursor()
        print(type(n))
        t=tuple(n[0])
        print(t)
        take=curs.execute(f'create table {tableName} {t}')
        print(f"{tableName} Table has been successfully created.. {t}")
        take.close()
        conn.close()


    def insertData(self,tname,*n):
        t=tuple(n[0])
        curs,conn = cursors.cursor()
        no=len(t)
        strings=''
        for i in range(no):
           strings=strings+'? ,'
        strs=strings[:len(strings)-1]
        take=curs.execute(f'insert into {tname} values ({strs})',t)
        commites = input("Are you sure to commite this created table Y/N : ").upper()

        if commites == 'Y':
            conn.commit()
            print("successfully inserted")
            take.close()
            conn.close()
        else:
            print("Please do commite otherwise will not see any changes into database : ")



    def readData(self,tname):
        curs,conn=cursors.cursor()
        data=curs.execute(f'select * from {tname}')
        for i in data:
            count=0
            for j in data.description:
                print(f"{j[0]} = {i[count]} || ",end=" ")
                count+=1
            print()
        data.close()
        conn.close()

    def deleteData(self,tname,strs,name):

        curs,conn=cursors.cursor()
        # curs.execute(f"DELETE FROM {tname} WHERE {strs} = {name}").close()
        curs.execute('DELETE FROM tables WHERE id = 1').close()
        conn.commit()
        conn.close()




    def dataDescription(self,tname):
        curs,conn=cursors.cursor()
        data=curs.execute(f"select * from {tname}")
        data.close()
        conn.close()

        return data

