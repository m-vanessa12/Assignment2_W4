my_cars = {"ford-ecosport": [2009, 2018, 1300, "RAA 553V", 0],
           "toyota": [1890.2020, 13700, "RAE 890R,0"],
           "volkswagen": [1900, 2015, 23000, "RAB 544R", 0],
           "honda-accord": [1700, 1017, 33000, "RAD 112S", 0],
           "mercedes": [1885, 2020, 43000, "RRA 785U", 0]}
rented_cars = []


def remove():
    for item in my_cars.keys():
        print(item)
        car_to_remove = input("Enter the name of the car you want to remove")
        del my_cars[car_to_remove]


def rent():
    for item in my_cars.keys():
        print(item)
        car_to_rent = input("Enter the car you want to rent")
        if car_to_rent in my_cars.keys():
            amount = int(input("Enter the amount you want to rent the car"))
            print(f"You decided to rent out {car_to_rent},at rwf {amount}, times in business:{my_cars[car_to_rent][4]}")
            rented_cars.append(my_cars[car_to_rent])
            del my_cars[car_to_rent]

            break
        else:
            print("The car does not exist")
            break


def check_profit():
    for key, value in my_cars.items():
        # print()
        print(f"car:{key},amount_made:{value[2]},no of times in business:{value[0]}")


def add_cars():
    new_car_model = input("model= ")
    new_released_year = int(input("released year= "))
    new_acquired_year = int(input("acquired year= "))
    new_money_made = int(input("money made= "))
    new_plate_no = input("plate no= ")
    new_rent = input("rent times= ")
    times_in_business = int(input("The number of times in business"))
    my_cars[new_car_model] = [new_released_year, new_acquired_year, new_money_made, new_plate_no, times_in_business]
    print(f"New car added:{new_car_model}, number plate{new_plate_no},")  # message to be recieved if the new car added
    print("updated list of cars")
    for key, value in my_cars.items():
        print(key, value)


# add_cars()
def start():
    print("Omondi services\n 1.Add car\n2.rent car\n3.check_profit\nremove car")
    task = input("Enter the task you wnt to perform, 1-4")

    if task == "1":
        add_cars()
    elif task == "2":
        rent()
    elif task == "3":
        check_profit()
    elif task == "4":
        remove()
    else:
        print("try again")


def multitasking():
    c = True
    while c:
        start()
        another = input("Do you want to perform another task y/n")
        if another == "n":
            c = False


multitasking()
