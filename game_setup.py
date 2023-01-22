from game_war.player import Player
from game_war.desk import Desk
from game_war.card import Card

player_one = Player("One")
player_two = Player("Two")


new_desk = Desk()
new_desk.shuffle()


game_on = True

round_num = 0


for x in range(26):
    player_one.add_cards(new_desk.deal_one())
    player_two.add_cards(new_desk.deal_one())

print(player_one.remove_one())

while game_on:
    round_num += 1

    # Game over
    if len(player_one.all_card) == 0 or len(player_two.all_card) == 0:
        # Who win ?
        player_win = "One" if len(player_two.all_card) == 0 else "Two"
        Player_lose = "One" if len(player_one.all_card) == 0 else "Two"

        print(f"Player {Player_lose}, out of cards! Player {player_win} Wins!")
        break

    print(f"Round {round_num}")
    print("Fight")
    # Player a new round
    # Show card to fight
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
         if player_one_cards[-1].value > player_two_cards[-1].value:
             # player 1 win round, Player One get all card was bet
             player_one.add_cards(player_one_cards)
             player_one.add_cards(player_two_cards)

             at_war = False
          
         elif player_one_cards[-1].value < player_two_cards[-1].value:
             # player 2 win round, Player One get all card was bet
             player_two.add_cards(player_one_cards)
             player_two.add_cards(player_two_cards)

             at_war = False
         else:
             print("WAR!")

             if len(player_one.all_card) < 5:
                 print("Player One unable to declare war")
                 print("PLAYER TWO WIN!")
                 game_on = False
                 break
             elif len(player_two.all_card) < 5:
                 print("Player TWO unable to declare war")
                 print("PLAYER ONE WIN!")
                 game_on = False
                 break
             else:
                 for num in range(5):
                     player_one_cards.append(player_one.remove_one())
                     player_two_cards.append(player_two.remove_one())
                 break
             



