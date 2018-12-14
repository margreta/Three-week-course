import datetime

from ui.home_page_ui import Home_page
from ui.dealer_ui import Dealer_Ui
from ui.admin_ui import Admin_Ui
from ui.overview_ui import Overview_Ui
from ui.return_rental_ui import Return_Rental
from ui.change_booking_ui import Change_Booking_Ui
from repository.car_repo import Car_Repo
from service.car_service import Car_Service
from navigation_page import Navigation_Page
from models.car import Car

def billing_type_1(dealer_ui):
    #Credit or debit card:
    card_name, card_number, validation_time = dealer_ui.credit_debit_card()
    type_of_billing = "Credit Card/Debit Card"
    return card_name, card_number, validation_time, type_of_billing

def billing_type_2(dealer_ui):
    #Send bill to travel agency:
    comp_name = dealer_ui.billing_to()
    type_of_billing = "Billing to"
    return comp_name, type_of_billing

def billing_type_3(dealer_ui, total_amount):
    #Cash, calculates the change:
    paid_amount = int(dealer_ui.cash(total_amount))
    type_of_billing = "Cash"
    change = paid_amount - total_amount
    dealer_ui.print_change(change)
    return paid_amount, change, type_of_billing


def main():
    #initiate the navigation class.
    navigation = Navigation_Page()
    home_page = Home_page()
    dealer_ui = Dealer_Ui()
    admin_ui = Admin_Ui()
    change_booking = Change_Booking_Ui()
    return_rental = Return_Rental()
    
    #Homepage and login.
    go_to_homepage = True
    while go_to_homepage:
        home_page.logo()
        user = navigation.go_to_homepage()
        username = navigation.go_to_login(user)

        confirm = "n"
        #dealer homepage.
        if username == "dealer":
            to_dealer_homepage = "y"
            while to_dealer_homepage == "y":
                continue_to_get_to_homepage = "n"
                dealer_choice = navigation.go_to_dealer_homepage()
                if dealer_choice == 1:
                    #All 5 pages of create booking process. 
                    name, driver_license, email, phone_num, current_page = navigation.create_booking_page_1_of_5(confirm)
                    unfinished = True
                    while unfinished:
                        continue_vs_go_to_dealer_homepage = dealer_ui.options()
                        if continue_vs_go_to_dealer_homepage == "1":
                            if current_page == 1:
                                card_num, validation_date, cvc, current_page = navigation.create_booking_page_2_of_5(name,current_page)
                            elif current_page == 2:
                                start_date, amount_of_days, inp_car_type, price, end_date, current_page = navigation.create_booking_page_3_of_5(current_page)
                            elif current_page == 3:           
                                total_price, kasko_child, car_pick, current_page = navigation.create_booking_page_4_of_5(inp_car_type,current_page,start_date)
                                unfinished = False
                        elif continue_vs_go_to_dealer_homepage == "2":
                            continue_to_get_to_homepage = "y"
                            unfinished = False
                            to_dealer_homepage = "y"
                            continue
                    
                    if continue_to_get_to_homepage == "y":
                            continue

                    unconfirmed_billing_type = True
                    while unconfirmed_billing_type:
                        #Get billing type from user. 
                        total_amount, billing_type = navigation.create_booking_page_5_of_5(price, total_price,amount_of_days)
                        if billing_type == "1":
                            #Credit or debit card.
                            card_name, card_number, validation_time, type_of_billing  = billing_type_1(dealer_ui)
                        elif billing_type == "2":
                            #Send bill to another company (f.e. travel agency)
                            comp_name, type_of_billing = billing_type_2(dealer_ui)
                        elif billing_type == "3":
                            #Cash
                            paid_amount, change, type_of_billing = billing_type_3(dealer_ui, total_amount)
                        elif billing_type == "4":
                            #Go back to Dealer homepage:
                            to_dealer_homepage = "y"
                            break

                        #If one of first three are chosen the user needs to confirm the payment.
                        if billing_type in "1,2,3":
                            confirm_payment = dealer_ui.confirm_billing()
                            if confirm_payment == "n":
                                #Start over:
                                continue
                            if confirm_payment == "y":
                                booking_status = "New"
                                #print the reciept.
                                dealer_ui.create_booking_6_of_5_recipt(name,driver_license,email,phone_num, price, kasko_child, total_amount, car_pick,amount_of_days)
                                #Create the booking in csv file.
                                dealer_ui.create_the_booking(name, driver_license, email, phone_num,card_num, start_date, end_date,car_pick, inp_car_type, total_amount,kasko_child , type_of_billing, booking_status)
                                unconfirmed_billing_type = False
                                break

                #DEALER : change booking
                elif dealer_choice == 2:
                    change_choice = navigation.go_to_change_booking()
                    #Edit booking.
                    if change_choice == 1:
                        navigation.edit_booking()
                    #Cancel booking.
                    elif change_choice == 2:
                        change_booking.cancel_booking()
                #DEALER : return rental
                elif dealer_choice == 3:
                    return_rental.return_rental_ui()
                    
                #DEALER : overview
                elif dealer_choice == 4: 
                    to_dealer_homepage = navigation.go_to_overview()
                    to_dealer_homepage = "y"
                    continue                      
                #DEALER : log out
                elif dealer_choice == 5:
                    to_dealer_homepage = "n"
                    break

        elif username == "admin":
            to_admin_homepage = "y"
            while to_admin_homepage == "y":
                admin_choice = admin_ui.admin_home_page()
                if admin_choice == 1:
                    again = "y"
                    counter = 0
                    while again == "y":
                        license_num, car_type, confirm, again = admin_ui.create_car_page()
                        price = navigation.car_type_price(car_type)
                        admin_ui.create_the_car(license_num, car_type, price)
                        counter += 1
                    admin_ui.counter_added_cars(counter)
                elif admin_choice == 2:
                    admin_ui.remove_car()
                elif admin_choice == 3:
                    admin_ui.mark_repair()
                elif admin_choice == 4:
                    go_to_homepage = "y"
                    

main()
