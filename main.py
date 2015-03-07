import setup
import pygame
from puzzle_game import PuzzleGame

def main():
    pygame.init()

    puzzleGame = PuzzleGame()
    puzzleGame.start()

if __name__ == "__main__":
    main()
