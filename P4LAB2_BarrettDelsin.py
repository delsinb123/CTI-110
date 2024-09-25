#Delsin Barrett
#9/25/2024
#P4LAB2
#Use while loop and for loop together


run_again =  ""

while run_again != "no":
    user_num = int(input("\nEnter an integer: "))
    if user_num < 0:
        print("\nThis program does not handle negative numbers!!\n")
        run_again = input("Would you like to run the program again?")
    else:
        for num in range (12):
            print(f"{user_num} * {num+1} = {user_num * (num+1)}")
            print()
        run_again = input("\nWould you like to run the program again?")
        

#Loop ends
print("\nExiting program...")
