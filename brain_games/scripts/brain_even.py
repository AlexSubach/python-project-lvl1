#!/usr/bin/env python
from brain_games.engine import run_game
from brain_games.games import is_even


def main():
    run_game(is_even)
    

if __name__ == '__main__':
    main()
    
