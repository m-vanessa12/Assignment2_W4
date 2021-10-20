# Omondi is starting a new business, a car renting business.
# Omondi starts with five different Cars.
# Each car has a model, a year when it was released, a year when Omondi acquired it,
# the money made from that car, the car's plate number, and the number of times that ' \
# 'it has been in business. (It has been rented).
# As Omondi is looking into expansion, he wants to be able to rent the cars,
# add new cars to his collection, remove the cars from his collection, count
# the number that each car has been rented out, and the money made from each car.
# Please help Omondi.
# ----------------------------------------------------------------------------------------------------------


class Car:  # parent class

    def __init__(self, car_model, released_year, acquired_year, money_made, plate_no, rented_times):
        self.car_model = car_model
        self.released_year = released_year
        self.acquired_year = acquired_year
        self.money_made = money_made
        self.plate_no = plate_no
        self.rented_times = rented_times

    def car_business(self):
        print(self.car_model, self.released_year,
              self.acquired_year, self.money_made, self.plate_no, self.rented_times)


# instance of of car1
car_one = Car("ford-ecosport", "2009", "2018", "$13000", "RAA 553V", "0")
car_one.car_business()
# car_one.change_made()

# instance of car2
car_two = Car("toyota", "1890", "2020", " $13700 ", "RAE 890R", "0")
car_two.car_business()
# car_two.change_made()

# instance of car3
car_three = Car("volkswagen", "1900", "2015", " $23000 ", "RAB 544E", "0")
car_three.car_business()
# # car_two.change_made()

# instance of car4
car_four = Car("honda-accord", "1700", "1017", " $33000 ", "RAD 112S", "0")
car_four.car_business()
# car_two.change_made()

# instace of car5
car_five = Car("mercedes", "1885", "2020", "$43000", "RRA 785U", "0")
car_five.car_business()
# car_two.change_made

# this one is for adding all my objects/ instances or cars information into a list which will hold them
car_list = [car_one, car_two, car_three, car_four, car_five]


def menu_choice():
    global car_list
    change = (input("you want to remove car in your store car? ="))  # this code is going to let omodi make his choice on a car he want
    # to remove

    if change == 'yes':
        choice = input("which one do you want to remove? =")
        if choice == 'car_one':
            car_list.remove(car_one)  # remove select car_one in store
            print("car removed")
            print(car_list)

        elif choice == 'car_two':
            car_list.remove(car_two)
            print("car removed")
            print(car_list)

        elif choice == 'car_three':
            car_list.remove(car_three)
            print("car removed")
            print(car_list)

        elif choice == 'car_four':
            car_list.remove(car_four)
            print("car removed")
            print(car_list)

        elif choice == 'car_five':
            car_list.remove(car_five)
            print("car removed")
            print(car_list)

# write a func call check; lst = [car1,.. car5] if


        else:
         exit()

    add = (input("you want to add car in your store car? ="))  # this code is going to let Omodi add a new car
    if add == 'yes':  # cheching an answer if it meet the condition
        new_car_model = input("model= ")
        new_released_year = input("released year= ")
        new_acquired_year = input("acquired year= ")
        new_money_made = input("money made= ")
        new_plate_no = input("plate no= ")
        new_rent = input("rent times= ")
        print("New car added")  # message to be recieved if the new car added
        print("The new added car information: ", new_car_model, new_released_year, new_acquired_year, new_money_made,
              new_plate_no, new_rent)

        # new_car=... this the created object for just a new aaded car
        new_car = Car(new_car_model, new_released_year, new_acquired_year, new_money_made, new_plate_no, new_rent)
        new_car.car_business()


    rent_time = 0
    rent = (input("Is a car going to be rented? ="))  # this code is going to let Omodi add a new car
    if rent == 'yes':
        input("Which one?= ")
        car_info='car_one'
        while car_info=='car_one' and rent_time==0:

        # if car_info == "car_one":
         rent_time =rent_time + 1
         print("rented times of car_one= ",rent_time)

        else:
            exit()


    other=input("Do you want to do other change?=")
    if other=='no':
         exit()
    while other=='yes':
        menu_choice()



menu_choice()


