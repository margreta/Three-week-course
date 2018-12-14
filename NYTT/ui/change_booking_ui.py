from service.dealer_service import Dealer_service
from service.car_service import Car_Service

class Change_Booking_Ui:

    def __init__(self):
        self.__dealer_service = Dealer_service()
        self.__car_service = Car_Service()
    
    def change_booking_menu(self):
        change_choice = 7
        while change_choice not in range (1,4):
            try:
                print("Choose action:")
                print("")
                change_choice = int(input("1. Edit booking\n2. Cancel booking\n3. Go back\n"))
                self.__dealer_service.change_check(change_choice)#hér þarf að kalla í eitthvað í service fallinu
            except:
                print("Not a valid option, please select number from 1 to 3")
                print("")
        return change_choice
    
############################################################################################################################
############################################################################################################################

#EDIT BOOKING UI


    def edit_booking_name_input(self):
        name = False
        while name == False:
            # try:
            print("Enter name of editing customer: ")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            name = first_name.capitalize() + " " + last_name.capitalize()
            self.__dealer_service.edit_name(name)# kalla í service fall
            name = True
            # except:
            #     print("This name does not exist in the system, please try again.")
            #     print("")
        return name


    def edit_booking_menu(self):
        edit_choice = 7
        while edit_choice in range(1,10):
            try:
                print("What would you like to edit?")
                print("")
                edit_choice = int(input("1. Name\n2. License\n3. Email\n4. Phone\n5. Credit card insurance\n6. Start date\n7. End date\n8. Payment\n"))
                self.__dealer_service.edit_menu_check(edit_choice) #hér þarf að kalla í eitthvað í service fallinu
            except:
                print("Not a valid option, please select number from 1 to 3")
                print("")
            return edit_choice

    #If the edit_choice is 1 then we are changing the name 

    def edit_booking_name(self):
        name = False
        while name == False:
            try:
                print("Enter new name: ")
                first_name = input("First name: ")
                last_name = input("Last name: ")
                edit_name = first_name.capitalize() + " " + last_name.capitalize()
                self.__dealer_service.edit_name_check(name, edit_name)# kalla í service fall
                print("Name has been changed")
                print("")
                name = True
            except:
                print("Whoops, something went wrong.")
                print("")
        return edit_name


############################################################################################################################
############################################################################################################################

#CANCEL BOOKING UI


    def cancel_booking(self):
            name = False
            while name == False:
                try:
                    print("Enter name of cancelling customer: ")
                    first_name = input("First name: ")
                    last_name = input("Last name: ")
                    name = first_name.capitalize() + " " + last_name.capitalize()
                    self.__dealer_service.cancel_check(name)# kalla í service fall
                    license_num = self.__car_service.cb_show_cancel_car(name)
                    self.__car_service.cb_cancel_available(license_num)
                    print("{} had the car {}".format(name,license_num))
                    print("{} booking has been cancelled".format(name))
                    print("")
                    name = True
                except:
                    print("This name does not exist in the system, please try again.")
                    print("")
            return name