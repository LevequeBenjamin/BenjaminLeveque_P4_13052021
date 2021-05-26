"""Define the tournament controller."""

# librairies
from datetime import datetime
import logging
import time
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
    """TournamentController controller."""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(self):
        """Inits TournamentController."""
        self.db_tournament = DbControllerTournament()
        self.db_player = DbControllerlPlayer()
        self.tournament_view = TournamentView()
        self.user_view = UserView()
        self.round_view = RoundView()

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def print_tournaments(self) -> list:
        """Method used to display all tournaments in the database

        Returns:
            tournaments (list): a list of players found in the database
        """
        self.user_view.header()
        tournaments = self.db_tournament.get_tournois
        if tournaments:
            self.tournament_view.menu_tournois()
            self.tournament_view.print_header_tournament_array()
            for tournament in tournaments:
                self.tournament_view.print_tournament(
                    tournament.doc_id,
                    tournament["name"],
                    tournament["location"],
                    tournament["dated"],
                    tournament["time_control"],
                )
            return tournaments
        else:
            self.user_view.user_print_msg(
                Fore.LIGHTRED_EX
                + "Aucun tournoi n'a été trouvé dans la base de données."
            )
            time.sleep(2.0)
            return None

    def print_result_tournament(self, tournament: object) -> None:
        """Method used to display tournament rankings."""
        self.tournament_view.print_current_tournament(tournament)
        self.user_view.title_h2("Résultat du tournoi")
        self.tournament_view.print_result_tournament(tournament.sort_score_players)
        confirm = self.user_view.prompt_return()
        if confirm == "Y":
            return None

    def set_tournament(self) -> object:
        """Method used to creates a Tournament instance.
        if a tournament is created, the method redirects to a tournament submenu
        with the possibility of creating the list of participants.

        Returns:
            tournament (Tournament): a Tournament instance
        """
        try:
            name = self.user_view.prompt_string("tournoi", "le nom")
            location = self.user_view.prompt_string("tournoi", "l'adresse")
            dated = self.user_view.prompt_string("tournoi", "la date")
            time_control = self.tournament_view.prompt_tournament_time_control()
            description = self.user_view.prompt_string("tournoi", "la description")
            self.tournament_view.print_confirm_tournament(
                name, location, dated, time_control, description
            )
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
                time.sleep(2.0)
                return tournament
            else:
                return None
        except Exception as err:
            logger.error("Oops! %s", err)
            time.sleep(2.0)

    def import_tournament(self) -> object:
        """Method used to import a tournament in progress and create a Tournament instance.
        if a tournament is founded, the method redirects to a tournament submenu
        And resume where the tournament left off.

        Returns:
            tournament (Tournament): a Tournament instance
        """
        tournament_id = self.user_view.prompt_id("tournoi", "l'id")
        tournament_found = self.db_tournament.search_table_tournament_with_id(
            tournament_id
        )
        if tournament_found:
            self.tournament_view.print_header_tournament_array()
            self.tournament_view.print_tournament(
                tournament_found.doc_id,
                tournament_found["name"],
                tournament_found["location"],
                tournament_found["dated"],
                tournament_found["time_control"],
            )
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
                        player = Participant(
                            player_import["last_name"],
                            player_import["first_name"],
                            player_import["birth_date"],
                            player_import["sex"],
                            player_import["elo"],
                        )
                        player_id = self.db_player.get_id_player(
                            player_import["last_name"], player_import["first_name"]
                        )
                        player.add_id(player_id)
                        player.add_score(player_import["score"])
                        player.add_ladder(player_import["ladder"])
                        for opponent in player_import["opponents"]:
                            player.append_list_opponents(opponent)
                        tournament.append_list_players(player)
                if tournament_found["rounds"]:
                    for round_import in tournament_found["rounds"]:
                        round = Round(
                            round_import["list_matches"],
                            round_import["created_at"],
                            round_import["round"],
                        )
                        round.add_start = round_import["round_in_progress"]
                        round.add_finished = round_import["finished_at"]
                        tournament.append_list_rounds(round)
                        for match_import in round_import["list_matches"]:
                            match = Match(
                                match_import["match"][0][0],
                                match_import["match"][1][0],
                                match_import["match"][0][1],
                                match_import["match"][1][1],
                            )
                            round.append_list_matches(match)
                            tournament.counter_round()
                        if tournament.get_current_round == 5:
                            tournament.finished_tournament()
                tournament.add_id(tournament_found.doc_id)
                self.user_view.user_print_green_msg(
                    f"\nLe tournoi {tournament.get_name} est importé avec succés !"
                )
                time.sleep(2.0)
                return tournament
        else:
            self.user_view.user_print_err("Aucun tournoi en cours n'a été trouvé.")
            time.sleep(2.0)

    def start_rounds(self, tournament: object) -> None:
        """Start the rounds.

        Args:
            tournament (Object): Tournament instance
        """
        current_round = tournament.get_current_round
        if current_round <= 4:
            j = 1
            name = f"Round{current_round}"
            created_at = datetime.now()
            round = Round(tournament.get_list_players, name, str(created_at))
            self.round_view.menu()
            if current_round == 1:
                self.user_view.title_h2("Première ronde")
                players_pair = round.generate_pair_first_round(round.sort_elo_players)
            else:
                self.user_view.title_h2(f"{current_round}ème tour.\n")
                players_pair = round.generate_pair(round.sort_score_players)
            self.round_view.print_header_players_pair_array()
            for player_one, player_two in players_pair:
                self.round_view.print_players_pair(player_one, player_two)
            self.round_view.print_players_pair(players_pair)
            user_choice = self.round_view.prompt_choice_menu_round()
            if user_choice == 1:
                self.user_view.header()
                self.start_round(round, players_pair, tournament, current_round, j)
            else:
                return None
        else:
            self.user_view.user_print_err("Ce tournoi est terminé !")
            time.sleep(2.0)

    def start_round(
        self,
        round: object,
        players_pair: list,
        tournament: object,
        current_round: int,
        j: int,
    ) -> None:
        """This method manages the matches of a round.

        Args:
            round (object): a Round instance.
            players_pair (list): a list of players pair.
            tournament (object): a Tournament instance.
            current_round (int): a current round.
            j (int): a match counter.
        """
        for player_one, player_two in players_pair:
            self.user_view.title_h2(f"MATCH : {j}")
            self.round_view.print_header_players_pair_array()
            self.round_view.print_players_pair(player_one, player_two)
            self.user_view.user_print_msg(f"\nJoueur : {str(player_one)}\n")
            score_player_one = self.round_view.prompt_set_score()
            player_one.add_score(score_player_one)
            self.user_view.user_print_msg(f"joueur : {str(player_two)}")
            score_player_two = self.round_view.prompt_set_score()
            player_two.add_score(score_player_two)
            match = Match(
                player_one.serialize_player_match(),
                player_two.serialize_player_match(),
                score_player_one,
                score_player_two,
            )
            round.append_list_matches(match)
            j += 1
        tournament.append_list_rounds(round)
        tournament.counter_round()
        finished_at = datetime.now()
        round.add_finished(str(finished_at))
        round.add_start()
        if tournament.get_current_round == 5:
            ladder = 1
            players = tournament.sort_score_players
            for player in players:
                player.add_ladder(ladder)
                ladder += 1
            self.user_view.user_print_green_msg(
                "TOURNOI TERMINÉ! Vous pouvez dés à present afficher les résultats."
            )
            tournament.finished_tournament()
        else:
            self.user_view.user_print_green_msg(f"\nTOUR {current_round} TERMINÉ.")
        self.db_tournament.update_table_tournament(tournament)
        time.sleep(2.0)
