import csv
from models.car import Car
import os

class Car_Repo:

    def add_cars(self, car):
        with open("./data/car.csv", "a") as cars_file:
            license_num = car.get_license_num()
            car_type = car.get_car_type()
            price = car.get_price()
            status = car.get_status()
            cars_file.write("{},{},{},{}\n".format(license_num.upper(), car_type.upper(),price, status))

    def mark_repair(self, repair_choice, license_num):
        with open("./data/car.csv", "r+") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open("./data/new_cars.csv", "a+",newline="") as new_file:
                fieldnames = ["License_plate", "Type", "Price","Status"]

                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                csv_writer.writeheader()

                for line in csv_reader:
                    if repair_choice == "1":
                        if license_num in line.values():
                            line["Status"] = "Unavailable"
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)
                    elif repair_choice == "2":
                        if license_num in line.values():
                            line["Status"] = "Available"
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)

        os.remove("./data/car.csv")
        os.rename("./data/new_cars.csv","./data/car.csv")

    def remove_car(self, license_num):

        with open("./data/car.csv", "r+") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open("./data/new_cars.csv", "a+",newline="") as new_file:
                fieldnames = ["License_plate", "Type", "Price","Status"]
            
                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                csv_writer.writeheader()

                for line in csv_reader:
                    if license_num not in line.values():
                        csv_writer.writerow(line)
        os.remove("./data/car.csv")
        os.rename("./data/new_cars.csv","./data/car.csv")

    def cb_show_available_cars(self, inp_car_type):
        with open("./data/car.csv", "r+") as cars_file:
            for line in cars_file.readlines():

                license_num, car_type, price, status = line.strip().split(",")

                if status == "Available" and car_type == inp_car_type:
                    print("{:<15}{:<6}{:<7}{:<10}".format(license_num, car_type, price, status))
    

    def return_rental(self, license_num):
        with open("./data/car.csv", "r+") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open("./data/new_cars.csv", "a+", newline="") as new_file:
                fieldnames = ["License_plate", "Type", "Price","Status"]

                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                csv_writer.writeheader()

                for line in csv_reader:
                    if license_num in line.values():
                        line["Status"] = "Available"
                        csv_writer.writerow(line)
                    else:
                        csv_writer.writerow(line)


        os.remove("./data/car.csv")
        os.rename("./data/new_cars.csv","./data/car.csv")

    #Overview action.  
    def show_available_cars(self, car_choice):
        with open("./data/car.csv", "r") as cars_file:
            for line in cars_file.readlines():

                license_num, car_type, price, status = line.strip().split(",")
                if car_choice == 1:
                    if status == "Available":
                        print("{:<15}{:<6}${:<7}{:<10}".format(license_num, car_type, price, status))
                elif car_choice == 2:
                    if status == "Rented":
                        print("{:<15}{:<6}${:<7}{:<10}".format(license_num, car_type, price, status))

    #Overview action.
    def look_up_car(self, car_choice, license_number):
        with open("./data/car.csv", "r") as cars_file:
            header = []
            for line in cars_file:
                list_line = line.strip().split(",")
                file_car = list_line[0]
                if file_car == "License_plate":
                    header.extend(list_line)
                elif file_car == license_number:
                    for x in range(4): 
                        print("{:>21}  {:<25}".format(header[x],list_line[x]))
                    break
            if file_car != license_number:      
                print("Car not found.")          


    def mark_as_rented(self, car_pick):
        with open("./data/car.csv", "r+") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open("./data/new_cars.csv", "a+", newline="") as new_file:
                fieldnames = ["License_plate", "Type", "Price","Status"]

                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                csv_writer.writeheader()

                for line in csv_reader:
                    if car_pick in line.values():
                        line["Status"] = "Rented"
                        csv_writer.writerow(line)
                    else:
                        csv_writer.writerow(line)
    
        os.remove("./data/car.csv")
        os.rename("./data/new_cars.csv","./data/car.csv")

    def show_cancelled_rented_car(self,name):
        with open("./data/booking.csv", "r",encoding = "utf-8") as car_book_file:
            csv_reader = csv.DictReader(car_book_file)

            for line in csv_reader:
                if name in line.values():
                    license_num = (line["License_plate"])
                    return license_num


    def cancel_available(self, license_num):
        with open("./data/car.csv", "r+") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open("./data/new_cars.csv", "a+", newline="") as new_file:
                fieldnames = ["License_plate", "Type", "Price","Status"]

                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                csv_writer.writeheader()

                for line in csv_reader:
                    if license_num in line.values():
                        line["Status"] = "Available"
                        csv_writer.writerow(line)
                    else:
                        csv_writer.writerow(line)
    
        os.remove("./data/car.csv")
        os.rename("./data/new_cars.csv","./data/car.csv")
