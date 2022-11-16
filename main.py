from Game.Game import Game
from Game.GameState import GameState
from Players.Player import Player
from Tracks.Track import Track

if __name__ == '__main__':
    #game = Game()
    #player = Player()
    track = Track()

    game_state = GameState()
    game_state.reset(track)
    print(game_state)


    #game.run(track, player)


