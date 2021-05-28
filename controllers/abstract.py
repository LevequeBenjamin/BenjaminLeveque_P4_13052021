"""Define a parent controller for players controller and tournaments controller"""

from abc import ABC

# views
from views.round import RoundView
from views.tournament import TournamentView
from views.player import PlayerView
from views.match import MatchView

# controllers
from controllers.db import DbControllerTournament, DbControllerlPlayer


class AbstractController(ABC):
    """It is a parent class which is used to create inheritance."""

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
        self.match_view = MatchView()
