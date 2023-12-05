#!/usr/bin/env python

from icecream import ic
import sys
import math


def main() -> None:
    lines = open("input", mode="r").read().split("\n")

    games = [
        (
            set(
                int(i)
                for i in l.split(":")[1]
                .split("|")[0]
                .replace("  ", " ")
                .split(" ")[1:-1]
            ),
            set(
                int(i)
                for i in l.split(":")[1]
                .split("|")[1]
                .replace("  ", " ")
                .split(" ")[1:]
            ),
        )
        for l in lines
    ]

    points = [math.floor(2 ** (len(nums & piks) - 1)) for nums, piks in games]

    ic(sum(points))


if __name__ == "__main__":
    sys.exit(main())
