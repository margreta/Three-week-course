import datetime
from repository.car_repo import Car_Repo
from repository.booking_repo import Booking_Repo

class Dealer_service:
    def __init__(self):
        self.car_repo = Car_Repo()
        self.booking_repo = Booking_Repo()

    def home_check(self, choice):
        if choice not in range(1,6):
            raise Exception

    def option_check(self,contin):
        if contin != "1" and contin != "2":
            raise Exception

    #cb = Create booking. 
    def cb_check_name(self,first_name_alpha, last_name_alpha):       
        if first_name_alpha == False or last_name_alpha == False: 
            raise Exception

    def cb_check_driver_license(self, driver_license):
        driver = driver_license.isnumeric()
        len_driver_license = len(driver_license)
        if driver == False or len_driver_license != 9:
            raise Exception
        
    def cb_check_email(self,email):
        for letter in email: 
            if letter == "@": 
                email = True
                break
            else:
                email = False
        
        if email == False:
            raise Exception
    
    def cb_check_phone(self, phone_num):
        if phone_num == False:
            raise Exception

    def cb_check_card_num(self, card_num):
        len_card_num = len(card_num)
        card_num_numeric = card_num.isnumeric()
        if len_card_num < 16 or len_card_num > 16:
            raise Exception
        if card_num_numeric == False:
            raise Exception
    
    def create_booking_check_card_valid_time(self,start_date):
        if len(start_date) == 10:
            day = start_date[0:2] 
            month = start_date[3:5]
            year = start_date[6:]
        elif len(start_date) == 8:
            day = start_date[0]
            month = start_date[2]
            year = start_date[4:]
        if day not in range(1,32) or month not in range(1,13) or year < 2018:
            raise Exception

    def check_if_card_is_valid(self, validation_date): 
        tday = datetime.datetime.today()
        dt = datetime.datetime.strptime(validation_date, "%m/%y")
        end_date = dt - tday
        difference = end_date.days
        if difference < 0:
            raise Exception

    def cb_check_cvc(self,cvc):
        len_cvc = len(cvc)
        cvc_numeric = cvc.isnumeric()
        if len_cvc < 3 or len_cvc > 3: 
            raise Exception
        if cvc_numeric == False:
            raise Exception

    def valid_return(self, license_num):
        if license_num == False:
            raise Exception
        self.car_repo.return_rental(license_num)

    #Extras menu.
    def extras_menu_check(self,extras_option):
        if extras_option not in range (1,5):
            raise Exception 

    #Change booking.
    def change_check(self, change_choice):
        if change_choice not in range (1,4):
            raise Exception


#Edit booking.
    def edit_name(self, name):
        if name == False:
            raise Exception
        self.booking_repo.look_up_customer_by_name(name)#Kalla á fall sem les bara skrá enn breytir ekki.

    def edit_menu_check(self, edit_choice):
        if edit_choice not in range (1,6):
            raise Exception

    def edit_name_check(self,name,edit_name):
        self.booking_repo.edit_booking_name(name, edit_name)

    def edit_drivers_license_check(self,name,edit_drivers_license):
        self.booking_repo.edit_booking_driver_license(name, edit_drivers_license)

    def edit_email_check(self, name, edit_email):
        self.booking_repo.edit_booking_email(edit_email,name)

    def edit_phone_number(self,name,edit_phone_number):
        #Á eftir að gera villu check
        #Sigga
        self.booking_repo.edit_booking_phone_number(name, edit_phone_number)
    
    def edit_credit_card_insurance_check(self,edit_credit_card_info,name):
        self.booking_repo.edit_booking_credit_card_insurance(edit_credit_card_info,name)

    #Cancel booking.
    def cancel_check(self, name):
        if name == False:
            raise Exception
        self.booking_repo.cancel_booking(name)

    #Adding booking.
    def add_booking(self, booking):
        self.booking_repo.add_booking(booking)

    #check date.
    def obtain_date(self,start_date): 
         date_c = datetime.datetime.strptime(start_date, "%d/%m/%Y")
         if date_c == False:
             raise Exception


