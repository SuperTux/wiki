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

import os
import sys

# https://github.com/rtfd/CommonMark-py
from CommonMark import Parser, dumpAST


class Validator:

    def __init__(self, filename: str) -> None:
        self._filename = filename

    def validate(self) -> None:
        with open(self._filename) as fin:
            parser = Parser()
            document = parser.parse(fin.read())

            for node, starttag in document.walker():
                self.check(node, starttag)

            # dumpAST(document)

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
            pass  # insert url code here
        else:
            filename = node.destination + ".md"
            if not os.path.exists(filename):
                print("{}: error: {} does not exist".format(self.get_pos(node),
                                                            filename),
                      file=sys.stderr)

    def validate_image_destination(self, node) -> None:
        # print("image: {}".format(link))
        if not os.path.exists(node.destination):
            print("{}: error: {} does not exist".format(self.get_pos(node),
                                                        node.destination),
                  file=sys.stderr)


    def check(self, node, starttag: bool):
        if starttag:
            if node.t == "link":
                # children = list(node.walker())
                # print(children[1][0].literal)
                # print(node.destination)
                # print()
                self.validate_link_destination(node)
            elif node.t == "image":
                # children = list(node.walker())
                # print(children[1][0].literal)
                # print(node.destination)
                # print()
                self.validate_image_destination(node)


def main():
    for filename in sys.argv[1:]:
        validator = Validator(filename)
        validator.validate()


if __name__ == "__main__":
    main()


# EOF #
