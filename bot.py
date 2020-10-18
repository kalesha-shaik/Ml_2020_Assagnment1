import random
from datetime import datetime

'''
this function gives us greeting message

'''

def greeting():
    responce = [
    "hello...! Hai Nice to see You",
    "welcome To the portal nice to see you here"
    ]
    print(random.choice(responce))

'''
this function gives us greeting with current time 
i.e if it is AM then it will greet us Good Morning
based on time it will greet us.

'''


def current_time_greet():
    current_time_greet=datetime.now()
    greeting="good morning"
    if current_time_greet.hour>12 and current_time_greet.hour<17:
        greeting="good afternoon"
    elif current_time_greet.hour>=17 and current_time_greet.hour<22:
        greeting="good evening"
    elif current_time_greet.hour>=22:
        greeting="Hi, its too late"
    return greeting

'''
this function gives us Welcome message 

'''

def welcome(name):
    message = [
        "welcome, to the portal nice to see you here..!  Who you are..?",
        "nice to meet you..! Welcome.... Who you are..?"
    ]
    print(f"{current_time_greet()},! {name}, {random.choice(message)}")


'''
this function gives us farmer menu. main menu it will show.

'''

def farmer_menu():
    print("1. Farmer")
    print("2. Buyer")
    print("3. End")
    print("-------------------")
    try:
        return int(input("Enter your choice[1-3]:  "))
    except:
        print("invalid try again")
        return 0

lst = []
def farmer():
    expr = input("Enter the farmer name to display Buyer : ")
    try:
        print("the farmer name you entered to display Buyer is : ", expr )
    except Exception as e:
        print(str(e))
    def farmerlog_menu():
        print("1. Farmer login")
        print("2. Farmer Registration")
        print("3. End")
        print("-------------------")
        try:
            return int(input("Enter your choice[1-3] : "))
        except:
            print("invalid try again")
            return 0
    def farmerlog():
        farmer_name = input("Enter the farmer name to login : ")
        farmer_number = int(input("Enter the farmer contact number : "))
        try:
            print("Farmer name is : ", farmer_name )
            print("Farmer number is : ", farmer_number)
            print("login success")
            product_location = input("Please enter your location : ")
            product_name = input("Enter your Product: ")
            product_quantity = int(input("Enter the Quantity of your product(in kgs): "))
            product_price = int(input("Enter the price of your product(in thousands): "))
            product_discription = input("Enter a short discription of your product: ")
            try:
                lst.append(farmer_name)
                lst.append(farmer_number)
                lst.append(product_location)
                lst.append(product_name)
                lst.append(product_quantity)
                lst.append(product_price)
                lst.append(product_discription)
                print("Location : ", product_location)
                print("Product name is : ", product_name )
                print("Product Quantity is : ", product_quantity," Kgs")
                print("Price of the procut is ",product_price, " /-")
                print("product Discription is : ", product_discription)
                print("Your product detais are successfully inserted to our database. The buyer will contact you soon")
                print("Happy earning :)")
            except Exception as e:
                print(str(e))          
        except Exception as e:
            print(str(e))
    def farmerreg():
        farmer_name = input("Enter the farmer name to Register: ")
        farmer_number = int(input("Enter the farmer contact number: "))
        farmer_aadhar = int(input("Enter the farmer aadhar number: "))
        try:
            print("name is : ", farmer_name )
            print("number is : ", farmer_number)
            print("your aadhar number is : ", farmer_aadhar)
            print("Farmer Registration success")
            product_name = input("Enter your Product: ")
            product_quantity = int(input("Enter the Quantity of your product(in kgs): "))
            product_price = int(input("Enter the price of your product(in thousands): "))
            Product_discription = input("Enter a short discription of your product: ")
            try:
                print("Product name is : ", product_name )
                print("Product Quantity is : ", product_quantity," Kgs")
                print("Price of the procut is ",product_price, " /-")
                print("product Discription is : ", Product_discription)
                print("Your product detais are successfully inserted to our database. The buyer will contact you soon")
                print("Happy earning :)")
            except Exception as e:
                print(str(e))          
        except Exception as e:
            print(str(e))

    def farmer_log():
        choices = farmerlog_menu()
        while choices != 3:
            if choices ==1:
                farmerlog()
            elif choices ==2 :
                farmerreg()
            else:
                print("sorry")
            choices = farmerlog_menu()
    farmer_log()




'''
this function gives us buyer menu

'''


def buyer():
    expr = input("Enter the buyer name : ")
    try:
        print("name is : ", expr )
    except Exception as e:
        print(str(e))
    def buyerlog_menu():
        print("1. buyer login")
        print("2. buyer Registration")
        print("3. End")
        print("-------------------")
        try:
            return int(input("Enter your choice[1-3]"))
        except:
            print("invalid try again")
            return 0
    def buyerlog():
        buyer_name = input("Enter the buyer name to login : ")
        buyer_number = input("Enter the buyer number : ")
        try:
            print("buyer name is : ", buyer_name )
            print("buyer number is : ", buyer_number )  
            print("Location of the product : ",lst[2]) 
            print("Name of the farmer : ", lst[0])
            print("Phone number to contact the farmer : ",lst[1])
            print("Product : ",lst[3])
            print("Quantity of the product : ",lst[4])
            print("Price of the product : ", lst[5])
            print("Discription of the product provided by farmer : ", lst[6])
            print("Please call the farmer and buy your product for a better price.")
            print("thanks for being with us...!")
            print("Hope you to see next time :)")

        except Exception as e:
            print(str(e))

    def buyerreg():
        buyer_num = input("Enter the buyer phone number : ")
        try:
            print("name is : ", buyer_num )
        except Exception as e:
            print(str(e))

    def buyer_log():
        choices = buyerlog_menu()
        while choices != 3:
            if choices ==1:
                buyerlog()
            elif choices ==2 :
                buyerreg()
            else:
                print("sorry")
            choices = buyerlog_menu()
    buyer_log()

'''
this function gives us output. 
it prints the output based on our requirements.

'''


def bot():
    greeting()
    name = input("Can you please provide your name : ")
    welcome(name)
    choice = farmer_menu()
    while choice != 3:
        if choice ==1:
            farmer()
        elif choice ==2:
            buyer()
        else:
            print("Invalid..! Try again")
        choice = farmer_menu()  
bot()


















# def food_to_eat():
#         print("The foods which you can intake if you are suffering from Type 1 Diabetes are Brown rice, Whole Wheat, Fruits, Vegetables, Lentils, Sprouts, Beets and etc...")
#     def food_to_avoid():
#         print("The foods which you should not intake if you are suffering from Type 1 Diabetes are Sodas, White Bread, Chips, Fried Foods, Refined Grains, Juice Drinks and etc...")
#     def print_food():
#         option = print_food()
#         while option != 3:
#             if option==1:
#                 food_to_eat()
#             elif option==2:
#                 food_to_avoid()
#             else:
#                 return "Sorry"
#             option=type1_diabetes()


