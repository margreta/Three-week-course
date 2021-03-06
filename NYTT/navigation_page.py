import datetime

from ui.home_page_ui import Home_page
from ui.dealer_ui import Dealer_Ui
from ui.admin_ui import Admin_Ui
from ui.overview_ui import Overview_Ui
from ui.return_rental_ui import Return_Rental
from ui.change_booking_ui import Change_Booking_Ui

from models.car import Car


class Navigation_Page:
    def __init__(self):
        self.dealer_ui = Dealer_Ui()
        self.admin_ui = Admin_Ui()
        self.home_page = Home_page()
        self.overview_ui = Overview_Ui()
        self.return_rental = Return_Rental()
        self.change_booking = Change_Booking_Ui()
##########################################################################
  # HOME PAGE

    def go_to_homepage(self):
        user = self.home_page.home()
        return user

    def go_to_login(self, user):
        username = self.home_page.log_in(user)
        return username
##########################################################################
  # DEALER - Create booking

    def go_to_dealer_homepage(self):
        dealer_choice = self.dealer_ui.home_page()
        return dealer_choice

    def go_to_options(self):
        continue_vs_back_vs_home = self.dealer_ui.options()
        return continue_vs_back_vs_home

    def create_booking_page_1_of_5(self,confirm):
        while confirm == "n":
            first_name, last_name, driver_license, email, phone_num = self.dealer_ui.create_booking_1_of_5()
            confirm = self.dealer_ui.confirm_customer(first_name, last_name)
        name = first_name + " " + last_name
        current_page = 1
        return name, driver_license, email, phone_num, current_page

    def create_booking_page_2_of_5(self,name,current_page):
        """Get card information for insurance."""
        card_num, validation_date, cvc = self.dealer_ui.create_booking_2_of_5(name)
        current_page += 1
        return card_num, validation_date, cvc, current_page

    def create_booking_page_3_of_5(self,current_page):
        start_date, amount_of_days, inp_car_type = self.dealer_ui.create_booking_3_of_5()
        end_date = self.calculate_date(start_date, amount_of_days)
        price = self.car_type_price(inp_car_type)
        self.dealer_ui.print_end_date(end_date)
        current_page += 1
        return start_date, amount_of_days, inp_car_type, price, end_date, current_page
    
    #Part of create booking page 3 of 5.
    def calculate_date(self,start_date, amount_of_days):
        dt = datetime.datetime.strptime(start_date, "%d/%m/%Y")
        tdelta = datetime.timedelta(days = amount_of_days)
        end_date_calc = dt + tdelta
        end_date = end_date_calc.strftime("%d/%m/%Y")
        return end_date
    
    #Part of create booking page 3 of 5.
    def car_type_price(self,inp_car_type):
        """sets correct price related to the car type"""
        if inp_car_type == "A":
            price = 4000
        elif inp_car_type == "B":
            price = 3000
        elif inp_car_type == "C":
            price = 2000 
        return price 


    def create_booking_page_4_of_5(self,inp_car_type,current_page,start_date):
        """Calculates extras and returns total price"""
        #initiate the price counter.
        total_price = 0 
        #Calculates extras, if customer wants.   -- ATH hér þarf að bæta við möguleika að velja ekkert extra. 
        self.dealer_ui.create_booking_4_of_5(inp_car_type)
        car_pick = self.dealer_ui.picking_car(start_date)
        total_price, kasko_child = self.extras(total_price)
        current_page += 1
        return total_price, kasko_child, car_pick, current_page

    #Part of create booking page 4 of 5.
    def extras(self, total_price):
        extras_option = self.dealer_ui.extras()
        if extras_option == "1": 
            #Kasko costs $50
            total_price += 50 
            kasko_child = "Kasko insurance"
        elif extras_option == "2":
            #Child seat costs $1
            total_price += 1
            kasko_child = "Child seat"
        elif extras_option == "3":
            #Kasko insurance and child seat
            total_price += 51
            kasko_child = "Kasko insurance & child seat"
        elif extras_option == "4":
            #none
            kasko_child = "No extras"
        return total_price, kasko_child 



    def create_booking_page_5_of_5(self, price, total_price,amount_of_days):
        #Get total amount to charge:
        total_amount = price + total_price
        total_amount = total_amount * amount_of_days
        #How is customer paying:
        billing_type = self.dealer_ui.create_booking_5_of_5()
        return total_amount, billing_type
        
#######################################################################################    

    # DEALER - Change booking

    def go_to_change_booking(self):
        change_choice = self.change_booking.change_booking_menu()
        return change_choice

    def edit_booking(self):
        name_test = False
        while name_test== False:
            name, name_test = self.change_booking.find_edit_booking_name()
        edit_choice = self.change_booking.edit_booking_menu()
        #If name is changed
        if edit_choice == 1:
            self.change_booking.edit_name(name)
        #If drivers license is changed
        elif edit_choice == 2: 
            self.change_booking.edit_drivers_license(name)
        #If email is changed
        elif edit_choice == 3:
            self.change_booking.edit_email(name)
        #If phone number is changed
        elif edit_choice == 4:
            self.change_booking.edit_phone_number(name)
        #If credit card number is changed
        elif edit_choice == 5:
            self.change_booking.edit_credit_card_insurance(name)

#######################################################################################    
        
    # DEALER - Overview

    def go_to_overview(self):
        overview_choice = self.overview_ui.overview_menu()
        if overview_choice == 1:
            self.overview_ui.look_up_customer()
        elif overview_choice == 2:
            car_choice = self.overview_ui.car_overview()
            if car_choice == 1 or car_choice == 2:
                self.overview_ui.get_car(car_choice)
            elif car_choice == 3:
                license_number = self.overview_ui.specific_car_input(car_choice)
            elif car_choice == 4:
                self.overview_ui.show_price_list()
            elif car_choice == 5:
                go_to_dealer_homepage = "y"
                return go_to_dealer_homepage
        elif overview_choice == 3:
            go_to_dealer_homepage = "y"
            return go_to_dealer_homepage
        

#######################################################################################    

