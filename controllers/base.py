"""Define the main controller."""

# librairies
import logging

# models
from models.tournaments import Tournament
from models.players import Participant
from models.rounds import Round
from models.matches import Match

# views
from views.user import UserView

# controller
from controllers.players import PlayerCtrl
from controllers.tournaments import TournamentCtrl


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
        self.player_ctrl = PlayerCtrl()
        self.tournament_ctrl = TournamentCtrl()

    def get_choice_menu_tournament(self, tournament):
        """[summary]

        Args:
            tournament ([type]): [description]
        """
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
                    for player_import in tournament_found["players"]:
                        player = Participant(player_import["last_name"], player_import["first_name"],
                                             player_import["birth_date"], player_import["sex"], player_import["elo"])
                        player_id = self.player_ctrl.db_player.check_table_players(
                            player_import["last_name"], player_import["first_name"])
                        player.add_id(player_id)
                        player.add_score(player_import["score"])
                        player.add_ladder(player_import["ladder"])
                        tournament.append_list_players(player)
                if tournament_found["rounds"]:
                    for round_import in tournament_found["rounds"]:
                        print(round_import)
                        round = Round(round_import["liste match"], round_import["début tour"], round_import["round"])
                        tournament.append_list_rounds(round)
                        for match_import in round_import["liste match"]:
                            match = Match(match_import["match"][0][0], match_import["match"][1][0],
                                          match_import["match"][0][1], match_import["match"][1][1])
                            round.append_list_matches(match)
                        tournament.counter_round
                tournament.add_id(tournament_found.doc_id)
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
