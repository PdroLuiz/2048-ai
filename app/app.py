from game import Game
from random import randint
from model import Model
import numpy as np
highest = 0
ciclos = 0
while True:
    counter = 0
    game = Game()
    model = Model()
    ciclos += 1
    print(ciclos)
    while True:
        game_state = game.state.copy()
        mov = model.predict(game.state)
        if mov == 0:
            still_playng = game.move_up()
            if np.array_equal(game_state, game.state):
                counter += 1
        elif mov == 1:
            still_playng = game.move_down()
            if np.array_equal(game_state, game.state):
                counter += 1
        elif mov == 2:
            still_playng = game.move_left()
            if np.array_equal(game_state, game.state):
                counter += 1
        elif mov == 3:
            still_playng = game.move_right()
            if np.array_equal(game_state, game.state):
                counter += 1
        if counter > 1:
            still_playng = False
        if not still_playng:
            if highest < game.points:
                highest = game.points
                print(game.state)
                print(f'pontuação: {highest}\n')
            break
