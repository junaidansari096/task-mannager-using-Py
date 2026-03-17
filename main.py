def task():
    tasks=[]
    print("___welcome to task manager___")

    count= int(input("Enter how many Tasks you want to add: "))

    for i in range(1, count+1):
       task_name= input((f"enter the task {i} "))
       tasks.append(task_name)
    print(f"your tasks are: {tasks}") 

    while True:
        operation=int(input("enter 1-ADD\nEnter 2-Delete\nEnter 3-update\nEnter 4-View\nEnter 5-Exit: "))
        if operation==1:
            add=input("enter the task you want to add: ")
            tasks.append(add)
            print(f"task {add} has sucessfully added..!!")

        elif operation ==3:
            updated_task=input("enter the task you want to update.. ")
            if updated_task in tasks:
                new=input("enter the new task: ")
                ind=tasks.index(updated_task)
                tasks[ind]=new
                print("Task has sucessfully updated..!!")
            else:
                print("invalid input..")  

        elif operation==2:
            delt=input("Enter which task you want to delete ")
            if delt in tasks:
                idx=tasks.index(delt)
                del tasks[idx]
                print(f"Deleted value {delt} has been sucessfully deleted ")
            else:
                print("invalid input..") 

        elif operation==4:
            print(f"your tasks are {tasks}")     

        elif operation == 5:
            print("Thanks for using this app...")
            break

        else:
            print("fuck you Invalid Input..")




          


task()