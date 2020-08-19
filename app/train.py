from model import Model
from game import Game


class Generation:

    def __init__(self, num_individuals : int):
        self.models = list()
        for i in range(num_individuals):
            self.models.append(Model())

    def CrossOver(self, model1 : Model, model2 : Model):
        pass

    
    def Train(self):
        game = Game()
        pass

geracao = Generation(10)

print(geracao.models)


