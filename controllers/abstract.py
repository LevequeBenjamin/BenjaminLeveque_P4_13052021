"""Define a parent controller for players controller and tournaments controller"""

from abc import ABC

# views
from views.round import RoundView
from views.tournament import TournamentView
from views.player import PlayerView

# controllers
from controllers.db import DbControllerTournament, DbControllerlPlayer


class AbstractController(ABC):  # pylint: disable=too-few-public-methods
    """It is a parent class which is used to create inheritance.

    Attributs:
        db_tournament: DbControllerTournament()
        db_player: DbControllerlPlayer()
        tournament_view: TournamentView()
        player_view: PlayerView()
        round_view: RoundView()
    """

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(self):
        """Inits GlobalController"""
        # database
        self.db_tournament = DbControllerTournament()
        self.db_player = DbControllerlPlayer()
        # views
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.round_view = RoundView()
