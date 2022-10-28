#!/usr/bin/env python3
from argparse import ArgumentParser
import json


def create_parser():
    parser = ArgumentParser(
        description="Add a game to the list"
    )

    parser.add_argument("platform", type=str, help="Platform/system the game runs on")
    parser.add_argument("name", nargs="+", type=str, help="Name of the game")

    return parser


def get_game_from_command_line_arguments():
    parser = create_parser()
    args = parser.parse_args()

    return {
        "platform": args.platform,
        "name": " ".join(args.name),
    }


if __name__ == '__main__':
    game = get_game_from_command_line_arguments()
    print(game)
