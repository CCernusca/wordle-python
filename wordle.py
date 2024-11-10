
# Libraries


# Functions
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
    return [(letter, '0' if letter not in solution else ('2' if letter == solution[index] else '1')) for index, letter in enumerate(guess)]

def visualize_guess(processed_guess: list) -> str:
    """
    Prints a visually appealing representation of the processed guess.

    Args:
        processed_guess (list): A list of tuples as returned by process_guess().

    Returns:
        str: A string representing the visualized guess.
    """
    # Helper functions for printing colored text
    def red(text: str) -> str:
        return '\x1b[31m' + text + '\x1b[0m'
    def yellow(text: str) -> str:
        return '\x1b[33m' + text + '\x1b[0m'
    def green(text: str) -> str:
        return '\x1b[32m' + text + '\x1b[0m'

    print(' '.join([green(letter) if status == '2' else yellow(letter) if status == '1' else red(letter) for letter, status in processed_guess]))

# Main
if __name__ == "__main__":
    visualize_guess(process_guess('hello', 'world'))
