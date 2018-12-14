
class Booking():
    def __init__(self, name, driver_license, email, phone_num, card_insurance, start_date, end_date, license_plate, car_type, price, extras, payment_type, booking_status):
        self.name = name
        self.driver_license = driver_license
        self.email = email
        self.phone_num = phone_num
        self.card_insurance = card_insurance
        self.start_date = start_date
        self.end_date = end_date
        self.license_plate = license_plate
        self.car_type = car_type
        self.price = price
        self.extras = extras
        self.payment_type = payment_type
        self.booking_status = booking_status

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.name, self.driver_license, self.email, self.phone_num,
                                                                    self.card_insurance, self.start_date, self.end_date, 
                                                                    self.license_plate, self.car_type, self.price,
                                                                    self.extras, self.payment_type, self.booking_status)


    def get_name(self):
        return self.name
    
    def get_driver_license(self):
        return self.driver_license
    
    def get_email(self):
        return self.email
    
    def get_phone_num(self):
        return self.phone_num
    
    def get_card_insurance(self):
        return self.card_insurance
    
    def get_start_date(self):
        return self.start_date
    
    def get_end_date(self):
        return self.end_date
    
    def get_license_plate(self):
        return self.license_plate
    
    def get_car_type(self):
        return self.car_type
    
    def get_total_amount(self):
        return self.price
    
    def get_extras(self):
        return self.extras
    
    def get_payment(self):
        return self.payment_type
    
    def get_booking_status(self):
        return self.booking_status
