
# views
from views.round import RoundView
from views.user import UserView
from views.tournament import TournamentView
from views.player import PlayerView

# controllers
from controllers.db import DbControllerTournament, DbControllerlPlayer

class GlobalController:

    def __init__(self):
        self.db_tournament = DbControllerTournament()
        self.db_player = DbControllerlPlayer()
        self.tournament_view = TournamentView()
        self.user_view = UserView()
        self.player_view = PlayerView()
        self.round_view = RoundView()
