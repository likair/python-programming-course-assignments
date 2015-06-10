'''
Created on Jun 3, 2015

    A program in which you implement a poker game. 

    In the program define a class called Player, whose instance variables are: name and stake 
    (decimal number). Define also the following 
    methods for the class:
    The constructor method
    The method which returns the object data as text.
    The play() method, which asks whether the user wants to play or not. If the user wants to play,
    then it generates a random number between 1 and 13 and adds it to variable points.
    
    Define also class Game, whose instance variable is two or more Player objects and its class 
    variable is game_status, which is a dictionary, so that its key is the name of each player 
    and its value is the collected points of the relevant player. Define also the following methods
    for the class:
    
    The constructor method
    The method which returns the object data as text.
    The start() method, which asks the user how many players want to play and then for each player 
    it should generate an instance of class Player and then keep on calling the play() method of 
    each player in order to generate a new random number for each player in turn. The program should
    continue until it finds the winner. The winner will be the player whose sum of generated random 
    numbers (cards) is equal to 21 or bigger but still less than 21.
    In the main program you should create an instance of class Game and call its methods to start 
    the game and print the results of the game.

@author: lebs
'''
import random

class Player:
    def play(self):
        if input(self.name + ', do you want to play? (y/n)') == 'y':
            random_number = random.randrange(1, 14)
            self.points += random_number
            print('# Your got ' + str(random_number) + ', and your sum is ' + str(self.points) + '.')
            return True
        return False
    def __init__(self, name=''):
        self.name = name
        self.points = 0
    def __str__(self):
        return self.name
            
class Game():
    game_status = {}
    def __init__(self):
        pass
    def __str__(self):
        return self.players
    def start(self):
        self.players = []
        number_players = eval(input('How many players:'))
        while True:
            if number_players < 2 or not isinstance(number_players, int):
                number_players = eval(input('Wrong format, please input again:'))
            else: break
        for i in range(number_players):
            self.players.append(Player('player' + str(i)))
            type(self).game_status[self.players[i].name] = self.players[i].points
        round = 0 
        while True:
            biggerPointsPlayer = self.players[0]
            if len(self.players) < 2:
                break
            round += 1
            flag = False
            for player in self.players[:]:
                if len(self.players) == 1:
                    biggerPointsPlayer = self.players[0]
                    flag = False
                    break
                if player.play():
                    flag = True
                    type(self).game_status[player.name] = player.points
                    if player.points > 21:
                        print('You lost!')
                        self.players.remove(player)
                        continue
                    elif player.points == 21:
                        biggerPointsPlayer = player
                        flag = False
                        break
                    if player.points > biggerPointsPlayer.points:
                        biggerPointsPlayer = player
                    
            print('* The ' + str(round) + ' round result: ' + str(type(self).game_status))
            print('  ' + str(biggerPointsPlayer) + ' is the bigger one.')
            if flag == False:
                break
        print('---------------------------')
        print('Here is the final result:')
        type(self).game_status[player.name] = player.points
        print(type(self).game_status)
        print(biggerPointsPlayer.name + ' win!')
        return
                 

if __name__ == '__main__':
    game = Game()
    game.start()
    



