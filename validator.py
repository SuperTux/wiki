#!/usr/bin/env python3

# A quick&dirty Markdown Validator
# Copyright (C) 2018 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from typing import List

import os
import sys
import argparse
from enum import Flag
import requests

# https://github.com/rtfd/CommonMark-py
from CommonMark import Parser, dumpAST


def url_valid(url: str) -> bool:
    try:
        request = requests.head(url, timeout=1.0)
        if request.ok:
            return True
        else:
            return False
    except Exception:
        return False


class ValidatorFlags(Flag):

    # Validate everything
    ALL = ~0

    # Validate image
    IMAGE = (1 << 1)

    # Validate regular text links
    LINK = (1 << 2)

    # Validate anchor links (e.g. "#FOOBAR")
    ANCHOR = (1 << 3)

    # Validate external references (e.g. "http://...", "https://...")
    EXTERNAL = (1 << 4)

    # Validate local references
    LOCAL = (1 << 5)


class Validator:

    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._anchors = []

    def set_flags(self, flags):
        self._flags = flags

    def validate(self) -> None:
        with open(self._filename) as fin:
            parser = Parser()
            document = parser.parse(fin.read())

            for node, starttag in document.walker():
                self.preprocess(node, starttag)

            for node, starttag in document.walker():
                self.check(node, starttag)

    def get_pos(self, node) -> str:
        cur = node.parent

        while cur is not None:
            if cur.sourcepos is not None:
                return "{}:{}".format(self._filename, cur.sourcepos[0][0])
            else:
                cur = cur.parent

        return "{}".format(self._filename)

    def validate_link_destination(self, node) -> None:
        # print("link: {}".format(link))
        if node.destination.startswith("http://") or node.destination.startswith("https://"):
            if self._flags & ValidatorFlags.EXTERNAL:
                if not url_valid(node.destination):
                    print("{}: error: {} failed to load".format(self.get_pos(node),
                                                                node.destination))
                else:
                    print("{}: OK".format(node.destination))
        elif node.destination.startswith("#"):
            if self._flags & ValidatorFlags.ANCHOR:
                self.validate_anchor(node, node.destination[1:])
        else:
            page, *rest = node.destination.split("#", 1)
            filename = page + ".md"
            if not os.path.exists(filename):
                print("{}: error: {} does not exist".format(self.get_pos(node),
                                                            filename),
                      file=sys.stderr)

            if rest and self._flags & ValidatorFlags.ANCHOR:
                # need to read in the other document to validate this
                # anchor properly
                # self.validate_anchor(node, rest[0])
                pass

    def validate_anchor(self, node, anchor: str) -> None:
        if anchor not in self._anchors:
            print("{}: error: {} anchor does not exist".format(self.get_pos(node),
                                                               anchor),
                  file=sys.stderr)

    def validate_image_destination(self, node) -> None:
        # print("image: {}".format(link))
        if not os.path.exists(node.destination):
            print("{}: error: {} does not exist".format(self.get_pos(node),
                                                        node.destination),
                  file=sys.stderr)

    def get_text(self, node) -> str:
        result = ""
        for child, starttag in node.walker():
            if child.t == "text":
                result += child.literal
        return result

    def preprocess(self, node, starttag: bool):
        if starttag:
            if node.t == "heading":
                title = self.get_text(node)
                anchor = title.lower().replace(" ", "-")
                self._anchors.append(anchor)

    def check(self, node, starttag: bool):
        if starttag:
            if node.t == "link" and self._flags & ValidatorFlags.LINK:
                # children = list(node.walker())
                # print(children[1][0].literal)
                # print(node.destination)
                # print()
                self.validate_link_destination(node)
            elif node.t == "image" and self._flags & ValidatorFlags.IMAGE:
                # children = list(node.walker())
                # print(children[1][0].literal)
                # print(node.destination)
                # print()
                self.validate_image_destination(node)


def parse_args(argv: List[str]) -> argparse.Namespace:
    # Parse Arguments
    parser = argparse.ArgumentParser(description="Flexlay - SuperTux Editor")
    parser.add_argument("FILE", action="store", type=str, nargs="+",
                        help=".md file to verify")
    parser.add_argument("--validate", metavar="CATEGORY", type=str, default="all")
    parser.add_argument("--dump-ast", action='store_true', default=False)
    return parser.parse_args(argv[1:])


def main(argv: List[str]):
    args = parse_args(argv)

    flags = ValidatorFlags(0)
    categories = args.validate.split(",")
    for category in categories:
        category = category.lower()
        if category == "all":
            flags |= ValidatorFlags.ALL
        elif category == "external":
            flags |= ValidatorFlags.EXTERNAL
        elif category == "local":
            flags |= ValidatorFlags.LOCAL
        elif category == "link":
            flags |= ValidatorFlags.LINK
        elif category == "anchor":
            flags |= ValidatorFlags.ANCHOR
        elif category == "image":
            flags |= ValidatorFlags.IMAGE
        else:
            raise Exception("unknown category '{}'".format(category))

    for filename in args.FILE:
        if args.dump_ast:
            with open(filename) as fin:
                parser = Parser()
                document = parser.parse(fin.read())
                dumpAST(document)
        else:
            validator = Validator(filename)
            validator.set_flags(flags)
            validator.validate()


if __name__ == "__main__":
    main(sys.argv)


# EOF #
