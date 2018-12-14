import datetime

from ui.home_page_ui import Home_page
from ui.dealer_ui import Dealer_Ui
from ui.admin_ui import Admin_Ui
from ui.overview_ui import Overview_Ui
from ui.return_rental_ui import Return_Rental
from ui.change_booking_ui import Change_Booking_Ui
from repository.car_repo import Car_Repo
from service.car_service import Car_Service

from models.car import Car

#cb = create booking. 
def cb_page_1_of_5(dealer_ui):
    """Get variables needed to create a booking""" 
    first_name, last_name, driver_license, email, phone_num = dealer_ui.create_booking_1_of_5()
    confirm = dealer_ui.confirm_customer(first_name, last_name)
    current_page = 1
    return first_name, last_name, driver_license, email, phone_num, confirm, current_page

def cb_page_2_of_5(dealer_ui,current_page,first_name, last_name):
    """Get card information for insurance."""
    name = first_name + " " + last_name
    card_num, validation_date, cvc = dealer_ui.create_booking_2_of_5(name)
    current_page += 1
    return card_num, validation_date, cvc, current_page, name 

def cb_page_3_of_5(dealer_ui, current_page):
    """Get starting date of rent and the end date, also get the type of car customer wants to rent."""
    start_date, amount_of_days, inp_car_type = dealer_ui.create_booking_3_of_5()
    end_date = calculate_date(start_date, amount_of_days)
    price = car_type_price(inp_car_type)
    dealer_ui.print_end_date(end_date)
    current_page += 1
    return start_date, amount_of_days, inp_car_type, current_page, price, end_date

def cb_page_4_of_5(dealer_ui,skip_option,inp_car_type, current_page,more_extras = "y"):
    """Calculates extras and returns total price"""
    #initiate the price counter.
    total_price = 0 
    skip_option = "n"
    #Calculates extras, if customer wants.   -- ATH hér þarf að bæta við möguleika að velja ekkert extra. 
    dealer_ui.create_booking_4_of_5(inp_car_type)
    car_pick = dealer_ui.picking_car()
    total_price, kasko_child = extras(dealer_ui,total_price)
    current_page += 1
    return total_price, skip_option, current_page, kasko_child, car_pick


def car_type_price(inp_car_type):
    """sets correct price related to the car type"""
    if inp_car_type == "A":
        price = 4000
    elif inp_car_type == "B":
        price = 3000
    elif inp_car_type == "C":
        price = 2000 
    return price 

#Calculates the end date of the rent
def calculate_date(start_date, amount_of_days):
    dt = datetime.datetime.strptime(start_date, "%d/%m/%Y")
    tdelta = datetime.timedelta(days = amount_of_days)
    end_date_calc = dt + tdelta
    end_date = end_date_calc.strftime("%d/%m/%Y")
    return end_date

