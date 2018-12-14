from service.admin_service import Admin_service
from service.car_service import Car_Service
from repository.car_repo import Car_Repo
from models.car import Car

class Admin_Ui:
    def __init__(self):
        self.admin_service = Admin_service()
        self.__car_service = Car_Service()
        self.car_repo = Car_Repo()

    def admin_home_page(self):
        """interface that admin can access"""
        #Header
        print("ADMIN")
        print("-" *20)

        print("Choose action: ")
        
        choice = 7
        while choice not in range(1,5):
            try: 
                choice = int(input("1. Create new car\n2. Remove car\n3. Mark car for repair\n4. Log out\n "))
                print("")
                self.admin_service.home_check(choice)
            except:
                print("Invalid action, please select number from 1 to 4")
                print("")
        return choice
    
    def remove_car(self):
        #Header
        print("ADMIN/Remove car")
        print("-" *20)
        
        confirm = "y"
        while confirm == "y":
            license_num = input("Please enter license plate number of car to remove from system: ").upper()
            
            confirm_inp = "a"
            no_fails = True
            while no_fails:
                try:
                    if confirm_inp not in "yn":
                        confirm_inp = input("Are you sure you want to remove {} from system? (y/n) ".format(license_num)).lower()
                        self.admin_service.y_and_n_validation(confirm_inp)
                        if confirm_inp == "y":
                            print("{} has been removed from system\n".format(license_num.upper()))
                            self.car_repo.remove_car(license_num) 
                        elif confirm_inp == "n":
                                break
                    elif confirm_inp == "y" or confirm_inp == "n":    
                        again = input("Do you want to remove another car? (y/n)")
                        self.admin_service.y_and_n_validation(again)
                        if again == "y":
                            confirm_inp = "a"
                            break
                        if again == "n":
                            no_fails = False
                            confirm = "n"
                except:
                    print("Please use 'y' or 'n' to confirm!")
         

          
    def mark_repair(self):
        print("Choose action: ")
        repair_choice = input("1. Mark in repair\n2. Mark out of repair\n ")
        repeat = "y"
        sure = "n"
        while repeat == "y":
            while sure == "n":
                license_num = input("Pleace enter the License plate number of car to mark for repair: ").upper()
                sure = input ("Are you sure you want to mark {0} for repair? (y/n) ".format(license_num)).lower()
                repeat = input("Would you like to mark another car for repair? (y/n) ").lower()
        self.car_repo.mark_repair(repair_choice,license_num)    
        
        

    def create_car_page(self): 
        print("ADMIN/Create new car")
        print("-" *20)

        confirm = "y"

        while confirm == "y":
            
            license_num = input("Please enter license plate number: ")
            
            car_type = " "
            while car_type not in "ABC":
                try:
                    car_type = input("Please enter car type (A, B, C) :").upper()
                    self.admin_service.car_type_check(car_type)
                except: 
                    print("Available types are A, B or C. Please choose one of those types!")
            print("")

            #initiate variables:
            confirm_inp = "a" 
            no_fails = True
            while no_fails:
                try:
                    if confirm_inp not in "yn":
                        confirm_inp = input("Confirm this car registration? (y/n) ")
                        print("")
                        self.admin_service.y_and_n_validation(confirm_inp)
                        if confirm_inp == "y":
                            print("The car {} has been added to system.\n".format(license_num.upper()))
                        elif confirm_inp == "n":
                            break
                    elif confirm_inp == "y" or confirm_inp == "n":
                        again = input("Would you like to add another car? (y/n)")
                        self.admin_service.y_and_n_validation(again)
                        if again == "y":
                            return license_num, car_type, confirm, again
                        if again == "n":
                            no_fails = False
                            confirm = "n"
                except:
                    print("Please use 'y' or 'n' to confirm!")
            
        print("")
        return license_num, car_type, confirm, again

    def counter_added_cars(self, counter):
        print("You have added {} car/s to the system.".format(counter))

    def create_the_car(self, license_num, car_type, price, status = "Available"):
        new_car = Car(license_num, car_type, price, status)
        self.__car_service.add_cars(new_car)
        