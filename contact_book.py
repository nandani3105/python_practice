contact_book={}
while True:
    operation =int(input("\n Enter the Operations you want to perform  :\n1CREAT \n2.VIEW \n3.SEARCH \n4.UPDATE \n5 COUNT \n6.DELETE\n7.EXISTS \n : "))

    if operation==1:
            name=input("enter the name : ")
            if name in contact_book:
                  print("already exist")
            else:
                  email=input("enter the email : ")
                  phone_no=int(input("enter the number :"))
                  address=input("enter the address : ")
                  contact_book[name]={f'email':{email},'phone_no':{phone_no},'address':{address}}
                  print(f"contact {name} is created successfully:")
    
    elif operation ==2:
          name1=input("enter the name you want to view : ")
          if name in contact_book:
            #     contact =contact_book[name]
                print(f'name:{name},\n email:{email},\n phone_no:{phone_no},\n address:{address}')
          else:
             print("contact not found !")

    elif operation==3:
           search_name=input("enter the name you want to search : ")
           for name , contact in contact_book.items():
                 if search_name.lower() in name.lower():
                       print(f'name:{name},email:{email},phone_no:{phone_no},address:{address}')
                 else:
                    print("contact not found!")    
    
    elif operation==4:
            name=input("enter the name you want to update : ")
            if name in contact_book:
                  email=input("enter the update email : ")
                  phone_no=int(input("enter the updated number :"))
                  address=input("enter the updated address : ")
                  contact_book[name]={f'email':{email},'phone_no':{phone_no},'address':{address}}
                  print(f"contact {name} is updated successfully:")
            else:
                  print("contact not found")
    elif operation==5:
            print(f"total no of contact are {len(contact_book)}")

    elif operation==6:
            name=input("enter the name you want to delete : ")
            if name in contact_book:
                  del contact_book[name]
                  print(f"contact {name} is deleted successfully:")
            else:
                print("contact not found!")

    elif operation ==7:
                    print(f"closing contac_book manager..........")
                    break
        
    else:
       print("You have enter the operation which is not in the list")