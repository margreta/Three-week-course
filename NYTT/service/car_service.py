from repository.car_repo import Car_Repo

class Car_Service:

    def __init__(self):
        self.__car_repos = Car_Repo()

    def add_cars(self, cars):
        if self.is_valid_car(cars):
            self.__car_repos.add_cars(cars)
    
    def is_valid_car(self, cars):
        return True

    
    #cb = create booking.
    def cb_show_available_cars(self, inp_car_type):
        return self.__car_repos.cb_show_available_cars(inp_car_type)

    
    def cb_show_cancel_car(self,name):
        return self.__car_repos.show_cancelled_rented_car(name)

    def cb_cancel_available(self,license_num):
        return self.__car_repos.cancel_available(license_num)

    def car_choice(self, car_pick):
        if car_pick == False:
            raise Exception
        self.__car_repos.mark_as_rented(car_pick)