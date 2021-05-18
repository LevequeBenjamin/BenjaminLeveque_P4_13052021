#! /usr/bin/env python3
# coding: utf-8

"""
=========================================================
            ***** Chess Tournament *****
                  DA PYTHON / 2021
=========================================================
"""

# models
from models import tournaments

# views
from views.tournament import TournamentView
from views.player import PlayerView
from views.round import RoundView
from views.user import UserView

# controllers
from controllers.base import Controller


def main():
    """ Main instructions to run """
    user_view = UserView()
    tournament_view = TournamentView()
    player_view = PlayerView()
    round_view = RoundView()
    controller = Controller(user_view, tournament_view,
                            player_view, round_view)
    controller.run()


if __name__ == "__main__":
    main()
