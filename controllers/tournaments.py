"""Define the tournament controller."""

# librairies
from datetime import datetime
import logging
from colorama import Fore

# models
from models.tournaments import Tournament
from models.players import Participant
from models.rounds import Round
from models.matches import Match

# views
from views.round import RoundView
from views.user import UserView
from views.tournament import TournamentView

# controllers
from controllers.db import DbControllerTournament, DbControllerlPlayer

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TournamentController:
    """Main controller."""

    def __init__(self):
        """[summary]
        """
        self.db_tournament = DbControllerTournament()
        self.db_player = DbControllerlPlayer()
        self.tournament_view = TournamentView()
        self.user_view = UserView()
        self.round_view = RoundView()
        
    def print_tournaments(self):
        self.user_view.header()
        self.tournament_view.menu_tournois()
        tournois = self.db_tournament.get_tournois()
        self.tournament_view.print_tournois(tournois)

    def set_tournament(self):
        """Creates a Tournament instance.

        Returns:
            Objet: instance Tournament
        """
        try:
            name = self.tournament_view.prompt_tournament_name()
            location = self.tournament_view.prompt_tournament_location()
            dated = self.tournament_view.prompt_tournament_dated()
            time_control = self.tournament_view.prompt_tournament_time_control()
            description = self.tournament_view.prompt_tournament_description()

            self.user_view.separator_white()
            self.user_view.user_print_msg(f"tournoi : {name}")
            self.user_view.user_print_msg(f"adresse : {location}")
            self.user_view.user_print_msg(f"date : {dated}")
            self.user_view.user_print_msg(f"time control : {time_control}")
            self.user_view.user_print_msg(f"description : {description}")
            confirm = self.user_view.prompt_confirm()
            if confirm == "Y":
                tournament = Tournament(
                    name, location, dated, time_control, description
                )
                self.db_tournament.save_table_tournament(tournament)
                tournament_id = self.db_tournament.get_id_tournament(name)
                tournament.add_id(tournament_id)
                self.user_view.user_print_green_msg(
                    f"\nLe tournoi {name} est créé avec succés !"
                )
                self.user_view.separator_white()
                return tournament
            else:
                return None
        except Exception as err:
            logger.error("Oops! %s", err)

    def import_tournament(self):
        """Start a tournament in progress"""
        id = self.tournament_view.prompt_tournament_id()
        tournament_found = self.db_tournament.search_table_tournament_with_id(id)
        print(tournament_found)
        if tournament_found:
            self.tournament_view.print_one_tournament(tournament_found)
            confirm = self.user_view.prompt_confirm()
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
                        player_id = self.db_player.check_table_players(
                            player_import["last_name"], player_import["first_name"])
                        player.add_id(player_id)
                        player.add_score(player_import["score"])
                        player.add_ladder(player_import["ladder"])
                        tournament.append_list_players(player)
                if tournament_found["rounds"]:
                    for round_import in tournament_found["rounds"]:
                        print(round_import)
                        round = Round(round_import["list_matches"], round_import["created_at"], round_import["round"])
                        round.add_start = round_import["round_in_progress"]
                        round.add_finished = round_import["finished_at"]
                        tournament.append_list_rounds(round)
                        for match_import in round_import["list_matches"]:
                            match = Match(match_import["match"][0][0], match_import["match"][1][0],
                                          match_import["match"][0][1], match_import["match"][1][1])
                            round.append_list_matches(match)
                        tournament.counter_round
                tournament.add_id(tournament_found.doc_id)
                self.user_view.user_print_green_msg(
                    f"\nLe tournoi {tournament.get_name()} est importé avec succés !"
                )
                self.user_view.separator_white()
                return tournament
        else:
            self.user_view.user_print_err("Aucun tournoi en cours n'a été trouvé.")

    def start_rounds(self, tournament):
        """Start the rounds.

        Args:
            tournament (Object): Tournament instance
        """
        current_matches = []
        current_round = tournament.get_current_round()
        if current_round < 5:
            j = 1
            name = f"Round{current_round}"
            created_at = datetime.now()
            round = Round(tournament.get_list_players(), name, str(created_at))
            if current_round == 1:
                self.user_view.user_print_msg("Lancer le premier tour.")
                players = round.sort_elo_players()

            else:
                self.user_view.user_print_msg(f"{current_round}ème tour.")
                players = round.sort_score_players()
            players_pair = round.generate_pair(current_matches, players, current_round)
            self.round_view.print_players_pair(players_pair)
            self.user_view.separator_white()
            # to do confirm end of round !!!
            self.round_view.menu()
            user_choice = self.round_view.prompt_choice_menu_round()
            if user_choice == 1:
                self.start_round(players_pair, tournament, current_round, current_matches, j)
                finished_at = datetime.now()
                self.round.add_finished(finished_at)
                self.round.start()
            else:
                return None
        else:
            self.user_view.user_print_err("Ce tournoi est terminé !")

    def start_round(self, players_pair, tournament, current_round, current_matches, j):
        for player in players_pair:
            player_one = player[0]
            player_two = player[1]
            self.user_view.user_print_msg(f"MATCH : {j}")
            self.user_view.user_print_msg(f'{str(player_one)} vs ' f'{str(player_two)}\n')
            self.user_view.user_print_msg(f'Joueur : {str(player_one)}')
            score_player_one = self.round_view.prompt_set_score()
            player_one.add_score(score_player_one)
            self.user_view.user_print_msg(f'joueur : {str(player_two)}')
            score_player_two = self.round_view.prompt_set_score()
            player_two.add_score(score_player_two)
            match = Match(
                player_one.serialize_player_match(), player_two.serialize_player_match(), score_player_one, score_player_two
            )
            round.append_list_matches(match)
            j += 1
            self.user_view.separator_white()
        self.user_view.user_print_msg(f"\nTour {current_round} terminé.")
        self.user_view.separator_white()
        tournament.append_list_rounds(round)
        tournament.counter_round()
        self.db_tournament.update_table_tournament(tournament)
        del current_matches[:]
