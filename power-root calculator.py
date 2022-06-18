print ("\n\nWelcome to the power/root calculator\n\n")

def main():
    def options():
        option = (input("Choose an option:\n\n 1. Root \n 2. Power\n\n"))
        
        while option not in ("1", "2"):
            print("Please choose 1 or 2 ")
            options()
            
        x = float(input("enter the number: "))

        if option == "1":
            root = float(input("enter the root: "))
            result = x**(1/root)
            print(result)

        if option == "2":
            power = float(input("enter the power: "))
            result = x**(power)
            print(result)

        restart = input("Do you want to start again? y / n: ")
    
        if restart == "y":
            main()
        elif restart == "n":
            exit()
            
    options()
    
main()