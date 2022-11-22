import random
print("\n------------------- HAND CRICKET ------------------")

lst1 = [1, 2, 3, 4, 5, 6]

chances = int(input("\n\tEnter the over you want to play :"))

chances_1 = 0
no_of_chances_1 = 0
your_runs = 0
no_of_chances_2 = 0
comp_runs = 0
num = 0
user_toss_res = 0
comp_toss_res = 0

if chances <= 0:
    print("\n\tPlease enter a number greater than zero")
else:
    chances_1 = chances * 6

toss = ['ODD', 'EVEN']
user_toss = input("Enter your choice ODD/EVEN..? :").upper()
if user_toss == 'ODD':
    comp_toss = 'EVEN'
else:
    comp_toss = 'ODD'
user_toss_num = int(input("Enter your number for toss b/w 6..:"))
comp_toss_num = random.choice(lst1)

if user_toss == 'EVEN' and ((user_toss_num + comp_toss_num) % 2 == 0):
    print("User won the toss...")
    user_toss_res = 1
elif user_toss == 'ODD' and ((user_toss_num + comp_toss_num) % 2 == 1):
    print("User won the toss...")
    user_toss_res = 1
else:
    print("computer won the toss...")
    comp_toss_res = 1

if user_toss_res == 1:
    num = 1
    print(
        "---------------------------------------\n\t\t-- Your Batting --\n---------------------------------------")
    while no_of_chances_1 < chances_1:

        user_runs = int(input("\tEnter Runs for Your Batting Turn: "))
        comp_bowl = random.choice(lst1)

        if user_runs == comp_bowl:
            print("\tYour Guess: ", user_runs, ",\tComputer Guess: ", comp_bowl)
            print("\tYOU ARE OUT...!!"
                  "\n\tYour Total Runs = ", your_runs, "\n")
            no_of_chances_1 = no_of_chances_1 + 1
            break
        elif user_runs > 6:
            print("ALERT!! Support Number only till 6\n")
            continue
        else:
            your_runs = your_runs + user_runs
            print("\tYour Guess: ", user_runs, ",\tComputer Guess: ", comp_bowl)
            print("\tYour runs Now are: ", your_runs, "\n")
            no_of_chances_1 = no_of_chances_1 + 1



else:

    lst2 = [1, 2, 3, 4, 5, 6]

    chances_2 = chances_1

    print(
        "---------------------------------------\n\t\t-- Computer Batting --\n---------------------------------------")
    while no_of_chances_2 < chances_2:

        user_bowl = int(input("\tEnter Runs for Your Bowling Turn: "))
        comp_bat = random.choice(lst2)

        if comp_bat == user_bowl:
            print("\tComputer Guess: ", comp_bat, ",\tYour Guess: ", user_bowl)
            print("\tTHE COMPUTER IS OUT.... "
                  "\n\tComputer Runs= ", comp_runs, "\n")
            no_of_chances_2 = no_of_chances_2 + 1
            break
        elif user_bowl > 6:
            print("ALERT!! Support Number only till 6\n")
            continue
        else:
            comp_runs = comp_runs + comp_bat
            print("\tComputer Guess: ", comp_bat, ",\tYour Guess: ", user_bowl)
            print("\tComputer Runs: ", comp_runs, "\n")
            no_of_chances_2 = no_of_chances_2 + 1



if num == 1:
    lst2 = [1, 2, 3, 4, 5, 6]

    chances_2 = chances_1

    print(
        "---------------------------------------\n\t\t-- Computer Batting --\n---------------------------------------")
    while no_of_chances_2 < chances_2:

        user_bowl = int(input("\tEnter Runs for Your Bowling Turn: "))
        comp_bat = random.choice(lst2)

        if comp_bat == user_bowl:
            print("\tComputer Guess: ", comp_bat, ",\tYour Guess: ", user_bowl)
            print("\tTHE COMPUTER IS OUT.... "
                  "\n\tComputer Runs= ", comp_runs, "\n")
            no_of_chances_2 = no_of_chances_2 + 1

            break
        elif user_bowl > 6:
            print("ALERT!! Support Number only till 6\n")
            continue
        else:
            comp_runs = comp_runs + comp_bat
            print("\tComputer Guess: ", comp_bat, ",\tYour Guess: ", user_bowl)
            print("\tComputer Runs: ", comp_runs, "\n")
            no_of_chances_2 = no_of_chances_2 + 1


            if comp_runs > your_runs:
                break


else:
    num = 1
    print(
        "---------------------------------------\n\t\t-- Your Batting --\n---------------------------------------")
    while no_of_chances_1 < chances_1:

        user_runs = int(input("\tEnter Runs for Your Batting Turn: "))
        comp_bowl = random.choice(lst1)

        if user_runs == comp_bowl:
            print("\tYour Guess: ", user_runs, ",\tComputer Guess: ", comp_bowl)
            print("\tYOU ARE OUT...!!"
                  "\n\tYour Total Runs = ", your_runs, "\n")
            no_of_chances_1 = no_of_chances_1 + 1
            break
        elif user_runs > 6:
            print("ALERT!! Support Number only till 6\n")
            continue
        else:
            your_runs = your_runs + user_runs
            print("\tYour Guess: ", user_runs, ",\tComputer Guess: ", comp_bowl)
            print("\tYour runs Now are: ", your_runs, "\n")
            no_of_chances_1 = no_of_chances_1 + 1
            if comp_runs < your_runs:
                break


print("\n-----------------------\n\t-- RESULTS: --\n-----------------------")

if comp_runs < your_runs:
    print("\nYOU WON THE GAME....\n\nYour Total Runs= ", your_runs, " \t [Bowls taken(Out of ", chances_1, "): ",
          no_of_chances_1, "]", "\nComputer Total Runs= ", comp_runs, " \t [Bowls Taken(Out of ", chances_1, "): ",
          no_of_chances_2,
          "]\n")

elif comp_runs == your_runs:
    print("The Game is a Tie")

else:
    print("\nCOMPUTER WON THE GAME....\n\nComputer Total Runs= ", comp_runs, " \t [Bowls Taken(Out of ", chances_1,
          "): ",
          no_of_chances_2, "]", "\nYour Total Runs= ", your_runs, " \t [Bowls taken(Out of ", chances_1, "): ",
          no_of_chances_1, "]\n")
