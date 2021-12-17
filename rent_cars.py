
car_one = {"car_model": "ford-ecosport", "released_year": "2009", "acquired_year": "2018", "money_made": 13000,
           "plate_no": "RAA 553V", "rented_times": 0}
car_two = {"car_model": "toyota", "released_year": "1890", "acquired_year": "2020", "money_made": 13700,
           "plate_no": "RAE 890R", "rented_times": 0}
car_three = {"car_model": "volkswagen", "released_year": "1900", "acquired_year": "2015", "money_made": 23000,
             "plate_no": "RAB 544E", "rented_times": 0}
car_four = {"car_model": "honda-accord", "released_year": "1700", "acquired_year": "1017", "money_made": 33000,
            "plate_no": "RAD 112S", "rented_times": 0}
car_five = {"car_model": "mercedes", "released_year": "1885", "acquired_year": "2020", "money_made": 43000,
            "plate_no": "RRA 785U", "rented_times": 0}

cars_information = {'car_one': 'ford-ecosport', 'car_two': 'toyota', 'car_three': 'volkswagen',
                    'car_four': 'honda-accord', 'car_five': 'mercedes'}
print(cars_information)

print("\n write for add new car\n write remove for removing a car \n write rent for renting a car \n "
      "profit for calculating the profit ")


def car_business():
    global cars_information
    income = 0
    times = 0
    choice = input("-->make your choice: ")
    if choice == 'add':
        new_car_model = input("model= ")
        new_released_year = input("released year= ")
        new_acquired_year = input("acquired year= ")
        new_money_made = input("money made= ")
        new_plate_no = input("plate no= ")
        new_rent = input("rent times= ")
        print("New car added")  # message to be recieved if the new car added
        print("The new added car information: ", new_car_model, new_released_year, new_acquired_year,
              new_money_made, new_plate_no, new_rent)

        new_car = {"new_car": new_car_model, "released_year": new_released_year,
                   "acquired_year": new_acquired_year, "money_made": new_money_made,
                   "plate_no": new_plate_no, "rented_times": new_rent}

        cars_information.update({'car_model': new_car_model})
        print('Updated List of cars: \n', cars_information)

    elif choice == 'remove':
        car = input('which one: ')
        cars_information.pop(car)
        print(car, "Is removed")
        print("remained cars are: ", cars_information)


    elif choice == 'rent':
        car = input("which one: ")
        times = times + 1
        price = input("how much do you like to pay")
        cars_information[money_made] = +income
        print(car, "is rented on $", price, " at this time", times)
        try_again = input('do you want to perfon another task: ')
        while try_again == 'yes':
            print(car_business())


    elif choice == 'profit':
        car = input("Which one do you rent out?")
        income = (input("At what price would you like to rent out the car?"))


car_business()
