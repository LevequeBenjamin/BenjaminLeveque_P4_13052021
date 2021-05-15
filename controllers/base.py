"""Define the main controller."""

from colorama import Fore

from tinydb import TinyDB
from models import tournaments
from models.tournaments import Tournament
from models.players import Player
from models.rounds import Round
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

db = TinyDB("db/db.json")


class Controller:
    """Main controller."""

    def __init__(self, tournament_view, player_view):
        # views
        self.tournament_view = tournament_view
        self.player_view = player_view


    @property
    def set_tournament(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        try:
            name = self.tournament_view.prompt_tournament_name
            location = self.tournament_view.prompt_tournament_location
            dated = self.tournament_view.prompt_tournament_dated
            time_control = self.tournament_view.prompt_tournament_time_control
            description = self.tournament_view.prompt_tournament_description
            
            tournament = Tournament(name, location, dated, time_control,
                                    description)
            self.save_table_tournament(tournament)
            return tournament
        except Exception as err:
            logger.error("Oops! %s", err)


    @property
    def set_new_player(self):
        """[summary]

        Args:
            number_of_players ([type]): [description]
        """
        try:
            last_name = self.player_view.prompt_player_lastname
            first_name = self.player_view.prompt_player_firstname
            birth_date = self.player_view.prompt_player_birthdate
            sex = self.player_view.prompt_player_sex
            elo = self.player_view.prompt_player_elo

            player = Player(last_name, first_name, birth_date, sex, elo)
            self.save_table_players(player)
        except Exception as err:
            logger.error("Oops! %s", err)
            
    @property
    def set_list_players(self):
        """[summary]

        Args:
            number_of_players ([type]): [description]
        """
        players = []
        for i in range(8):
            try:
                last_name = self.player_view.prompt_player_lastname
                first_name = self.player_view.prompt_player_firstname
                birth_date = self.player_view.prompt_player_birthdate
                sex = self.player_view.prompt_player_sex
                elo = self.player_view.prompt_player_elo

                player = Player(last_name, first_name, birth_date, sex, elo)
                players.append(player.__str__)
            except Exception as err:
                logger.error("Oops! %s", err)
        return players


    def save_table_players(self, player):
        """Docstrings."""
        table = db.table("table_players")
        try:
            table.insert(player.__str__)
        except Exception as err:
            logger.error("Oops! %s :", err)


    def save_table_tournament(self, tournament):
        """Docstrings."""
        table = db.table("table_tournaments")
        try:
            table.insert(tournament.__str__)
        except Exception as err:
            logger.error("Oops! %s :", err)

    @property
    def start_tournament(self):
        """Docstrings."""
        tournament = self.set_tournament
        players = self.set_list_players
        tournament.append_list_players(players)
        round = Round(players)


    @property
    def menu(self):
        """Docstrings."""
        print(Fore.LIGHTWHITE_EX + "[1] Ajouter un nouveau joueur.")
        print("[2] Créer un tournoi.")
        print("[0] Quitter Chess Tournament.")


    def perform(self, user_choice):
        """Docstrings."""
        if user_choice == 1:
            self.set_new_player
        elif user_choice == 2:
            self.start_tournament
        elif user_choice == 0:
            print(Fore.WHITE + "Merci d'avoir utilisé Chess Tournament, à bientôt !!")
            quit()


    @property
    def start_program(self):
        """Docstrings."""
        print(Fore.LIGHTCYAN_EX + "========================================")
        print("            CHESS TOURNAMENT            ")
        print("========================================")
        print()
        self.menu
        print()
        user_choice = 3
        while user_choice not in range(0, 3):
            try:
                user_choice = int(
                    input(Fore.LIGHTBLUE_EX + "Bonjour, que voulez-vous faire ? : "))
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")
            except Exception as err:
                logger.error("Oops! %s", err)
        self.perform(user_choice)


    def run(self):
        """Run the tournament."""
        self.start_program

        #tournament = self.set_tournament()
        # self.set_players(tournament.number_of_players,
        # tournament.append_list_players)
        # for player in tournament.list_players:
        # db_player.insert(player)
        # tournament.append_list_players(self.list_players)
        # db_tournament.insert(tournament.__str__())
