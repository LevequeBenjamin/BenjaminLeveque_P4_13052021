"""Define the main controller."""

# librairies
import logging
from colorama import Fore

# models
from models.tournaments import Tournament
from models.players import Participant
from models.rounds import Round
from models.matches import Match

# views
from views.user import UserView

# controller
from controllers.players import PlayerController
from controllers.tournaments import TournamentController


# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Controller:
    """Main controller."""

    def __init__(self):
        """[summary]
        """
        # views
        self.user_view = UserView()
        # controllers
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def print_players(self):
        players = self.player_controller.print_players()
        if players:
            user_choice = self.player_controller.player_view.prompt_menu_players()
            self.players_perform(user_choice)
        else:
            return None

    def print_tournaments(self):
        tournaments = self.tournament_controller.print_tournaments()
        if tournaments:
            user_choice = self.tournament_controller.tournament_view.prompt_menu_tournaments()
            self.tournaments_perform(user_choice)
        else:
            return None

    def get_choice_menu_tournament(self, tournament):
        """[summary]

        Args:
            tournament ([type]): [description]
        """
        user_choice = ""
        while user_choice != 0:
            self.tournament_controller.tournament_view.menu(tournament)
            self.tournament_controller.tournament_view.print_current_tournament(tournament)
            user_choice = (
                self.tournament_controller.tournament_view.prompt_choice_menu_tournament()
            )
            self.tournament_perform(user_choice, tournament)

    def start_import_tournament(self):
        """Start a tournament in progress"""
        self.user_view.header()
        self.user_view.title_h2("Importez un tournoi.")
        self.tournament_controller.print_tournaments()
        tournament = self.tournament_controller.import_tournament()
        if tournament:
            self.get_choice_menu_tournament(tournament)

    def start_tournament(self):
        """Start the tournament."""
        self.user_view.header()
        self.user_view.title_h2("Créez un tournoi.")
        tournament = self.tournament_controller.set_tournament()
        if tournament:
            self.get_choice_menu_tournament(tournament)

    def tournament_perform(self, user_choice, tournament):
        self.user_view.header()
        if tournament.get_current_round() <= 4:
            if not tournament.get_list_players() or len(tournament.serialize_players()) < 8:
                if user_choice == 1:
                    self.user_view.title_h2("Créez 8 joueur.")
                    self.player_controller.set_list_players(tournament)
                elif user_choice == 2:
                    pass
                elif user_choice == 0:
                    self.start_program()
            else:
                if user_choice == 1:
                    self.user_view.title_h2("Tournoi en cours.")
                    self.tournament_controller.start_rounds(tournament)
                elif user_choice == 2:
                    pass
                elif user_choice == 0:
                    self.start_program()
            user_choice = ""
        else:
            if user_choice == 1:
                self.tournament_controller.print_result_tournament(tournament)
            if user_choice == 2:
                pass
            if user_choice == 3:
                self.start_program()

    def tournaments_perform(self, user_choice):
        """Performs according to the user choice.

        Args:
            user_choice (int): user choice
        """
        self.user_view.header()
        if user_choice == 1:
            self.start_import_tournament()
        elif user_choice == 2:
            self.user_view.title_h2("Afficher les résultats d'un tournoi.")
            pass
        elif user_choice == 0:
            self.start_program()

    def players_perform(self, user_choice):
        """Performs according to the user choice.

        Args:
            user_choice (int): user choice
        """
        self.user_view.header()
        if user_choice == 1:
            self.user_view.title_h2("Créez un joueur.")
            self.player_controller.set_new_player()
        elif user_choice == 2:
            self.user_view.title_h2("Modifiez le classement Elo un d'un joueur.")
            self.player_controller.update_players_elo()
        elif user_choice == 0:
            self.start_program()

    def perform(self, user_choice):
        """Performs according to the user choice.

        Args:
            user_choice (int): user choice
        """
        self.user_view.header()
        if user_choice == 1:
            self.user_view.title_h2("Créez un joueur.")
            self.player_controller.set_new_player()
        elif user_choice == 2:
            self.start_tournament()
        elif user_choice == 3:
            self.start_import_tournament()
        elif user_choice == 4:
            self.print_players()
        elif user_choice == 5:
            self.print_tournaments()
        elif user_choice == 0:
            self.user_view.exit_program()

    def start_program(self):
        """Start the program."""
        user_choice = ""
        while user_choice != 0:
            self.user_view.menu()
            user_choice = self.user_view.prompt_start_program()
            self.perform(user_choice)

    def run(self):
        """Run the tournament."""
        self.start_program()
