"""Entry point."""

from models import tournaments

from controllers.base import Controller

from views.tournament import TournamentView
from views.player import PlayerView
from views.round import RoundView
from views.user import UserView


def main():
    user_view = UserView()
    tournament_view = TournamentView()
    player_view = PlayerView()
    round_view = RoundView()
    controller = Controller(user_view, tournament_view, player_view, round_view)
    controller.run()


if __name__ == "__main__":
    main()
