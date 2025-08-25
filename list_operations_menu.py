# Program to perform basic list operations: insert, update, delete, and sort

# Take input for number of elements in the list
elements = int(input("Enter the no.of Elements you want in a list : \n"))

# Initialize counter and empty list
i = 0
aa = []

# Loop to take elements from user and add to the list
while (i < elements):
    a = input("Enter the element : ")
    aa.append(a)
    i += 1

# Print the initial list
print(aa)

# Infinite loop for menu-driven operations
while True:
    print("\nMenu")
    print("Enter 'insert' to Insert an Element")
    print("Enter 'update' to Update an Element")
    print("Enter 'delete' to Delete an Element")
    print("Enter 'sort' for sorting an Element")

    # Take user choice
    choice = input("\nEnter your choice : ")

    # Insert operation
    if choice == 'insert':
        index = int(input("Enter the index of the element where you want to insert : "))
        value = int(input("Enter the value you want to insert : "))

        aa.insert(index, value)  # Insert value at index
        print(aa)

        # Using default method (append)
        d = int(input("\nInsert a value for Default method : "))
        aa.append(d)
        print(aa)

    # Update operation
    elif choice == 'update':
        index = int(input("Enter the index of the element where you want to update : "))
        value = int(input("Enter the new value : "))

        aa[index] = value  # Update value at index
        print(aa)

    # Delete operation
    elif choice == 'delete':
        value = int(input("\nEnter the value you want to delete : "))

        aa.remove(value)  # Remove specific value
        print(aa)

        # Using default method (pop)
        print("\nDefault Delete method :")
        aa.pop()
        print(aa)

    # Sort operation
    elif choice == 'sort':
        print("\nList after using sort :- ")
        aa.sort()
        print(aa)

    # Invalid choice
    else:
        print("Enter a valid input !! ")

    # Ask if user wants to continue
    take = input("Do you want to proceed (yes or stop) : ")
    if take == 'stop':
        print("\nProgram Terminated")
        del aa  # Delete the list
        print(aa)  # Will throw error since aa is deleted
        break
