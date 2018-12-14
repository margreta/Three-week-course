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


    def find_edit_booking_name(self):
        name_test = False
        while name_test == False:
            try:
                print("Enter name of editing customer: ")
                first_name = input("First name: ")
                last_name = input("Last name: ")
                name = first_name.capitalize() + " " + last_name.capitalize()
                self.__dealer_service.edit_name(name)# kalla í service fall
                name_test = True
            except:
                print("This name does not exist in the system, please try again.")
                print("")
        return name

    def edit_booking_menu(self):
        edit_choice = 7
        while edit_choice in range(1,6):
            try:
                print("What would you like to edit?")
                print("")
                edit_choice = int(input("1. Name\n2. License\n3. Email\n4. Phone\n5. Credit card insurance\n"))
                self.__dealer_service.edit_menu_check(edit_choice) #hér þarf að kalla í eitthvað í service fallinu
            except:
                print("Not a valid option, please select number from 1 to 5")
                print("")
            return edit_choice

    def edit_name(self,name):
        edit_name = False
        while edit_name == False:
            try:
                print("Enter new customer name: ")
                edit_first_name = input("First name: ")
                edit_last_name = input("Last name: ")
                edit_name = edit_first_name.capitalize() + " " + edit_last_name.capitalize()
                self.__dealer_service.edit_name_check(name, edit_name)# kalla í service fall
                print("{} booking has been changed".format(edit_name))
                print("")
            except:
                print("Whoops, something went wrong.")
                print("")
        return edit_name


    def edit_drivers_license(self,name):
        edit_drivers_license = False
        while edit_drivers_license == False:
            try:
                print("Enter new drivers license number: ")
                edit_drivers_license = input("Drivers license: ")
                self.__dealer_service.edit_drivers_license_check(name, edit_drivers_license)# kalla í service fall
                print("{} booking has been changed".format(name))
                print("")
            except:
                print("Whoops, something went wrong.")
                print("")
        return edit_drivers_license


    def edit_email(self,name):
        edit_email = False
        while edit_email == False:
            try:
                print("Enter new email: ")
                edit_email = input("Email: ")
                self.__dealer_service.edit_email_check(name, edit_email)# kalla í service fall
                print("{} booking has been changed".format(name))
                print("")
            except:
                print("Whoops, something went wrong.")
                print("")
        return edit_email


    def edit_phone_number(self,name):
        edit_phone_number = False
        while edit_phone_number == False:
            try:
                print("Enter new phone number number: ")
                edit_phone_number = input("Phone number: ")
                # edit_phone_number_check = edit_phone_number.isnumeric()
                self.__dealer_service.edit_phone_number(name, edit_phone_number)# kalla í service fall
                print("{} booking has been changed".format(name))
                print("")
            except:
                print("Whoops, something went wrong.")
                print("")
        return edit_phone_number


    def edit_credit_card_insurance(self,name):
        edit_credit_card_info = False
        while edit_credit_card_info == False:
            try:
                print("Enter new credit card number: ")
                edit_credit_card_info = input("Credit card number: ")
                self.__dealer_service.edit_credit_card_insurance_check(name, edit_credit_card_info)# kalla í service fall
                print("{} booking has been changed".format(name))
                print("")
            except:
                print("Whoops, something went wrong.")
                print("")
        return edit_credit_card_info


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