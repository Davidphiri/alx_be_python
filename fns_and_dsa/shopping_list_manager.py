def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Please choose an option (1-4): ")
        
        if choice == '1':
            item = input("Enter the item you want to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")
            
        elif choice == '2':
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list")
            else:
                print(f"{item} not found in the shopping list")
                
        elif choice == '3':
            if shopping_list:
                print("Current shopping list: ")
                for index, item in enumerate(shopping_list, start = 1):
                    print(f"{index}, {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':
            print("Exiting the shopping list Manager. Goodbye.")
            break
        else: 
            print("Invalid choice. Please select a valid option (1-4)")
                    
            