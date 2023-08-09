import argparse
from pet_game import main as game_main

def cli_main():
    parser = argparse.ArgumentParser(description="Pocket Companions CLI")
    parser.add_argument("name", help="Enter your pet's name")
    args = parser.parse_args()

    game_main(args.name)

if __name__ == "__main__":
    cli_main()

