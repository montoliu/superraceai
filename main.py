import random

from Game.Game import Game
from Game.GameState import GameState
from Players.Player import Player
from Tracks.Track import Track

if __name__ == '__main__':
    #random.seed(10)

    game = Game()
    player = Player()
    track = Track()
    n_iter = 100
    wins = 0

    for i in range(n_iter):
        wins += game.run(track, player)

    print("Win rate: " + str(wins / n_iter))

