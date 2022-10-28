#!/usr/bin/env python3
from argparse import ArgumentParser
import json


def create_parser():
    parser = ArgumentParser(
        description="Add a game to the list"
    )

    parser.add_argument("System", type=str, help="Platform/system the game runs on")
    parser.add_argument("Name", type=str, help="Name of the game")
    parser.add_argument("Genre", type=str, help="Exp. Racing, farming, shooter..")
    parser.add_argument("Notes", type=str, help="Any additional notes here.")
    parser.add_argument("MaxPlayer", type=int, help="Max player that can play the game" )

    return parser


def get_game_from_command_line_arguments():
    parser = create_parser()
    args = parser.parse_args()

    return {
        "Sytem": args.System,
        "Name":  args.Name,
        "Genre": args.Genre,
        "Notes": args.Notes,
        "MaxPlayer": args.MaxPlayer,
    }


if __name__ == '__main__':
    game = get_game_from_command_line_arguments()
    print(game)
