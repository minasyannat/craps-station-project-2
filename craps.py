import random
greeting = input("Welcome to the 'Die' casino, where your win is ours too! Are you ready to try your luck in a small game of throwing the dice? (yes/no) ").lower()

if greeting == 'yes':
    while True:
        inp = input("Look who's so couragious today! Press 'ENTER' to throw the dice!")
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        die_sum = die_1 + die_2
        first = f'The sum of your dices is {die_1} + {die_2} = {die_sum}'
        print(first)

        if (die_sum == 7) or (die_sum == 11):
            res = input(" you Won, my firend! Want to try again? (yes/no) ")
            if res == "no":
                break
            elif res == "yes":
                continue
        elif (die_sum == 2) or (die_sum == 3) or (die_sum == 12):
            res = input(" you lost, my firend! Want to try again? (yes/no) ")
            if res == "no":
                break
            elif res == "yes":
                continue
        else:
            result = input(f"The sum is {die_sum}! That is your new goal! Try to throw it again, but beware of the number 7! Press 'ENTER' to throw ")
            while True:
                die_1 = random.randint(1,6)
                die_2 = random.randint(1,6)
                die_sum_2 = die_1 + die_2
                print(f"The sum of your dice is {die_1} + {die_2} = {die_sum_2}")
                if die_sum_2 == 7:
                    print("Meh, bad luck, the sum is 7, you lost!")
                    break
                elif die_sum_2 == die_sum:
                    print("YOU WON FELLA! Great job!")
                    break
                input("press 'ENTER' to continue")
        break
            



