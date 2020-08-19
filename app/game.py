import numpy as np
from random import randint


def mv(array):
    has_change = True
    while has_change:
        has_change = False
        for i in range(len(array) - 1):
            if array[i] == 0 != array[i + 1]:
                temp = array[i]
                aux = array[i + 1]
                array[i + 1] = temp
                array[i] = aux
                has_change = True

class Game:

    def __init__(self, state=None, points=0, mov=0):
        if state is None:
            self.state = np.zeros((4, 4), int)
        else:
            self.state = state
        self.points = points
        self.mov = mov
        if not self.has_movement():
            self.is_finished = True
        else:
            self.is_finished = False
        if state is None:
            for i in range(2):
                self.after_move(True)

    def start_pygame(self, pygame_):
        global pygame
        pygame = pygame_

    def has_space(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == 0:
                    return True
        return False

    def has_movement(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i]) - 1):
                if self.state[i][j] == self.state[i][j + 1] != 0:
                    return True
        self.state = self.state.transpose()
        for i in range(len(self.state)):
            for j in range(len(self.state[i]) - 1):
                if self.state[i][j] == self.state[i][j + 1] != 0:
                    self.state = self.state.transpose()
                    return True
        self.state = self.state.transpose()
        return False

    def after_move(self, initialization=False):
        if not self.has_space():
            if not self.has_movement():
                return False
            return True
        if randint(0, 9) <= 8:
            number = 2
        else:
            number = 4
        while True:
            line = randint(0, len(self.state) - 1)
            column = randint(0, len(self.state) - 1)
            if self.state[line][column] == 0:
                self.state[line][column] = number
                break
        if not initialization:
            self.mov += 1
        return True

    def move_up(self):
        self.state = self.state.transpose()
        for i in range(len(self.state)):
            self.move(i, 0)
        self.state = self.state.transpose()
        return self.after_move()

    def move_down(self):
        self.state = self.state.transpose()
        for i in range(len(self.state)):
            self.move(i, 1)
        self.state = self.state.transpose()
        return self.after_move()

    def move_left(self):
        for i in range(len(self.state)):
            self.move(i, 0)
        return self.after_move()

    def move_right(self):
        for i in range(len(self.state)):
            self.move(i, 1)
        return self.after_move()

    def add(self, array):
        for i in range(len(array) - 1):
            if array[i] == array[i + 1] != 0:
                array[i] += array[i + 1]
                array[i + 1] = 0
                self.points += array[i]
        mv(array)

    def move(self, index: int, direction):
        array = self.state[index]
        if direction:
            array = array[::-1]
        mv(array)
        self.add(array)
        if direction:
            array = array[::-1]
        self.state[index] = array

    def show(self, screen, font=None):
        if font is not None:
            self.font = font
        screen.fill((187, 173, 160))
        for line in range(len(self.state)):
            for column in range(len(self.state[line])):
                pygame.draw.rect(screen, square_color(self.state[line][column]), square(line, column))
                if self.state[line][column] != 0:
                    text = self.font.render(str(self.state[line][column]), True, (255, 255, 255))
                    screen.blit(text, square(line, column, True))



def square_color(val):
    if val == 0:
        color = (205, 193, 180)
    elif val == 2:
        color = (238, 228, 218)
    elif val == 4:
        color = (237, 224, 200)
    elif val == 8:
        color = (242, 177, 121)
    elif val == 16:
        color = (245, 149, 99)
    elif val == 32:
        color = (246, 124, 95)
    elif val == 64:
        color = (246, 94, 59)
    elif val == 128:
        color = (237, 207, 114)
    else:
        color = (0, 0, 0)
    return color


def square(line, column, text=False):
    x_top = 4 + (column * 124)
    y_left = 4 + (line * 124)
    if text:
        x_top += 35
        y_left += 35
    return pygame.Rect(x_top, y_left, 120, 120)

