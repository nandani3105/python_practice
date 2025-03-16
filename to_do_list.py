def task():
    tasks=[]
    print("-----------------Welcome To Task Manager App--------------")

    total_task=int(input("Enter the no. of task you wanted to add = "))
    for i in range(1,total_task+1):
        task_name=input(f"enter the task{i} =")
        tasks.append(task_name)

    print(f"Todays task are\n{tasks}")

    while True:
        operation=int(input("Enter\n 1-Add\n2-Upadat\n3-Delete\n4-View\n5-Exit/stop"))
        if operation==1:
          add =input("Enter the task you want to add =")
          tasks.append(add)
          print(f"Task {add} has been  successfully added......")

        elif operation==2:
            update=input("Enter the name of the task you want to update = ")
            if update in tasks:
                up=input("Enter new task = ")
                ind=tasks.index(update)
                tasks[ind]=up
                print(f"Task updated {up} successfully........")

        elif operation==3:
            delt = input("Which task you wanted to delete = ")
            if delt in tasks:
                ind2=tasks.index(delt)
                del tasks[ind2]       
                print(f"Task {delt} has been deleted ..........")

        elif operation==4:
            print(f"Tasks are = {tasks}")

        elif operation==5:
            print("Closing the program......")
            break
        else:
            print("Invalid enter")



task()