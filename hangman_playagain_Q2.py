# This is kind of a break for you, very easy.
# Go to assignment one and refine your code for question 3.
# Again, use functions to do everything.
# Remember, a function does one and only one thing, and it does it perfectly.

# print("\nQuestions List\n")
# print(" 1.When was ALU founded\n 2.Who is the CEO of ALU\n 3.Where are ALU campuses\n"
#       " 4.How many campuses does ALU have\n 5.What is the name of ALU Rwanda’s Dean\n"
#       " 6.Who is in charge of Student Life\n 7.What is the name of our Lab\n"
#
#       " 8.How many students do we have in Year 2 CS\n 9.How many degrees does ALU offer\n"
#       " 10.Where are the headquarters of ALU \n")

player = input("Enter Your name : ")
print("Welcome in a game", player, "Now let's play :) \n")


def hangman():
    answer1 = 2015
    answer2 = 'Fred Swaniker'
    answer3 = 'Rwanda and Mauritius'
    answer4 = 2
    answer5 = 'Veda Sunassee'
    answer6 = 'Sila Ogidi'
    answer7 = 'Nigeria'
    answer8 = 96
    answer9 = 8
    answer10 = 'Mauritius'

    correct = 0  # declared  variable that is going to hold the numbers of correct answers
    incorrect = 0  # variable that is  going to hold the numbers of incorrect answers

    # the asked questions
    q1 = int(input("1.When was ALU founded? please enter a number: "))
    if q1 != answer1:  # checkes if the answer not true to what we have
        incorrect = incorrect + 1  # count the number of incorrect answer
        print("wrong answer. --> hanging a man...")  # result to returned

    else:  # checks  the answer is right to what we hold
        correct = correct + 1  # the code to count the number of correct answer/
        print("the answer is right")

    q2 = input("2.Who is the CEO of ALU: ")
    if q2 != answer2:
        incorrect = incorrect + 1
        print("wrong answer. --> hanging a man....")
    else:
        correct = correct + 1
        print("the answer is right")

    q3 = input("3.Where are ALU campuses?: ")
    if q3 != answer3:
        incorrect = incorrect + 1
        print("wrong answer. --> hanging a man....")
    else:
        correct = correct + 1
        print("the answer is right")

    q4 = int(input("4.How many campuses does ALU have? please enter a number: "))
    if q4 != answer4:
        incorrect = incorrect + 1
        print("wrong answer. --> hanging a man....")
    else:
        correct = correct + 1
        print("the answer is right")

    q5 = input("5.What is the name of ALU Rwanda’s Dean? : ")
    if q5 != answer5:
        incorrect = incorrect + 1
        print("wrong answer. --> hanging a man....")
    else:
        correct = correct + 1
        print("the answer is right")

    q6 = input("6.Who is in charge of Student Life? : ")
    if q6 != answer6:
        incorrect = incorrect + 1
        print("wrong! --> hanging a man....")
        if incorrect == 6:
            print("you lost The game is over")

            choice = 'no'  # this variable is create to help me know an answer of a player
            choice = input("do you want to play again ? : ")
            if choice == 'no':  # this statement is going to help me know if a player doesn't to continue
                print("The Marks of correct answer is : ", correct)
                print("Lost questions are : ", incorrect)
                exit()  # it will automatically end the game if the choice meet the condition
            while choice == 'yes': #this while loop is going to help me check if player's answer doesn't meet the above condition
                hangman() # if the player's choice is yes the while loop will go back and call my functions whic is where
                          # all asked question are passed through and bring them

    else:
        correct = correct + 1
        print("the answer is right?")

    q7 = input("7.What is the name of our Lab? : ")
    if q7 != answer7:
        incorrect = incorrect + 1
        print("wrong --> hanging a man....")

        if incorrect == 6:
            print("you lost The game is over")
            choice = 'no'
            choice = input("do you want to play again ? : ")
            if choice == 'no':
                print("The Marks of correct answer is : ", correct)
                print("Lost questions are : ", incorrect)
                exit()
            while choice == 'yes':
                hangman()

    else:
        correct = correct + 1
        print("the answer is right")

    q8 = int(input("8.How many students do we have in Year 2 CS? enter the number? please enter a number :"))
    if q8 != answer8:
        incorrect = incorrect + 1
        print("wrong!  --> hanging a man....")
        if incorrect == 6:
            print("you lost The game is over")
            choice = 'no'
            choice = input("do you want to play again ? : ")
            if choice == 'no':
                print("The Marks of correct answer is : ", correct)
                print("Lost questions are : ", incorrect)
                exit()
            while choice == 'yes':
                hangman()
    else:
        correct = correct + 1
        print("the answer is right")

    q9 = int(input("9.How many degrees does ALU offer? please enter a number? please enter a number : "))
    if q9 != answer9:
        incorrect = incorrect + 1
        print("wrong! --> hanging a man....")

        if incorrect == 6:
            print("you lost The game is over")
            choice = 'no'
            choice = input("do you want to play again ? : ")
            if choice == 'no':
                print("The Marks of correct answer is : ", correct)
                print("Lost questions are : ", incorrect)
                exit()
            while choice == 'yes':
                hangman()

    else:
        correct = correct + 1
        print("the answer is right")

    q10 = input("10.Where are the headquarters of ALU?: ")
    if q10 != answer10:
        incorrect = incorrect + 1
        print("wrong! --> hanging a man....")
        if incorrect == 6:
            print("you lost The game is over")
            choice = 'no'
            choice = input("do you want to play again ? : ")
            if choice == 'no':
                print("The Marks of correct answer is : ", correct)
                print("Lost questions are : ", incorrect)
                exit()
            while choice == 'yes':
                hangman()

    else:
        correct = correct + 1
        print("the answer is right")
        choice = input("do you want to contiue ? : ")
        if choice == 'no':
            print("The Marks of correct answer is : ", correct)
            print("Lost questions are : ", incorrect)
            exit()
        while choice == 'yes':
            hangman()

    print("congratulations", player, "You Won the Game!!!")
    print("The Marks of correct answer is : ", correct)
    print("Lost questions are : ", incorrect)


hangman()
