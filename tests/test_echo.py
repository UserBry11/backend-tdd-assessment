#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Bryan"

import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        args = ["-u", "hello"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertEquals(namespace.upper, True)
        self.assertEquals("HELLO", echo.main(args))

    def test_lower(self):
        args = ["-l", "HELLO"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertEquals(namespace.lower, True)
        self.assertEquals("hello", echo.main(args))

    def test_title(self):
        args = ["-t", "help"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertEquals(namespace.title, True)
        self.assertEquals("Help", echo.main(args))

    def test_allargs(self):
        args = ["-u", "-l", "-t", "heLLo"]
        # parser = echo.create_parser()
        # namespace = parser.parse_args(args)
        self.assertEquals("Hello", echo.main(args))

    def test_nothing(self):
        args = ["tree"]
        # parser = echo.create_parser()
        # namespace = parser.parse_args(args)
        self.assertEquals("tree", echo.main(args))


if __name__ == '__main__':
    unittest.main()
