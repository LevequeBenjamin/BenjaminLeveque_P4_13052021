"""Entry point."""

from models import tournaments

from controllers.base import Controller

from views.tournament import TournamentView
from views.player import PlayerView


def main():
    tournament_view = TournamentView()
    player_view = PlayerView()
    controller = Controller(tournament_view, player_view)
    controller.run()


if __name__ == "__main__":
    main()
