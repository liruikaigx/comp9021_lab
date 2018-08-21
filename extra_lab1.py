'''
Simulates the cast of an unknown die, chosen from a set of 5 dice with 4, 6, 8, 12, and 20 sides.

To start with, every die has a probability of 0.2 to be the chosen die.
At every cast, the probability of each die is updated using Bayes' rule.
The probabilities are displayed for at most 6 casts.
If more than 6 casts have been requested, the final probabilities obtained
for the chosen number of casts are eventually displayed.
'''


from random import choice, seed
import sys



while True:
    try:
        for_seed = int(input('Enter the seed: '))
        seed(for_seed)
        break
    except ValueError:
        pass
dice = [4, 6, 8, 12, 20]
P_list = [0.2] * 5
chosen_dice = choice(dice)          

        
cast = int(input('Enter the desired number of times a randomly chosen die will be cast: ')) 
print(f'\nThis is a secret, but the chosen die is the one with {chosen_dice} faces')


outcome_list = []
c = 1
for c in range(cast):
    for i in range(1, chosen_dice+1):
        outcome_list.append(i)
    outcome = choice(outcome_list)
    print(f'\nCasting the chosen die... Outcome: {outcome}')

    if outcome <= 4:
        PB_list = []
        for d in range(5):
            PB_list.append(1/dice[d] * P_list[d])
        PB = sum(PB_list)

        print('The updated dice probabilities are:')
        for x in range(5):
            P = (1/dice[x] * P_list[x]) / PB
            if dice[x] < 10:
                print(f'     {dice[x]}: {P*100:0.2f}%')
            else:
                print(f'    {dice[x]}: {P*100:0.2f}%')
            P_list[x] = P
    elif outcome > 4 and outcome <= 6:
        P_list[0] = 0
        PB_list = []
        for d in range(1, 5):
            PB_list.append(1/dice[d] * P_list[d])
        PB = sum(PB_list)

        print('The updated dice probabilities are:')
        for x in range(5):
            P = (1/dice[x] * P_list[x]) / PB
            if dice[x] < 10: 
                print(f'     {dice[x]}: {P*100:0.2f}%')
            else:
                print(f'    {dice[x]}: {P*100:0.2f}%')
            P_list[x] = P
    elif outcome > 6 and outcome <= 8:
        P_list[0] = 0
        P_list[1] = 0
        PB_list = []
        for d in range(2, 5):
            PB_list.append(1/dice[d] * P_list[d])
        PB = sum(PB_list)

        print('The updated dice probabilities are:')
        for x in range(5):
            P = (1/dice[x] * P_list[x]) / PB
            if dice[x] < 10:
                print(f'     {dice[x]}: {P*100:0.2f}%')
            else:
                print(f'    {dice[x]}: {P*100:0.2f}%')
            P_list[x] = P
    elif outcome > 8 and outcome <= 12:
        P_list[0] = 0
        P_list[1] = 0
        P_list[2] = 0
        PB_list = []
        for d in range(3, 5):
            PB_list.append(1/dice[d] * P_list[d])
        PB = sum(PB_list)

        print('The updated dice probabilities are:')
        for x in range(5):
            P = (1/dice[x] * P_list[x]) / PB
            if dice[x] < 10:
                print(f'     {dice[x]}: {P*100:0.2f}%')
            else:
                print(f'    {dice[x]}: {P*100:0.2f}%')
            P_list[x] = P
    elif outcome >12 and outcome <= 20:
        P_list[0] = 0
        P_list[1] = 0
        P_list[2] = 0
        P_list[3] = 0
        PB_list = []
        for d in range(5):
            PB_list.append(1/dice[d] * P_list[d])
        PB = sum(PB_list)

        print('The updated dice probabilities are:')
        for x in range(5):
            P = (1/dice[x] * P_list[x]) / PB
            if dice[x] < 10:
                print(f'     {dice[x]}: {P*100:0.2f}%')
            else:
                print(f'    {dice[x]}: {P*100:0.2f}%')
            P_list[x] = P