"""Define the main controller."""

# librairies
import logging

# models
from models.tournaments import Tournament

# controller
from controllers.players import PlayerCtrl
from controllers.tournaments import TournamentCtrl

# views
from views.user import UserView

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Controller:
    """Main controller."""

    def __init__(self):
        # views
        self.user_view = UserView()
        self.player_ctrl = PlayerCtrl()
        self.tournament_ctrl = TournamentCtrl()
        
    def get_choice_menu_tournament(self, tournament):
        user_choice = ""
        while user_choice != 0:
            self.tournament_ctrl.tournament_view.menu(tournament)
            user_choice = (
                self.tournament_ctrl.tournament_view.prompt_choice_menu_tournament
            )
            self.tournament_perform(user_choice, tournament)

    @property
    def start_import_tournament(self):
        """Start a tournament in progress"""
        name = self.tournament_ctrl.tournament_view.prompt_tournament_name
        tournament_found = self.tournament_ctrl.db.search_table_tournaments(name)
        if tournament_found:
            self.user_view.separator_white
            self.user_view.user_print_msg(f"tournoi : {tournament_found['name']}")
            self.user_view.user_print_msg(f"adresse : {tournament_found['location']}")
            self.user_view.user_print_msg(f"date : {tournament_found['dated']}")
            self.user_view.user_print_msg(
                f"time control : {tournament_found['time_control']}"
            )
            self.user_view.user_print_msg(
                f"description : {tournament_found['description']}"
            )
            confirm = self.user_view.prompt_confirm
            if confirm == "Y":
                tournament = Tournament(
                    tournament_found["name"],
                    tournament_found["location"],
                    tournament_found["dated"],
                    tournament_found["time_control"],
                    tournament_found["description"],
                )
                if tournament_found["players"]:
                    for player in tournament_found["players"]:
                        tournament.append_list_players(player)
                if tournament_found["rounds"]:
                    for round in tournament_found["rounds"]:
                        tournament.append_list_rounds(round)
                self.get_choice_menu_tournament(tournament)
        else:
            self.user_view.user_print_err("Aucun tournoi en cours n'a été trouvé.")

    @property
    def start_tournament(self):
        """Start the tournament."""
        self.user_view.separator_title("Créez un tournoi")
        tournament = self.tournament_ctrl.set_tournament
        if tournament:
            self.get_choice_menu_tournament(tournament)

    def tournament_perform(self, user_choice, tournament):
        if tournament.get_current_round < 5:
            if not tournament.get_list_players:
                if user_choice == 1:
                    self.user_view.separator_title("Créez 8 joueurs")
                    self.player_ctrl.set_list_players(tournament)
                elif user_choice == 2:
                    pass
                elif user_choice == 0:
                    self.start_program
            else:
                if user_choice == 1:
                    self.user_view.separator_title("Tournoi en cours")
                    self.tournament_ctrl.start_rounds(tournament)
                elif user_choice == 2:
                    pass
                elif user_choice == 0:
                    self.start_program
            user_choice = ""
        else:
            if user_choice == 1:
                pass
            if user_choice == 2:
                pass
            if user_choice == 3:
                self.start_program
            

    def perform(self, user_choice):
        """Performs according to the user choice.

        Args:
            user_choice (int): user choice
        """
        if user_choice == 1:
            self.player_ctrl.set_new_player
        elif user_choice == 2:
            self.start_tournament
        elif user_choice == 3:
            self.start_import_tournament
        elif user_choice == 0:
            self.user_view.exit_program

    @property
    def start_program(self):
        """Start the program."""
        self.user_view.header
        user_choice = ""
        while user_choice != 0:
            self.user_view.menu
            user_choice = self.user_view.prompt_start_program
            self.perform(user_choice)

    def run(self):
        """Run the tournament."""
        self.start_program
