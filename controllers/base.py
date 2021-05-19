"""Define the main controller."""

# librairies
from colorama import Fore
from datetime import datetime
from tinydb import TinyDB, Query
import logging

# models
from models.tournaments import Tournament
from models.players import Player
from models.players import Participant
from models.rounds import Round
from models.matches import Match

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# database
db = TinyDB("db/db.json")
User = Query()
table_players = db.table("table_players")
table_tournaments = db.table("table_tournaments")


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
        """Creates a Tournament instance.

        Returns:
            Objet: instance Tournament
        """
        try:
            name = self.tournament_view.prompt_tournament_name
            location = self.tournament_view.prompt_tournament_location
            dated = self.tournament_view.prompt_tournament_dated
            time_control = self.tournament_view.prompt_tournament_time_control
            description = self.tournament_view.prompt_tournament_description

            tournament = Tournament(name, location, dated, time_control,
                                    description)
            return tournament
        except Exception as err:
            logger.error("Oops! %s", err)

    @property
    def set_new_player(self):
        """Create a new Player instance and save it in the database. """
        try:
            last_name = self.player_view.prompt_player_lastname
            first_name = self.player_view.prompt_player_firstname
            if not self.check_table_players(last_name, first_name):
                birth_date = self.player_view.prompt_player_birthdate
                sex = self.player_view.prompt_player_sex
                elo = self.player_view.prompt_player_elo

                player = Player(last_name, first_name, birth_date, sex, elo)
                self.save_table_players(player)
                print(Fore.LIGHTYELLOW_EX +
                      f"\nLe joueur {last_name} {first_name} a bien été ajouté !")
            else:
                print(Fore.LIGHTRED_EX +
                      f"\nLe joueur {last_name} {first_name} est déjà présent dans la base de données.")
            print("************************************************************\n")
        except Exception as err:
            logger.error("Oops! %s", err)

    def set_list_players(self, tournament):
        """Creates 8 Players instance, save in database and 
        add to the list players in Tournament instance.

        Args:
            tournament (Object): Tournament instance
        """
        for j in range(1, 9):
            if j == 1:
                print(f"Créez le {j}er joueur.")
            else:
                print(f"Créez le {j}eme joueur.")
            try:
                last_name = self.player_view.prompt_player_lastname
                first_name = self.player_view.prompt_player_firstname
                if not self.check_table_players(last_name, first_name):
                    birth_date = self.player_view.prompt_player_birthdate
                    sex = self.player_view.prompt_player_sex
                    elo = self.player_view.prompt_player_elo

                    player = Participant(last_name, first_name,
                                         birth_date, sex, elo)
                    tournament.append_list_players(player.serialize)
                    self.save_table_players(player)
                    print(Fore.LIGHTYELLOW_EX +
                          f"\nLe joueur {last_name} {first_name} a bien été ajouté et enregistré dans la base de données!")
                else:
                    player_found = self.search_table_players(
                        last_name, first_name)
                    player = Participant(player_found["last_name"], player_found["first_name"],
                                         player_found["birth_date"], player_found["sex"], player_found["elo"])
                    tournament.append_list_players(player.serialize)
                    print(Fore.LIGHTYELLOW_EX +
                          f"\nLe joueur {last_name} {first_name} a bien été ajouté!")
                    print("Ses informations sont importés depuis la base de données.")
                print("*************************************************************\n")
            except Exception as err:
                logger.error("Oops! %s", err)

    def check_table_players(self, last_name, first_name):
        for player in table_players:
            if player["last_name"] == last_name and player["first_name"] == first_name:
                return True
            else:
                False

    def search_table_players(self, last_name, first_name):
        player_found = ""
        for player in table_players:
            if player["last_name"] == last_name and player["first_name"] == first_name:
                player_found = player
        return player_found

    def save_table_players(self, player):
        """Save player in database.

        Args:
            player (Object): Player instance
        """
        try:
            table_players.insert(player.serialize_player)
        except Exception as err:
            logger.error("Oops! %s :", err)

    def save_table_tournament(self, tournament):
        """Save tournament in database.

        Args:
            tournament (Object): Tournament instance
        """
        try:
            table_tournaments.insert(tournament.serialize)
        except Exception as err:
            logger.error("Oops! %s :", err)

    def start_rounds(self, tournament):
        """Start the rounds.

        Args:
            tournament (Object): Tournament instance
        """
        for i in range(1, 5):
            j = 1
            name = f"Round{i}"
            created_at = datetime.now()
            round = Round(tournament.get_list_players, name, str(created_at))
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
                print(
                    f"{player_one['last_name']} vs {player_two['last_name']}")
                print(f"joueur :", player_one["last_name"])
                score_player_one = self.round_view.prompt_set_score
                player_one["score"] += score_player_one
                print(f"joueur :", player_two["last_name"])
                score_player_two = self.round_view.prompt_set_score
                player_two["score"] += score_player_two
                match = Match(player_one, player_two,
                              score_player_one, score_player_two)
                round.append_list_matches(match.serialize)
                j += 1
                print(Fore.LIGHTWHITE_EX +
                      "\n************************************************************\n")
            print(f"\nTour {i} terminé.")
            print(Fore.LIGHTWHITE_EX +
                  "************************************************************\n")
            tournament.append_list_rounds(round.serialize)
        self.save_table_tournament(tournament)

    @property
    def start_tournament(self):
        """Start the tournament."""
        print(Fore.LIGHTYELLOW_EX +
              "\n********************* Créez un tournoi *********************\n")
        tournament = self.set_tournament
        print(Fore.LIGHTYELLOW_EX +
              "\n********************* Créez 8 joueurs *********************\n")
        self.set_list_players(tournament)
        print(Fore.LIGHTYELLOW_EX +
              "********************* Lancer le tournoi *********************\n")
        self.start_rounds(tournament)

    def perform(self, user_choice):
        """Performs according to the user choice.

        Args:
            user_choice (int): user choice
        """
        if user_choice == 1:
            self.set_new_player
        elif user_choice == 2:
            self.start_tournament
        elif user_choice == 0:
            print(Fore.LIGHTYELLOW_EX +
                  "\n************************************************************")
            print(Fore.WHITE +
                  "    Merci d'avoir utilisé Chess Tournament, à bientôt !!")
            print(Fore.LIGHTYELLOW_EX +
                  "************************************************************\n")
            quit()

    @property
    def start_program(self):
        """Start the program."""
        print(Fore.LIGHTCYAN_EX +
              "\n============================================================")
        print("                      CHESS TOURNAMENT                      ")
        print("============================================================ \n")
        user_choice = ""
        while user_choice != 0:
            self.user_view.menu
            user_choice = self.user_view.prompt_start_program
            self.perform(user_choice)

    def run(self):
        """Run the tournament."""
        self.start_program
