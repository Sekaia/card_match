from cards import Card
import random

class Game:
    def __init__(self):
        self.size = 6
        if self.size == 4:
            self.columns = ['A', 'B', 'C', 'D']
            self.card_options = ["Boo", "Bat", "Man", "Dog",
                                 "Cat", "Ham", "Lab", "Pot"]
        elif self.size == 6:
            self.columns = ['A', 'B', 'C', 'D', 'E', 'F']
            self.card_options = ["Boo", "Bat", "Man", "Dog",
                                 "Cat", "Ham", "Lab", "Pot", "Run"]
        elif self.size == 8:
            self.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            self.card_options = ["Boo", "Bat", "Man", "Dog", "Zap",
                                 "Cat", "Ham", "Lab", "Pot", "Run"]
        self.cards = []
        self.locations = []
        for column in self.columns:
            for num in range(1, self.size + 1):
                self.locations.append(f"{column}{num}")


    def set_cards(self):
        used_locations = []
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations) - set(used_locations)
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                card = Card(word, random_location)
                self.cards.append(card)

    def create_row(self, num):
        row = []
        for column in self.columns:
            for card in self.cards:
                if card.location == f"{column}{num}":
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append("   ")
        return row

    def create_grid(self):
        header = ' |  ' + '  |  '.join(self.columns) + '  |'
        print(header)
        for row in range(1, self.size + 1):
            print_row = f"{row}| "
            get_row = self.create_row(row)
            print_row += ' | '.join(get_row) + ' |'
            print(print_row)

    def add_guess(self):
        global guesses
        guesses += 1

    def check_match(self, loc1, loc2):
        cards = []
        for card in self.cards:
            if card.location == loc1 or card.location == loc2:
                cards.append(card)
        if cards[0] == cards[1]:
            cards[0].matched = True
            cards[1].matched = True
            return True
        else:
            for card in cards:
                print(f"{card.location}: {card}")
            return False

    def check_win(self):
        for card in self.cards:
            if card.matched == False:
                return False
            return True

    def check_location(self, time):
        while True:
            guess = input(f"What's the location of your {time} card? ")
            if guess.upper() in self.locations:
                return guess.upper()
            else:
                print("That's not a valid location. It should look like this: A1")

    def start_game(self):
        global guesses
        guesses = 0
        game_running = True
        print("Memory Game")
        self.set_cards()
        while game_running:
            self.create_grid()
            guess1 = self.check_location('first')
            guess2 = self.check_location('second')
            self.add_guess()
            if self.check_match(guess1, guess2):
                if self.check_win():
                    print("You win!")
                    self.create_grid()
                    game_running = False
                else:
                    input("Those cards are a match! Press enter to continue")
            print(f"Guesses: {guesses}")
        print(f"Game over, it took you {guesses} guesses.")


if __name__ == "__main__":
    new_game = Game()
    new_game.start_game()