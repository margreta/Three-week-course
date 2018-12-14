import csv
import os

from models.booking import Booking


class Booking_Repo: 
      

    #Overview action. Villumeðhöndlun vantar en það virkar að leita að viðskiptavini.
    def look_up_customer(self, email):
        with open("./data/booking.csv", encoding="utf-8") as booking_file:
            header = []
            for line in booking_file:
                list_line = line.strip().split(",")
                file_email = list_line[2]
                if file_email == "Email":
                    header.extend(list_line)
                elif file_email == email:
                    for x in range(13): 
                        print("{:>21}  {:<25}".format(header[x],list_line[x]))
                    break
            if file_email != email:
                print("Customer not found.")

                    
    
    def cancel_booking(self,name):
        with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
                fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                csv_writer.writeheader()

                for line in csv_reader:
                    if name in line.values():
                        line["Booking_status"] = "Cancelled"
                        csv_writer.writerow(line)
                    else:
                        csv_writer.writerow(line)

        os.remove("./data/booking.csv")
        os.rename("./data/new_booking.csv","./data/booking.csv")


    def add_booking(self, booking):
         with open("./data/booking.csv", "a+", encoding = "utf-8",newline="") as booking_file:
            name = booking.get_name()
            driver_license = booking.get_driver_license()
            email = booking.get_email()
            phone_num = booking.get_phone_num()
            card_insurance = booking.get_card_insurance()
            start_date = booking.get_start_date()
            end_date = booking.get_end_date()
            license_plate = booking.get_license_plate()
            car_type = booking.get_car_type()
            total_amount = booking.get_total_amount()
            extras = booking.get_extras()
            payment_type = booking.get_payment()
            booking_status = booking.get_booking_status()
            booking_file.write("{},{},{},{},{},{},{},{},{},${},{},{},{}\n".format(name, driver_license, email, phone_num,
                                                                                            card_insurance, start_date, end_date, license_plate,
                                                                                            car_type, total_amount, extras, payment_type, booking_status))

##########################################################################################################################
##########################################################################################################################


# EDIT BOOKING REPO STARTS HERE                                           


    def look_up_customer_by_name(self,name):
        with open("./data/booking.csv", encoding="utf-8") as booking_file:
            csv_reader = csv.DictReader(booking_file)

            for line in csv_reader:
                if name in line["Name"]:
                    print("Customer found.")


    # #Editing the name in "Edit booking"
    # def edit_booking_name(self,edit_name,name):
    #     with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
    #         csv_reader = csv.DictReader(csv_file)

    #         with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
    #             fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
    #             csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    #             csv_writer.writeheader()

    #             for line in csv_reader:
    #                 if name in line.values():
    #                     line["Name"] = edit_name  
    #                     csv_writer.writerow(line)
    #                 else:
    #                     csv_writer.writerow(line)

    #     os.remove("./data/booking.csv")
    #     os.rename("./data/new_booking.csv","./data/booking.csv")


    # #Editing the drivers license in "Edit booking"
    # def edit_booking_driver_license(self,edit_drivers_license,name):
    #     with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
    #         csv_reader = csv.DictReader(csv_file)

    #         with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
    #             fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
    #             csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    #             csv_writer.writeheader()

    #             for line in csv_reader:
    #                 if name in line.values():
    #                     line["Drivers_license"] = edit_drivers_license  
    #                     csv_writer.writerow(line)
    #                 else:
    #                     csv_writer.writerow(line)

    #     os.remove("./data/booking.csv")
    #     os.rename("./data/new_booking.csv","./data/booking.csv")


    # #Editing the email in "Edit booking"
    # def edit_booking_email(self,edit_email, name):
    #     with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
    #         csv_reader = csv.DictReader(csv_file)

    #         with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
    #             fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
    #             csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    #             csv_writer.writeheader()

    #             for line in csv_reader:
    #                 if name in line.values():
    #                     line["Email"] = edit_email
    #                     csv_writer.writerow(line)
    #                 else:
    #                     csv_writer.writerow(line)

    #     os.remove("./data/booking.csv")
    #     os.rename("./data/new_booking.csv","./data/booking.csv")

    # #Editing the phone number in "Edit booking"
    # def edit_booking_phone_number(self,edit_phone_number,name):
    #     with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
    #         csv_reader = csv.DictReader(csv_file)

    #         with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
    #             fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
    #             csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    #             csv_writer.writeheader()

    #             for line in csv_reader:
    #                 if name in line.values():
    #                     line["Phone_number"] = edit_phone_number #The edit phone is found in the ui layer
    #                     csv_writer.writerow(line)
    #                 else:
    #                     csv_writer.writerow(line)

    #     os.remove("./data/booking.csv")
    #     os.rename("./data/new_booking.csv","./data/booking.csv")


    # #Editing the credit card insurance in "Edit booking"
    # def edit_booking_credit_card_insurance(self,edit_credit_card_info, name):
    #     with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
    #         csv_reader = csv.DictReader(csv_file)

    #         with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
    #             fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
    #             csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    #             csv_writer.writeheader()

    #             for line in csv_reader:
    #                 if name in line.values():
    #                     line["Credit_card_insurance"] = edit_credit_card_info #The edit_credit_card_info is found in the ui layer
    #                     csv_writer.writerow(line)
    #                 else:
    #                     csv_writer.writerow(line)

    #     os.remove("./data/booking.csv")
    #     os.rename("./data/new_booking.csv","./data/booking.csv")

    # #Editing the start date in "Edit booking"
    # def edit_booking_start_date(self,edit_start_date, name):
    #     with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
    #         csv_reader = csv.DictReader(csv_file)

    #         with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
    #             fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
    #             csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    #             csv_writer.writeheader()

    #             for line in csv_reader:
    #                 if name in line.values():
    #                     line["Start_date"] = edit_start_date #The edit_start_date is found in the ui layer
    #                     csv_writer.writerow(line)
    #                 else:
    #                     csv_writer.writerow(line)

    #     os.remove("./data/booking.csv")
    #     os.rename("./data/new_booking.csv","./data/booking.csv")

    # #Editing the end_date in "Edit booking"
    # def edit_booking_end_date(self,edit_end_date,name):
    #     with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
    #         csv_reader = csv.DictReader(csv_file)

    #         with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
    #             fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
    #             csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    #             csv_writer.writeheader()

    #             for line in csv_reader:
    #                 if name in line.values():
    #                     line["End_date"] = edit_end_date #The edit_end_date is found in the ui layer
    #                     csv_writer.writerow(line)
    #                 else:
    #                     csv_writer.writerow(line)

    #     os.remove("./data/booking.csv")
    #     os.rename("./data/new_booking.csv","./data/booking.csv")


    # #Editing the extras in "Edit booking"
    # def edit_booking_extras(self,edit_extras,name):
    #     with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
    #         csv_reader = csv.DictReader(csv_file)

    #         with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
    #             fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
    #             csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    #             csv_writer.writeheader()

    #             for line in csv_reader:
    #                 if name in line.values():
    #                     line["Extras"] = edit_extras #The edit_extras is found in the ui layer
    #                     csv_writer.writerow(line)
    #                 else:
    #                     csv_writer.writerow(line)

    #     os.remove("./data/booking.csv")
    #     os.rename("./data/new_booking.csv","./data/booking.csv")

    # #Editing the payment in "Edit booking"
    # def edit_booking_payment(self,edit_payment,name):
    #     with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
    #         csv_reader = csv.DictReader(csv_file)

    #         with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
    #             fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
    #             csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    #             csv_writer.writeheader()

    #             for line in csv_reader:
    #                 if name in line.values():
    #                     line["Payment"] = edit_payment #The edit_extras is found in the ui layer
    #                     csv_writer.writerow(line)
    #                 else:
    #                     csv_writer.writerow(line)

    #     os.remove("./data/booking.csv")
    #     os.rename("./data/new_booking.csv","./data/booking.csv")

