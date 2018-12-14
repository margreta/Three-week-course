from service.dealer_service import Dealer_service

class Return_Rental:

    def __init__(self):
        self.__dealer_service = Dealer_service()

    def return_rental_ui(self):
        license_num = False
        while license_num == False:
            try:
                license_num = input("Insert license plate: ")
                self.__dealer_service.valid_return(license_num)
                print("{} has been returned".format(license_num.upper()))
                print("")
                license_num = True
            except:
                print("License plate number does not exist in the system, please enter a valid number.")
                print("")
        return license_num