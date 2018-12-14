![Bear](Bear.png)>
## **T-113-VLN1, Verklegt námskeið 1, 2018-3**

![header1](header1.png)

## **Table of contents**
1. Introduction 
2. Data 
3. Video 
4. Authors 
5. Installation 


## **1. Introduction**
This program is a car-rental booking system that allows the car-rental company to easily create and manage bookings in addition to keeping the car fleet updated. The system has two paths, admin and dealer, where the admin has its own set of actions and the dealer another set. The admin is the controller or the one who can manipulate the fleet, for example adding a car, removing a ca and marking a car unavailable/available. The dealer is the one who interacts with the customer and is therefore the main user of the system.The systems purpose is to make every day work easier for those in the car-rental business.


## **2. Data**
The program uses two csv datasets, one named cars.csv and the other booking.csv.
You can find them [here](https://github.com/margreta/Three-week-course/tree/master/NYTT/data).



_**Cars.csv**_ contains information about all registered cars: 

License plate | *Type | Price | Status 
--------------|------|-------|--------
OFS45|A|4000|Available
SDE44|B|3000|Rented 

*Type refers to the category a car belongs to (A, B or C), as well as determining the price.


_**booking.csv**_ contains information about each and every customer who has ever made a booking with the car-rental company: 

Name | Drivers license | Email | Phone number | *Credit card information | Start date | End date | License plate | type | price | Extras | Billing type | Booking status  
-----|-----------------|-------|--------------|-------------------------|---------------|----------|---------------|------|-------|--------|--------------|---------------
Anna Einarsdóttir|123436000|annacool@gmail.com|8980032|4543843343242342|2/3/2018|5/3/2018|OFD73|A|4000|Car seat|Debit card|New
Sigga Guðmundsdóttir|123246999|siggacool@gmail.com|4324322|4232234234788764|10/10/2018|15/10/2018|KSA55|B|3000|Kasko insurance|Cash|Cancelled


*Credit card information stores the validation time of the car and the CVC number.



The system allows the user to look up specific data to find in either one of the datasets mentioned above. To illustrate, if the user needs to know the status of a car he or she can look it up by its license plate number and all information regarding that specific car will appear on the screen. As well as when the user needs to find a specific customer he or she can simply do so by entering the customers email and all information regarding that customer will then appear on the screen. 


## **3. Video**
The video below is an introduction to the car-rental system and its functions.
[here]()


## **4. Authors**
- Anna Valdís Einarsdóttir - BSc in Business Administration with a minor in Computer Science
- Arna María Ólafsdóttir - BSc in Business Administration with a minor in Computer Science
- Margrét Anna Ágústsdóttir - BSc Computer Science
- Sara Brynjólfsdóttir - BSc in Business Administration with a minor in Computer Science
- Sigríður Herdís Guðmundsdóttir - BSc in Business Administration with a minor in Computer Science

## **5. Installation**
The system runs on Python.\
Log-in guidance:
As a user one needs to know whether to log-in as an “Admin” or “Dealer”. The log-in username for Admin is “admin” and does not require a password, and the log-in username for Dealer is “dealer” and does not require a specific password.
