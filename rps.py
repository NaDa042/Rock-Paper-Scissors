import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        m = input("Rock, Paper, or Scissors? ").lower()
        if m not in moves:
            print("Invalid move! Please type rock, paper, or scissors.")
            return self.move()
        return m


class ReflectPlayer(Player):
    def __init__(self):
        self.their_last_move = 'rock'

    def move(self):
        return self.their_last_move

    def learn(self, my_move, their_move):
        self.their_last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.last_index = 2  # so it starts at rock

    def move(self):
        next_index = (self.last_index + 1) % 3
        return moves[next_index]

    def learn(self, my_move, their_move):
        self.last_index = moves.index(my_move)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def choose_mode():
    try:
        lev = int(input(
            "Select a level:\n"
            "  1 - Super Easy\n"
            "  2 - Easy\n"
            "  3 - Medium\n"
            "  4 - Hard\n"
            "Your choice: "
        ))
    except ValueError:
        print("Please enter a number between 1 and 4.")
        return choose_mode()

    if lev == 1:
        return Player()
    elif lev == 2:
        return CyclePlayer()
    elif lev == 3:
        return ReflectPlayer()
    elif lev == 4:
        return RandomPlayer()
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
        return choose_mode()


def get_round_count():
    try:
        r = int(input("How many rounds do you want to play? "))
        if r <= 0:
            print("Please enter a number greater than 0.")
            return get_round_count()
        return r
    except ValueError:
        print("Please enter a valid number.")
        return get_round_count()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You: {move1}  |  Computer: {move2}")

        if beats(move1, move2):
            self.score1 += 1
            print("You win this round!")
        elif beats(move2, move1):
            self.score2 += 1
            print("Computer wins this round!")
        else:
            print("It's a tie this round!")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        r = get_round_count()

        for round_num in range(1, r + 1):
            print(f"\n--- Round {round_num} ---")
            self.play_round()
            print(f"Score: You {self.score1} : {self.score2} Computer")

        print(
            f"=== Final Score: You {self.score1} : {self.score2} Computer ==="
        )
        if self.score1 > self.score2:
            print("You won the game! Congratulations!")
        elif self.score2 > self.score1:
            print("Computer won the game. Better luck next time!")
        else:
            print("It's a tie!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), choose_mode())
    game.play_game()