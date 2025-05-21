# from calculator import calculator
storage=[]
delivered_items=[]
def add_item(item):
    storage.append(item)
    print(f"Item '{item}' added to storage.")
    return storage
def deliver_item(item):
    if item in storage:
        delivered_items.append(item)
        storage.remove(item)
        print(f"Item '{item}' delivered.")
    else:
        print(f"Item '{item}' not found in storage.")
    return storage
def view_storage():
    for i in range(0,len(storage)):
        print(f"Item {i+1}: {storage[i]}")
    print(end=" ")  
    
def customer(): 
     choice=int(input("enter your choice:\n1.Add item to deliver\n2.view storage\n3.Exit\n"))
     while (choice!=3):
        match choice:
                    case 1:
                        item=str(input("enter the item that you want to add:"))
                        add_item(item)
                    case 2:
                        print("Items in storage:")
                        view_storage()
                    case 3:
                        print("Exiting the program.")
                        main()
                        break
                    case _:
                        print("Invalid choice. Please try again.")
        choice=int(input("enter your choice:\n1.Add item to deliver\n2.view storage\n3.Exit\n"))                                                 
        return storage      
def owner():
    choice=int(input("enter your choice:\n1.Deliver item\n2.View delivered items\n3.view storage\n4.Exit\n"))
    while (choice!=3):
                match choice:
                    case 1:
                        item=str(input("enter the item that you want to deliver:"))
                        deliver_item(item)
                    case 2:
                        print("Delivered items:")
                        for i in range(0,len(delivered_items)):
                            print(f"Item {i+1}: {delivered_items[i]}")
                    case 3:
                          view_storage()        
                    case 4:
                        print("Exiting the program.")
                        main()
                        break
                    case _:
                        print("Invalid choice. Please try again.")
                choice=int(input("1.Deliver item\n2.View delivered items\n3.Exit\n"))
                return storage

def main():
     print("Welcome to the delivery system!")
     print("1. Customer")
     print("2. Owner")
     print('3. Exit')
     user=int(input("enter either customer or owner(customer/owner):"))
     while (user!="exit"):
        match user:
            case 1:
                customer()
            case 2:
                owner()
            case 3:
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice. Please try again.")
        print("1. Customer")
        print("2. Owner")
        print('3. Exit') 
        user=int(input("enter either customer or owner(customer/owner):")) 
            
if __name__ == "__main__":
    main()