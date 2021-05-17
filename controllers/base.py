"""Define the main controller."""

from colorama import Fore

from tinydb import TinyDB
from models import tournaments
from models.tournaments import Tournament
from models.players import Player
from models.rounds import Round
from models.matches import Match
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

db = TinyDB("db/db.json")


class Controller:
    """Main controller."""

    def __init__(self, user_view, tournament_view, player_view, round_view):
        # views
        self.user_view = user_view
        self.tournament_view = tournament_view
        self.player_view = player_view
        self.round_view = round_view

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
            print()
            print(Fore.LIGHTYELLOW_EX + f"Le joueur {last_name} a bien été ajouté !")
            print("************************************************************")
            print()
        except Exception as err:
            logger.error("Oops! %s", err)

    def set_list_players(self, tournament):
        """[summary]

        Args:
            number_of_players ([type]): [description]
        """
        for j in range(8):
            try:
                last_name = self.player_view.prompt_player_lastname
                first_name = self.player_view.prompt_player_firstname
                birth_date = self.player_view.prompt_player_birthdate
                sex = self.player_view.prompt_player_sex
                elo = self.player_view.prompt_player_elo

                player = Player(last_name, first_name, birth_date, sex, elo)
                tournament.append_list_players(player.__str__)
            except Exception as err:
                logger.error("Oops! %s", err)

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

    def start_rounds(self, tournament):
        round = Round(tournament.get_list_players)
        print()
        for i in range(1, 5):
            j = 1
            if i == 1:
                print("Lancer le premier tour.")
                players = round.sort_elo_players

            else:
                print(f"{i}ème tour.")
                players = round.sort_score_players

            players_pair = round.generate_pair(players)
            for player in players_pair:
                player_one = player[0]
                player_two = player[1]
                print(f"match :", j)
                print(f"joueur :", player_one["lastname"])
                score_player_one = self.round_view.prompt_set_score
                player_one["score"] += score_player_one
                print(f"joueur :", player_two["lastname"])
                score_player_two = self.round_view.prompt_set_score
                player_two["score"] += score_player_two
                match = Match(player_one, player_two, score_player_one, score_player_two)
                round.append_list_matches(match.tuple_match)
                j += 1
        


    @property
    def start_tournament(self):
        """Docstrings."""
        print()
        print(Fore.LIGHTYELLOW_EX + "********** Créez un tournoi **********")
        tournament = self.set_tournament
        print()
        print(Fore.LIGHTYELLOW_EX + "********** Créez 8 joueurs **********")
        self.set_list_players(tournament)
        print()
        print(Fore.LIGHTYELLOW_EX + "********** Lancer le tournoi **********")
        self.start_rounds(tournament)

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
        user_choice = ""
        while user_choice != 0:
            self.menu
            print()
            user_choice = self.user_view.prompt_start_program
            self.perform(user_choice)

    def run(self):
        """Run the tournament."""
        self.start_program
