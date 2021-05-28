"""Define the tournament controller."""

# librairies
from datetime import datetime
import time
from colorama import Fore

# models
from models.tournaments import Tournament
from models.players import Participant
from models.rounds import Round
from models.matches import Match

# controllers
from controllers._global import GlobalController


class TournamentController(GlobalController):
    """TournamentController controller."""

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def print_tournaments(self) -> list:
        """Method used to display all tournaments in the database

        Returns:
            tournaments (list): a list of players found in the database
        """
        self.user_view.header()
        if self.db_tournament.tournaments:
            self.tournament_view.menu_tournaments()
            self.tournament_view.print_header_tournament_array()
            for tournament in self.db_tournament.tournaments:
                self.tournament_view.print_tournament(
                    tournament.doc_id,
                    tournament["name"],
                    tournament["location"],
                    tournament["dated"],
                    tournament["time_control"],
                )
            return self.db_tournament.tournaments
        self.user_view.user_print_msg(
            Fore.LIGHTRED_EX + "Aucun tournoi n'a été trouvé dans la base de données."
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
            return

    def set_tournament(self) -> object:
        """Method used to creates a Tournament instance.
        if a tournament is created, the method redirects to a tournament submenu
        with the possibility of creating the list of participants.

        Returns:
            tournament (Tournament): a Tournament instance
        """
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
            tournament = Tournament(name, location, dated, time_control, description)
            self.db_tournament.save_table_tournament(tournament)
            tournament.tournament_id = self.db_tournament.get_id_tournament(name)
            self.user_view.user_print_msg(
                Fore.LIGHTGREEN_EX + f"\nLe tournoi {name} est créé avec succés !"
            )
            time.sleep(2.0)
            return tournament
        return None

    def import_tournament(self) -> object:
        """Method used to import a tournament in progress and create a Tournament instance.
        if a tournament is founded, the method redirects to a tournament submenu
        And resume where the tournament left off.

        Returns:
            tournament (Tournament): a Tournament instance
        """
        tournament_id = self.user_view.prompt_integer("tournoi", "l'id")
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
                        player.player_id = self.db_player.get_id_player(
                            player_import["last_name"], player_import["first_name"]
                        )
                        player.score = player_import["score"]
                        player.ladder = player_import["ladder"]
                        for opponent in player_import["opponents"]:
                            player.opponents.append(opponent)
                        tournament.players.append(player)
                if tournament_found["rounds"]:
                    for round_import in tournament_found["rounds"]:
                        round_game = Round(
                            round_import["list_matches"],
                            round_import["created_at"],
                            round_import["round"],
                        )
                        round_game.start = round_import["round_in_progress"]
                        round_game.finished_at = round_import["finished_at"]
                        tournament.rounds.append(round_game)
                        for match_import in round_import["list_matches"]:
                            match = Match(
                                match_import["match"][0][0],
                                match_import["match"][1][0],
                                match_import["match"][0][1],
                                match_import["match"][1][1],
                            )
                            round_game.matches.append(match)
                if tournament_found["current_players"]:
                    for player in tournament_found["current_players"]:
                        tournament.current_players.append(player)
                tournament.current_round = tournament_found["current_round"]
                if tournament.current_round == 5:
                    tournament.current_tournament = "Tournoi terminé"
                tournament.tournament_id = tournament_found.doc_id
                self.user_view.user_print_msg(
                    Fore.LIGHTGREEN_EX
                    + f"\nLe tournoi {tournament.name} est importé avec succés !"
                )
                time.sleep(2.0)
                return tournament
            return None
        self.user_view.user_print_msg(
            Fore.LIGHTRED_EX + "Aucun tournoi en cours n'a été trouvé."
        )
        time.sleep(2.0)
        return None

    def start_rounds(self, tournament: object) -> None:
        """Start the rounds.

        Args:
            tournament (Object): Tournament instance
        """
        if tournament.current_round <= 4:
            j = 1
            name = f"Round{tournament.current_round}"
            created_at = datetime.now()
            players = tournament.players
            round_game = Round(players, name, str(created_at))
            self.round_view.sub_round_menu()
            if tournament.current_round == 1:
                self.user_view.title_h2("Première ronde")
                players_pair = round_game.generate_pair_first_round(
                    round_game.sort_elo_players
                )
            else:
                self.user_view.title_h2(f"{tournament.current_round}ème tour.\n")
                players_pair = round_game.generate_pair(round_game.sort_score_players)
            self.round_view.print_header_players_pair_array()
            for player_one, player_two in players_pair:
                self.round_view.print_players_pair(player_one, player_two)
            user_choice = self.user_view.prompt_choice_menu(2)
            if user_choice == 1:
                self.user_view.header()
                self.start_round(round_game, players_pair, tournament, j)
            else:
                return
        else:
            self.user_view.user_print_msg(Fore.LIGHTRED_EX + "Ce tournoi est terminé !")
            time.sleep(2.0)
            return

    def start_round(
        self,
        round_game: object,
        players_pair: list,
        tournament: object,
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
            player_one.score += score_player_one
            self.user_view.user_print_msg(f"joueur : {str(player_two)}")
            score_player_two = self.round_view.prompt_set_score()
            player_two.score += score_player_two
            match = Match(
                player_one.serialize_player_match,
                player_two.serialize_player_match,
                score_player_one,
                score_player_two,
            )
            round_game.matches.append(match)
            j += 1
        tournament.rounds.append(round_game)
        tournament.current_round += 1
        round_game.finished_at = str(datetime.now())
        round_game.start = False
        if tournament.current_round == 5:
            ladder = 1
            for player in tournament.sort_score_players:
                player.ladder = ladder
                ladder += 1
            self.user_view.user_print_msg(
                Fore.LIGHTGREEN_EX
                + "TOURNOI TERMINÉ! Vous pouvez dés à present afficher les résultats."
            )
            tournament.current_tournament = "Tournoi terminé"
        else:
            self.user_view.user_print_msg(
                Fore.LIGHTGREEN_EX + f"\nTOUR {tournament.current_round} TERMINÉ."
            )
        self.db_tournament.update_table_tournament(tournament)
        time.sleep(2.0)
