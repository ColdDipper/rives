#!/usr/bin/python3

import rives.core.text_styles as ts
from rives.core.utils import show_banner


def command_input(prompt):
    return input(ts.white + ts.underline + 'ref' + ts.white + '(' + ts.bold + ts.red + str(prompt) + ts.white + ')>')


def main():
    show_banner()

    while True:
        command = command_input('console')


if __name__ == '__main__':
    main()
