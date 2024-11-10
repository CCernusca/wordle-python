
# Libraries
import pyfiglet

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

def get_solution() -> str:
    """
    Retrieves the solution word for the game.

    Returns:
        str: The solution word for the game.
    """
    return 'World'

def start_game() -> str:
    """
    Starts the Wordle game and welcomes the player.

    Returns:
        str: The solution word for the game.
    """
    solution = get_solution()

    print(f"{green("Welcome")} {yellow("to")} {red("Wordle")}! Try to guess the random {len(solution)}-letter word!")

    return solution

def game_loop(solution: str) -> int:
    """
    The main game loop for the Wordle game.

    Args:
        solution (str): The solution word for the game.
    """
    tries = 1

    while True:
        guess = input(f"Enter your {tries}. guess: ")

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
