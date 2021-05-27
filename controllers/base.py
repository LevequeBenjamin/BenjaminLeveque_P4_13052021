"""Define the main controller."""

# librairies
import logging

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

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(self):
        """Inits Controller."""
        # views
        self.user_view = UserView()
        # controllers
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def display_players(self) -> None:
        """Method which displays a complete list of players in database."""
        players = self.player_controller.print_players()
        if players:
            user_choice = self.player_controller.player_view.prompt_menu_players()
            self.display_players_perform(user_choice)

    def display_tournaments(self) -> None:
        """Method which displays a complete list of tournaments in database."""
        tournaments = self.tournament_controller.print_tournaments()
        if tournaments:
            user_choice = (
                self.tournament_controller.tournament_view.prompt_menu_tournaments()
            )
            self.display_tournaments_perform(user_choice)

    def get_choice_menu_tournament(self, tournament: object) -> None:
        """Method which displays the tournament submenu as well as the current
        tournament and allows you to select an option among the submenu.

        Args:
            tournament (Tournament): a Tournament instance
        """
        user_choice = ""
        while user_choice != 0:
            self.tournament_controller.tournament_view.menu(tournament)
            self.tournament_controller.tournament_view.print_current_tournament(
                tournament
            )
            user_choice = (
                self.tournament_controller.tournament_view.prompt_choice_menu_tournament()
            )
            self.start_tournament_perform(user_choice, tournament)

    def start_import_tournament(self) -> None:
        """Method used to start a tournament imported from the database."""
        self.user_view.header()
        self.user_view.title_h2("Importez un tournoi.")
        self.tournament_controller.print_tournaments()
        tournament = self.tournament_controller.import_tournament()
        if tournament:
            self.get_choice_menu_tournament(tournament)

    def start_tournament(self) -> None:
        """Method used to create and start a new tournament."""
        self.user_view.header()
        self.user_view.title_h2("Créez un tournoi.")
        tournament = self.tournament_controller.set_tournament()
        if tournament:
            self.get_choice_menu_tournament(tournament)

    def start_tournament_perform(self, user_choice: int, tournament: object) -> None:
        """Dispatch the action requested by the user

        Args:
            user_choice (int): contains the user choice entered by the user.
            tournament (Tournament): a Tournament instance
        """
        self.user_view.header()
        if tournament.current_round <= 4:
            if not tournament.players or len(tournament.serialize_players()) < 8:
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

    def display_tournaments_perform(self, user_choice: int) -> None:
        """Dispatch the action requested by the user

        Args:
            user_choice (int): contains the user choice entered by the user.
        """
        self.user_view.header()
        if user_choice == 1:
            self.start_import_tournament()
        elif user_choice == 0:
            self.start_program()

    def display_players_perform(self, user_choice: int) -> None:
        """Dispatch the action requested by the user

        Args:
            user_choice (int): contains the user choice entered by the user.
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

    def main_perform(self, user_choice: int) -> None:
        """Dispatch the action requested by the user

        Args:
            user_choice (int): contains the user choice entered by the user.
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
            self.display_players()
        elif user_choice == 5:
            self.display_tournaments()
        elif user_choice == 0:
            self.user_view.exit_program()

    def start_program(self) -> None:
        """Start the program."""
        user_choice = ""
        while user_choice != 0:
            self.user_view.menu()
            user_choice = self.user_view.prompt_start_program()
            self.main_perform(user_choice)

    def run(self) -> None:
        """Run the tournament."""
        self.start_program()
