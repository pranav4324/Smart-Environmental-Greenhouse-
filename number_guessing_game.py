"""
Number Guessing Game with two modes:
1. Player guesses a random number chosen by the computer.
2. Computer uses binary search to guess the player's number.

Run with:
    python number_guessing_game.py
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class GameRange:
    """Represents the inclusive range used by both game modes."""

    low: int = 1
    high: int = 100

    def __post_init__(self) -> None:
        if self.low >= self.high:
            raise ValueError("low must be smaller than high")

    @property
    def size(self) -> int:
        return self.high - self.low + 1

    @property
    def binary_search_limit(self) -> int:
        return math.ceil(math.log2(self.size))


class BinarySearchGuesser:
    """Computer player that narrows the search space using binary search."""

    def __init__(self, game_range: GameRange) -> None:
        self.low = game_range.low
        self.high = game_range.high
        self.attempts = 0

    def next_guess(self) -> int:
        if self.low > self.high:
            raise ValueError("No valid numbers remain. Check the feedback given.")

        self.attempts += 1
        return (self.low + self.high) // 2

    def apply_feedback(self, guess: int, feedback: str) -> bool:
        """Returns True when the guess is correct, otherwise updates bounds."""

        normalized = feedback.strip().lower()

        if normalized in {"c", "correct", "yes", "y"}:
            return True
        if normalized in {"h", "high"}:
            self.high = guess - 1
            return False
        if normalized in {"l", "low"}:
            self.low = guess + 1
            return False

        raise ValueError("Feedback must be 'h' for high, 'l' for low, or 'c' for correct.")


def read_integer(prompt: str, minimum: int | None = None, maximum: int | None = None) -> int:
    """Read and validate integer input from the user."""

    while True:
        user_input = input(prompt).strip()

        try:
            value = int(user_input)
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Please enter a number greater than or equal to {minimum}.")
            continue

        if maximum is not None and value > maximum:
            print(f"Please enter a number less than or equal to {maximum}.")
            continue

        return value


def play_player_guess_mode(game_range: GameRange) -> None:
    """Mode 1: the player guesses a random number."""

    secret_number = random.randint(game_range.low, game_range.high)
    attempts = 0

    print("\nPlayer Guess Mode")
    print(f"I picked a number between {game_range.low} and {game_range.high}.")

    while True:
        guess = read_integer("Your guess: ", game_range.low, game_range.high)
        attempts += 1

        if guess == secret_number:
            print(f"Correct! You found it in {attempts} attempt(s).")
            return
        if guess < secret_number:
            print("Too low. Try a bigger number.")
        else:
            print("Too high. Try a smaller number.")


def play_ai_guess_mode(game_range: GameRange) -> None:
    """Mode 2: the computer guesses using binary search."""

    guesser = BinarySearchGuesser(game_range)

    print("\nAI Guess Mode")
    print(f"Think of a number between {game_range.low} and {game_range.high}.")
    print("After each guess, reply with:")
    print("  h = my guess is too high")
    print("  l = my guess is too low")
    print("  c = correct")
    print(f"I should need at most {game_range.binary_search_limit} guesses.")

    while True:
        try:
            guess = guesser.next_guess()
        except ValueError as error:
            print(f"\n{error}")
            print("The feedback was inconsistent, so the AI cannot continue.")
            return

        feedback = input(f"Is your number {guess}? [h/l/c]: ")

        try:
            is_correct = guesser.apply_feedback(guess, feedback)
        except ValueError as error:
            print(error)
            guesser.attempts -= 1
            continue

        if is_correct:
            print(f"I guessed your number in {guesser.attempts} attempt(s)!")
            return


def choose_range() -> GameRange:
    """Allow the user to select a custom range or use the default."""

    print("\nChoose number range")
    print("1. Default range: 1 to 100")
    print("2. Custom range")

    choice = input("Select an option [1-2]: ").strip()
    if choice != "2":
        return GameRange()

    low = read_integer("Lowest number: ")
    high = read_integer("Highest number: ", low + 1)
    return GameRange(low, high)


def print_menu() -> None:
    print("\nNumber Guessing Game - AI Logic")
    print("1. Player guesses the computer's number")
    print("2. Computer guesses your number using binary search")
    print("3. Exit")


def main() -> None:
    print("Welcome to the Number Guessing Game!")

    while True:
        print_menu()
        choice = input("Select a mode [1-3]: ").strip()

        if choice == "1":
            play_player_guess_mode(choose_range())
        elif choice == "2":
            play_ai_guess_mode(choose_range())
        elif choice == "3":
            print("Thanks for playing. Good luck with your interview!")
            return
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
