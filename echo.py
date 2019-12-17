#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Bryan"


import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Perform " +
                                     "transformation on input text.")

    parser.add_argument("text", help="text to be manipulated")

    parser.add_argument("-u", "--upper", help="convert text to uppercase",
                        action="store_true")

    parser.add_argument("-l", "--lower", help="convert text to lowercase",
                        action="store_true")

    parser.add_argument("-t", "--title", help="convert text to titlecase",
                        action="store_true")

    return parser


def main(args):
    parser = create_parser()
    parsed_args = parser.parse_args(args)
    text = parsed_args.text

    if parsed_args.lower and parsed_args.upper and parsed_args.title:
        text = parsed_args.text.upper().lower().title()

    elif parsed_args.upper:
        text = parsed_args.text.upper()

    elif parsed_args.lower:
        text = parsed_args.text.lower()

    elif parsed_args.title:
        text = parsed_args.text.title()

    else:
        text = parsed_args.text

    print(text)

    return text


if __name__ == '__main__':
    main(sys.argv[1:])
