"""Simple test program."""

import argparse


def simple_addition(x: int) -> int:
    """Calculate x + 1."""
    return x + 1


def simple_multiplication(x: int) -> int:
    """Calculate x * 2."""
    return 2 * x


def parse_commandline() -> argparse.Namespace:
    """Parse the command line."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'N',
        help='Test this with N.',
        type=int,
        default=1,
    )
    return parser.parse_args()


def main() -> None:
    """The main entry point."""

    options = parse_commandline()
    print(f'1 + 1 = {simple_addition(options.N)}')
    print(f'2 * 2 = {simple_multiplication(options.N)}')
