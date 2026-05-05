print ("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas(e.g.5,67,32)")
display_main_menu()
def get_user_input(): 
    number = input()
    numlist = number.split(",")
    print(numlist)
get_user_input()

