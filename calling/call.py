
from tasks.taskFile import createTask,readTask,insertTask,deleteTask


conditions='Y'
while conditions=='Y':

    print("Which task do you want to do : ")
    task=int(input(" 1.CREATE \n 2.READ \n 3.INSERT \n 4.DELETE\n 5.EXIT \n"))

    # FOR CREATE
    if task==1:
        createTask()

    # FOR READ
    elif task==2:
        readTask()

    # FOR INSERT
    elif task==3:
        insertTask()

    # FOR DELETE
    elif task==4:
        deleteTask()

    # FOR ENDING THE TASK
    elif task==5:
        conditions='N'
        print("Task has been ended....")

    # FOR WRONG INPUT
    else:
        print("Please Give input Correctly....")
