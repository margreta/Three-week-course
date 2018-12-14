class Car: 
    def __init__(self, license_num, car_type, price, status = "Available"):
        self.car_type = car_type
        self.license_num = license_num
        self.price = price
        self.status = status

    def get_car_type(self):
        return self.car_type

    def get_status(self):
        return self.status

    def get_license_num(self):
        return self.license_num
    
    def get_price(self):
        return self.price

    def __str__(self):
        return "{}, {}, {}, {}".format(self.license_num, self.car_type, self.price, self.status)

    def __repr__(self):
        return self.__str__()

 