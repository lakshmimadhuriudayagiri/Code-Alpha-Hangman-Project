import random

class Login:
    def __init__(self):
        self.username = ""

    def login(self):
        print("="*40)
        print("LOGIN")
        print("="*40)
        self.username = input("Enter Username: ")
        password = input("Enter Password: ")
        if self.username and password:
            print("Login Successful!\n")
            return True
        print("Invalid Login")
        return False

class ScoreBoard:
    def __init__(self):
        self.score = 0

    def add(self, pts):
        self.score += pts

    def show(self, user):
        print("\n===== SCORE BOARD =====")
        print("Player :", user)
        print("Score  :", self.score)
        print("=======================\n")

class HangmanGame:
    def __init__(self):
        self.words = ["python","object","student","computer","project","college","program"]
        self.lives = 6

    def play(self):
        word = random.choice(self.words)
        guessed = []
        while self.lives > 0:
            display = ""
            complete = True
            for ch in word:
                if ch in guessed:
                    display += ch + " "
                else:
                    display += "_ "
                    complete = False
            print("\nWord:", display)
            print("Lives:", self.lives)
            if complete:
                print("Congratulations! You guessed the word:", word)
                return True
            letter = input("Guess a letter: ").lower()
            if len(letter)!=1 or not letter.isalpha():
                print("Enter one alphabet.")
                continue
            if letter in guessed:
                print("Already guessed.")
                continue
            guessed.append(letter)
            if letter not in word:
                self.lives -= 1
                print("Wrong guess!")
            else:
                print("Correct!")
        print("Game Over! Word was:", word)
        return False

class Menu:
    def __init__(self):
        self.login_obj = Login()
        self.score = ScoreBoard()

    def run(self):
        while True:
            print("="*40)
            print(" HANGMAN GAME ")
            print("="*40)
            print("1. Login")
            print("2. Play Game")
            print("3. Score Board")
            print("4. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.login_obj.login()
            elif choice == "2":
                if self.login_obj.username == "":
                    print("Please login first.")
                else:
                    game = HangmanGame()
                    if game.play():
                        self.score.add(10)
            elif choice == "3":
                if self.login_obj.username:
                    self.score.show(self.login_obj.username)
                else:
                    print("Please login first.")
            elif choice == "4":
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    Menu().run() 