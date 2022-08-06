import cards
# game class
# grid size
# card options
# columns
# locations
# methods
    # create cards
    # create grid
    # check for matches
    # check if game is won
    # run the game
# dunder main
    # create game instance
    # call start game

class Game:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def create_cards(self):
        pass

    def create_grid(self):
        pass

    def check_matches(self):
        pass

    def check_for_win(self):
        pass

    def run_game(self):
        pass


if __name__ == "__main__":
    new_game = Game(4, 4)
    new_game.run_game()