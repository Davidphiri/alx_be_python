#Prompts user for Pattern Size
size = int(input("Enter the size of the pattern: "))

row = 0

#while loop iterates through each row
while row < size:
    
    for x in range(size):
        print("*", end="")
        
    print()
    
    row += 1
    