def extras(dealer_ui, total_price):
    extras_option = dealer_ui.extras()
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
    #Initiate instances of the classes.
    dealer_ui = Dealer_Ui()
    admin_ui = Admin_Ui()
    home_page = Home_page()
    overview_ui = Overview_Ui()
    rr = Return_Rental()
    cb = Change_Booking_Ui()
    car_repo = Car_Repo()
    car_service = Car_Service()
    

    
    #Homepage, program starts here, defines the user admin or dealer.
    go_to_homepage = "y"
    while go_to_homepage == "y":
        user = home_page.home()
        username = home_page.log_in(user)

        #Starts actions for dealer. 
        go_to_dealer_homepage = "y" 
        while go_to_dealer_homepage == "y":
            if username == "dealer":
                #DEALER - Homepage.
                choice = dealer_ui.home_page()
                #DEALER - Create booking.
                if choice == 1: 
                    #Initializing variables. 
                    repeat = "y"
                    confirm = "n"
                    skip_option = "n"

                    #While loop to provide possibility to travel back and forth on create booking pages. 
                    while repeat == "y":
                        while confirm == "n":
                            first_name, last_name, driver_license, email, phone_num, confirm, current_page = cb_page_1_of_5(dealer_ui)
                        
                        #Option list that appears on every page, but in some cases we don't want it to run. 
                        if skip_option == "n":
                            contin = dealer_ui.options()
                        
                        #If user confirms the inputs and wants to continue (contin = 1) with creating booking.
                        if contin == "1":                        
                            if current_page == 1:
                                card_num, validation_date, cvc, current_page, name = cb_page_2_of_5(dealer_ui,current_page,first_name,last_name)
                            elif current_page == 2:
                                start_date, amount_of_days, inp_car_type, current_page, price, end_date = cb_page_3_of_5(dealer_ui,current_page)                        
                            elif current_page == 3: 
                                total_price, skip_option, current_page, kasko_child, car_pick = cb_page_4_of_5(dealer_ui,skip_option,inp_car_type,current_page)
                            elif current_page == 4:
                                #Get total amount to charge:
                                total_amount = price + total_price
                                total_amount = total_amount * amount_of_days
                                #How is customer paying:
                                billing_type = dealer_ui.create_booking_5_of_5()
                            
                                if billing_type == "1":
                                    card_name, card_number, validation_time, type_of_billing  = billing_type_1(dealer_ui)
                                elif billing_type == "2":
                                    comp_name, type_of_billing = billing_type_2(dealer_ui)
                                elif billing_type == "3":
                                    paid_amount, change, type_of_billing = billing_type_3(dealer_ui, total_amount)
                                elif billing_type == "4":
                                    #Go back one step - go back and re-choose billing type:
                                    current_page -= 1
                                    skip_option = "y"
                                elif billing_type == "5":
                                    #Go back to Dealer homepage:
                                    confirm = "n"
                                    continue

                                #If one of first three are chosen you need to confirm the payment:
                                if billing_type in "1,2,3":
                                    confirm_payment = dealer_ui.confirm_billing()
                                    if confirm_payment == "n":
                                        #Start over:
                                        continue
                                    if confirm_payment == "y":
                                        booking_status = "New"
                                        #print the reciept.
                                        dealer_ui.create_booking_6_of_5_recipt(name,driver_license,email,phone_num, price, kasko_child, total_amount, car_pick)
                                        dealer_ui.create_the_booking(name, driver_license, email, phone_num,card_num, start_date, end_date,car_pick, inp_car_type, total_amount,kasko_child , type_of_billing, booking_status)
                                        break


                        #If user doesn't confirm and wants to go back.    
                        elif contin == "2":
                            #Check the user location.
                            if current_page == 1: 
                                go_to_dealer_homepage = "y"
                                break
                            elif current_page == 2: 
                                confirm = "n"
                                skip_option = "n"
                                continue
                            elif current_page == 3: #Lendi í veseni hér! 
                                current_page -= 1
                                confirm = "y"
                                skip_option = "y"
                                contin = "1"
                                continue
                            elif current_page == 4: 
                                current_page -=1
                                continue
                           
                        #If user doesn't confirm and wants to go to Dealers homepage.
                        elif contin == "3":
                            go_to_dealer_homepage = "y"
                            break

                #DEALER : change booking
                elif choice == 2:
                    change_choice = cb.change_booking_menu()
                    #Edit booking.
                    if change_choice == 1:
                        name = cb.find_edit_booking_name()
                        e_choice = cb.edit_booking_menu() #e_choice stands for edit_choice
                        #If name is changed
                        if e_choice == 1:
                            cb.edit_name(name)
                        #If drivers license is changed
                        elif e_choice == 2:
                            cb.edit_drivers_license(name)
                        #If email is changed
                        elif e_choice == 3:
                            pass
                    elif change_choice == 2:
                        cb.cancel_booking()
                #DEALER : return rental
                elif choice == 3:
                    rr.return_rental_ui()
                    
                #DEALER : overview
                elif choice == 4: 
                    ov_choice = overview_ui.overview_menu()
                    if ov_choice == 1:
                        overview_ui.look_up_customer()
                    elif ov_choice == 2:
                        car_choice = overview_ui.car_overview()
                
                        if car_choice == 1:
                            overview_ui.get_car(car_choice)
                        elif car_choice == 2:
                            overview_ui.get_car(car_choice)
                        elif car_choice == 3:
                            license_number = overview_ui.specific_car_input(car_choice)
                        elif car_choice == 4:
                            overview_ui.show_price_list()
                        elif car_choice == 5:
                            pass
                            #send down to domain
                            # #car_information_menu() #send to car_information_menu class #####
                    elif ov_choice == 3:
                        pass
                        #Hér er farið til baka í dealer homepage
                    overview_ui.go_back()
                #DEALER : log out (go back -- þarf að laga í print setningu)
                elif choice == 5:
                    go_to_homepage = "y"
                    break

            elif username == "admin":
                choice = admin_ui.admin_home_page()
                if choice == 1:
                    again = "y"
                    counter = 0
                    while again == "y":
                        license_num, car_type, confirm, again = admin_ui.create_car_page()
                        price = car_type_price(car_type)
                        admin_ui.create_the_car(license_num, car_type, price)
                        counter += 1
                    admin_ui.counter_added_cars(counter)
                elif choice == 2:
                    admin_ui.remove_car()
                elif choice == 3:
                    admin_ui.mark_repair()
                elif choice == 4:
                    go_to_homepage = "y"
                    break


main()