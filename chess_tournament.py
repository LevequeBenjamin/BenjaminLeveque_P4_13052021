#! /usr/bin/env python3
# coding: utf-8

"""
=========================================================
            ***** Chess Tournament *****
                  DA PYTHON / 2021
=========================================================
"""


# controllers
from controllers.base import Controller


def main() -> None:
    """Main instructions to run"""
    controller = Controller()
    controller.run()


if __name__ == "__main__":
    main()
