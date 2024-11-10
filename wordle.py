
# Libraries
import pyfiglet
from random_word import RandomWords

# Functions
# Helper functions for printing colored text
def red(text: str) -> str:
    return '\x1b[31m' + text + '\x1b[0m'
def yellow(text: str) -> str:
    return '\x1b[33m' + text + '\x1b[0m'
def green(text: str) -> str:
    return '\x1b[32m' + text + '\x1b[0m'

def process_guess(guess: str, solution: str) -> list:
    """
    Evaluates a guessed word against the solution word.

    Args:
        guess (str): The guessed word.
        solution (str): The solution word to compare against.

    Returns:
        list: A list of tuples where each tuple contains a letter from the guessed word
        and a string indicating its status:
            '0' if the letter is not in the solution,
            '1' if the letter is in the solution but in the wrong position,
            '2' if the letter is in the correct position.
    """
    return [(letter, '0' if letter not in solution.lower() else ('2' if index < len(solution) and letter == solution[index].lower() else '1')) for index, letter in enumerate(guess.lower())]

def visualize_guess(processed_guess: list) -> str:
    """
    Prints a visually appealing representation of the processed guess.

    Args:
        processed_guess (list): A list of tuples as returned by process_guess().

    Returns:
        str: A string representing the visualized guess.
    """

    print(' '.join([green(letter) if status == '2' else yellow(letter) if status == '1' else red(letter) for letter, status in processed_guess]))

def get_solution(letter_count_min: int|None = None, letter_count_max: int|None = None, max_tries: int = 100) -> str|None:
    """
    Gets a random word with a length between letter_count_min and letter_count_max (inclusive) by querying the
    Datamuse API with the RandomWords library. If no suitable word is found after max_tries attempts, the function
    returns the last word that was queried.

    Args:
        letter_count_min (int): The minimum number of letters the returned word should have. Defaults to 5.
        letter_count_max (int): The maximum number of letters the returned word should have. Defaults to 5.
        max_tries (int): The maximum number of times to query the API before returning the last queried word. Defaults to 100.

    Returns:
        str: A random word with a length between letter_count_min and letter_count_max (inclusive)
    """
    word = RandomWords().get_random_word()
    while (letter_count_min is not None and len(word) < letter_count_min) or (letter_count_max is not None and len(word) > letter_count_max):
        max_tries -= 1
        word = RandomWords().get_random_word()
        if max_tries == 0:
            return None
    return word

def start_game() -> str:
    """
    Starts a new game of Wordle.

    Prompts the user to input the minimum and maximum number of letters the solution word should have.
    Queries the Datamuse API with the RandomWords library to find a suitable word with the given length constraints.
    If no suitable word is found after max_tries attempts, the function returns the last word that was queried.
    Prints a welcome message and displays the solution word once it is found.

    Returns:
        str: The solution word for the game.
    """
    print(f"{green("Welcome")} {yellow("to")} {red("Wordle")}!")

    while True:
        min_letter_count = input("Enter the minimum number of letters for the solution word, or press Enter to use no constraint: ")
        max_letter_count = input("Enter the maximum number of letters for the solution word, or press Enter to use no constraint: ")

        print("Searching for a suitable word...")
        solution = get_solution(int(min_letter_count) if min_letter_count != '' else None, int(max_letter_count) if max_letter_count != '' else None)

        if solution is not None:
            print("Suitable word found!")
            break
        print("No suitable word found. Please try again.")

    return solution

def game_loop(solution: str) -> int:
    """
    The main game loop for the Wordle game.

    Args:
        solution (str): The solution word for the game.
    """
    tries = 1

    while True:
        guess = input(f"Enter your {tries}. guess ({len(solution)} letters): ")

        if not validate_guess(guess, solution):
            print(f"Invalid guess. Please enter a {len(solution)}-letter word.")
            continue

        processed_guess = process_guess(guess, solution)
        visualize_guess(processed_guess)

        if all(status == '2' for _, status in processed_guess):
            print(f"Congratulations! You won in {tries} tries!")
            return tries

        tries += 1

def validate_guess(guess: str, solution: str) -> bool:
    """
    Validates the given guess against the solution word.

    Args:
        guess (str): The guessed word.
        solution (str): The solution word to compare against.

    Returns:
        bool: True if the guess is valid (same length as the solution), False otherwise.
    """
    return len(guess) == len(solution)

def application_loop() -> None:
    """
    The main application loop for the Wordle game.

    This function starts the game loop by calling start_game() and then enters
    a loop where it repeatedly calls game_loop() to play a game, prints the
    highscore at the end of each game, and asks the player if they want to play
    again. The loop continues until the player chooses to quit.

    The highscore is updated after each game if the player's score is higher than
    the current highscore.

    """
    highscore = float('inf')

    while True:
        solution = start_game()
        score = game_loop(solution)
        print(f"Your highscore is: {green(str(score)) if score < highscore else yellow(str(score)) if score == highscore else red(str(highscore))}")
        if score < highscore:
            highscore = score

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again.lower() != 'yes':
            break

def application_start() -> None:
    """
    Initializes and starts the Wordle application.

    This function prints the game title using a stylized font and then
    enters the main application loop to run the game.
    """
    print(pyfiglet.figlet_format("Wordle"))
    
    application_loop()

# Main
if __name__ == "__main__":
    application_start()