#########################################################################################################################
#########################################################################################################################


    def edit_booking(self, what_change, edit_name, edit_driver_license, edit_email, edit_phone_number, edit_credit_card_insurance, edit_start_date, edit_end_date, edit_extras, edit_payment):
        with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open("./data/new_booking.csv", "a+", encoding="utf-8",newline="") as new_file:
                fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                csv_writer.writeheader()

                #Edit booking
                for line in csv_reader:
                    #If changing name
                    if what_change == 1: #what_change is an option given in the ui layer
                        if edit_name in line.values():
                            line["Name"] = edit_name #edit_name is the input we get in the ui layer
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)
                    #If changing drivers license number
                    if what_change == 2:
                        if edit_driver_license in line.value():
                            line ["Drivers_license"] = edit_driver_license #edit_drivers license is the input we get in the ui layer
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)
                    #If changing email
                    if what_change == 3:    
                        if edit_email in line.value():
                            line["Email"] = edit_email #edit_email is the input we get in the ui layer
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)
                    #If changing phone number      
                    if what_change == 4:         
                        if edit_phone_number in line.value():
                            line["Phone_number"] = edit_phone_number #edit_phone_number is the input we get in the ui layer                               
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)
                    #If changing credit card insurance
                    if what_change == 5:
                        if edit_credit_card_insurance in line.value(): #edit_credit_card_insurance is the input we get in the ui layer
                            line["Credit_card_insurance"] = edit_credit_card_insurance                                 
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)                                      
                    #If changing start date
                    if what_change == 6:
                        if edit_start_date in line.value(): #edit_start_date is the input we get in the ui layer
                            line["Start_date"] = edit_start_date                             
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)                
                    #If changing amount of days (or end_date)
                    if what_change == 7:
                        if edit_end_date in line.value(): #edit_end_date is the input we get in the ui layer
                            line["End_date"] = edit_end_date                               
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)    
                    #If changing extras
                    if what_change == 8:
                        if edit_extras in line.value(): #edit_extras is the input we get in the ui layer
                            line["Extras"] = edit_extras                          
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line) 
                    #If changing payment
                    if what_change == 9:
                        if edit_payment in line.value(): #edit_payment is the input we get in the ui layer
                            line["Payment"] = edit_payment
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)                             


        os.remove("./data/booking.csv")
        os.rename("./data/new_booking.csv","./data/booking.csv")        

