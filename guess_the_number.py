import random

print("Let's Play" + ' "Guess The Number" Game :)')

computer_choose = random.randint(1, 10)

player_choose = int(input("Pick a number between [1] and [10] "))
player_moves_cnt = 5
player_choose_cnt = 0

while player_choose != computer_choose:

    if player_choose <= 0 or player_choose > 10:
        print("Invalid input!")
        print("Pick a number in correct range!")
        player_choose = int(input())

    if player_choose < computer_choose:
        player_moves_cnt -= 1
        player_choose_cnt += 1
        print("Your guess is too low!")
        print(f"You have {player_moves_cnt} turns left.")
        player_choose = int(input())
    elif player_choose > computer_choose:
        player_moves_cnt -= 1
        player_choose_cnt += 1
        print("Your guess is too high!")
        print(f"You have {player_moves_cnt} turns left.")
        player_choose = int(input())

    if player_moves_cnt == 0:
        print(f"Opps!! No turns left. My number was {computer_choose}")
        break

else:
    player_choose_cnt += 1
    print(f"It took you {player_choose_cnt} turns to guess my number, wich was {computer_choose}.")
