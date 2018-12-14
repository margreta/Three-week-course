from repository.car_repo import Car_Repo


class Admin_service:
    def __init__(self):
        self.car_repo = Car_Repo

    def home_check(self, choice):
        if choice not in range(1,6):
            raise Exception

    def car_type_check(self, car_type):
        if car_type not in "ABC":
            raise Exception

    def y_and_n_validation(self, choice):
        if choice not in "y,n":
            raise Exception
    
