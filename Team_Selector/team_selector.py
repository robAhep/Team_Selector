#Team Allocator Game
import random

players = ["Robbie", "Sam", "Sean", "Chris",
           "Peter", "Amanda", "Emma", "Jen",
           "Suz", "Stella"]
print("Welcome to Team/Player Selector!")
while True:
    random.shuffle(players)
    team1 = players[:len(players)//2]
    print("Team 1 captain: "+random.choice(team1))
    print("Team 1:")
    for player in team1:
        print(player)
    team2  = players[len(players)//2:]
    print("\nTeam 2 captain: "+random.choice(team2))
    print("Team 2:")
    for player in team2:
        print(player)
 
    response = input("Pick teams again? Type y or n:")
    if response == "n":
         break
