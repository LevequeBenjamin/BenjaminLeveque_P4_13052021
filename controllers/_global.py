"""Define a parent controller for players controller and tournaments controller"""

# views
from views.round import RoundView
from views.user import UserView
from views.tournament import TournamentView
from views.player import PlayerView

# controllers
from controllers.db import DbControllerTournament, DbControllerlPlayer


class GlobalController:
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
        self.user_view = UserView()
        self.player_view = PlayerView()
        self.round_view = RoundView()
