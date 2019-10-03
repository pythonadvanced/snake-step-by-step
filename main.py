#!/usr/bin/env python
import re
from argparse import ArgumentParser, ArgumentTypeError
from typing import Tuple

from snake import Game

Size = Tuple[int, int]
SIZE_REGEXP = re.compile(r'\A(\d+)x(\d+)\Z')


def parse_cli_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-b", "--board-size", default=(20, 20), type=_parse_size,
        help="Size of the board, in cells, defaults to 20x20")
    parser.add_argument(
        "-c", "--cell-size", default=(30, 30), type=_parse_size,
        help="Size of the board, in pixels, defaults to 30x30")
    args = parser.parse_args()
    return args.board_size, args.cell_size


def _parse_size(s: str) -> Size:
    match = SIZE_REGEXP.match(s)
    if not match:
        raise ArgumentTypeError("Invalid size")
    return (
        int(match.group(1)),
        int(match.group(2)),
    )


if __name__ == "__main__":
    board_size, cell_size = parse_cli_args()
    game = Game(board_size, cell_size)
    game.run()
